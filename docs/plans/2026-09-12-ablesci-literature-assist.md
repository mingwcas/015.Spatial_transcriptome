# AbleSci Literature Assist Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a portable Agent Skill and Playwright CLI that logs into AbleSci, posts an explicitly authorized DOI request, waits for assistance, accepts the matching file, downloads it, and verifies the PDF.

**Architecture:** Keep `SKILL.md` as a thin harness-facing contract and put deterministic behavior in an ESM Node.js CLI. Model the site workflow as resumable state transitions, use role/label-first Playwright selectors, and isolate live-site tests from offline unit tests.

**Tech Stack:** Node.js 24, npm, Playwright, dotenv, built-in `node:test`, ESM JavaScript.

---

### Task 1: Scaffold the portable skill package and protect local secrets

**Files:**
- Create: `tools/ablesci-literature-assist/package.json`
- Create: `tools/ablesci-literature-assist/.env.example`
- Create: `tools/ablesci-literature-assist/scripts/ablesci.mjs`
- Create: `tools/ablesci-literature-assist/src/cli.mjs`
- Modify: `.gitignore`

**Step 1: Add a failing CLI smoke test**

Create `tools/ablesci-literature-assist/tests/cli.test.mjs`:

```js
import test from "node:test";
import assert from "node:assert/strict";
import { parseArgs } from "../src/cli.mjs";

test("parseArgs recognizes doctor", () => {
  assert.deepEqual(parseArgs(["doctor"]), { command: "doctor", options: {} });
});
```

**Step 2: Run the test and verify failure**

Run: `cd tools/ablesci-literature-assist && node --test tests/cli.test.mjs`

Expected: FAIL because `src/cli.mjs` does not exist.

**Step 3: Add the minimal package and CLI parser**

`package.json`:

```json
{
  "name": "ablesci-literature-assist",
  "version": "0.1.0",
  "private": true,
  "type": "module",
  "scripts": {
    "test": "node --test tests/*.test.mjs",
    "doctor": "node scripts/ablesci.mjs doctor"
  },
  "dependencies": {
    "dotenv": "^17.2.2",
    "playwright": "^1.63.0"
  }
}
```

`src/cli.mjs`:

```js
export function parseArgs(argv) {
  const [command, ...rest] = argv;
  const options = {};
  for (let i = 0; i < rest.length; i += 1) {
    if (!rest[i].startsWith("--")) throw new Error(`Unexpected argument: ${rest[i]}`);
    const key = rest[i].slice(2).replaceAll("-", "_");
    const next = rest[i + 1];
    if (!next || next.startsWith("--")) options[key] = true;
    else { options[key] = next; i += 1; }
  }
  return { command, options };
}
```

`scripts/ablesci.mjs`:

```js
#!/usr/bin/env node
import { main } from "../src/cli.mjs";

process.exitCode = await main(process.argv.slice(2));
```

Add `.env.example` with empty `ABLESCI_EMAIL`, `ABLESCI_PASSWORD`, `ABLESCI_DOWNLOAD_DIR`, plus documented non-secret defaults. Add these root `.gitignore` entries:

```gitignore
.env
.env.*
!.env.example
**/.state/
**/downloads/
**/test-results/
**/playwright-report/
**/*.zip
```

Do not add a global `*.pdf` rule because the repository intentionally tracks some reports and references.

**Step 4: Run the smoke test**

Run: `cd tools/ablesci-literature-assist && node --test tests/cli.test.mjs`

Expected: PASS.

**Step 5: Commit**

```bash
git add .gitignore tools/ablesci-literature-assist/package.json tools/ablesci-literature-assist/.env.example tools/ablesci-literature-assist/scripts/ablesci.mjs tools/ablesci-literature-assist/src/cli.mjs tools/ablesci-literature-assist/tests/cli.test.mjs
git commit -m "feat: scaffold AbleSci automation skill"
```

### Task 2: Implement DOI validation and configuration

**Files:**
- Create: `tools/ablesci-literature-assist/src/doi.mjs`
- Create: `tools/ablesci-literature-assist/src/config.mjs`
- Create: `tools/ablesci-literature-assist/tests/doi.test.mjs`
- Create: `tools/ablesci-literature-assist/tests/config.test.mjs`

**Step 1: Write failing DOI and config tests**

Test these exact invariants:

```js
assert.equal(normalizeDoi(" https://doi.org/10.1038/S41592-026-03217-4 "), "10.1038/s41592-026-03217-4");
assert.throws(() => normalizeDoi("not-a-doi"), /Invalid DOI/);
assert.equal(loadConfig({ ABLESCI_HEADLESS: "true" }).headless, true);
assert.throws(() => loadConfig({}), /ABLESCI_EMAIL/);
assert.equal(redact("login failed for secret", ["secret"]), "login failed for [REDACTED]");
```

**Step 2: Run tests and verify failure**

Run: `cd tools/ablesci-literature-assist && node --test tests/doi.test.mjs tests/config.test.mjs`

Expected: FAIL because modules do not exist.

**Step 3: Implement minimal pure functions**

Use the DOI pattern `^10\.\d{4,9}/[-._;()/:a-z0-9]+$` after stripping a `doi:` or `https://doi.org/` prefix and lowercasing. `loadConfig` must validate required credentials only for commands that need login, resolve the download directory to an absolute path, bound poll interval to at least 5 seconds, and never return a printable combined credential string.

**Step 4: Run tests**

Run: `cd tools/ablesci-literature-assist && npm test`

Expected: all tests PASS.

**Step 5: Commit**

```bash
git add tools/ablesci-literature-assist/src/doi.mjs tools/ablesci-literature-assist/src/config.mjs tools/ablesci-literature-assist/tests/doi.test.mjs tools/ablesci-literature-assist/tests/config.test.mjs
git commit -m "feat: validate DOI and AbleSci configuration"
```

### Task 3: Add browser lifecycle, login, and doctor command

**Files:**
- Create: `tools/ablesci-literature-assist/src/browser.mjs`
- Create: `tools/ablesci-literature-assist/src/selectors.mjs`
- Create: `tools/ablesci-literature-assist/tests/browser.test.mjs`
- Modify: `tools/ablesci-literature-assist/src/cli.mjs`

**Step 1: Write tests against mocked Playwright objects**

Test that login:

```js
assert.deepEqual(actions, [
  ["goto", "https://www.ablesci.com/site/login"],
  ["fill", "登录邮箱（必填）", "user@example.com"],
  ["fill", "登录密码（必填）", "[secret supplied but not logged]"],
  ["click", "登录"]
]);
```

Also test that a page containing `验证码`, `二次验证`, or `异常登录` produces `USER_ACTION_REQUIRED` and does not retry.

**Step 2: Run tests and verify failure**

Run: `cd tools/ablesci-literature-assist && node --test tests/browser.test.mjs`

Expected: FAIL because browser module does not exist.

**Step 3: Implement browser helpers**

Launch installed Chrome with Playwright `chromium.launch({ channel: "chrome", headless })`. Create a context with `acceptDownloads: true`, locale `zh-CN`, and an optional storage-state file. Implement selector helpers that require exactly one visible match for critical actions.

Login sequence:

```js
await page.goto(`${baseUrl}/site/login`, { waitUntil: "domcontentloaded" });
await page.getByRole("combobox", { name: "登录邮箱（必填）" }).fill(email);
await page.getByRole("textbox", { name: "登录密码（必填）" }).fill(password);
await page.getByRole("button", { name: "登录", exact: true }).click();
```

If visible, click `继续访问`. Confirm success through a logged-in username/menu signal, then call `context.storageState({ path })`.

`doctor` checks Node major version, Chrome channel launch, download directory writability, and configuration names without echoing values.

**Step 4: Install dependencies and run offline tests**

Run: `cd tools/ablesci-literature-assist && npm install && npm test`

Expected: package lock created; all offline tests PASS.

**Step 5: Run doctor**

Run: `cd tools/ablesci-literature-assist && node scripts/ablesci.mjs doctor`

Expected: JSON with `ok: true`, `node`, `chrome`, and `downloadDir` checks.

**Step 6: Commit**

```bash
git add tools/ablesci-literature-assist/package.json tools/ablesci-literature-assist/package-lock.json tools/ablesci-literature-assist/src tools/ablesci-literature-assist/tests
git commit -m "feat: add AbleSci browser and login automation"
```

### Task 4: Implement resumable request creation and duplicate protection

**Files:**
- Create: `tools/ablesci-literature-assist/src/workflows.mjs`
- Create: `tools/ablesci-literature-assist/src/result.mjs`
- Create: `tools/ablesci-literature-assist/tests/state-machine.test.mjs`
- Modify: `tools/ablesci-literature-assist/src/cli.mjs`

**Step 1: Write failing state and authorization tests**

Required tests:

```js
assert.throws(() => authorizePublish({ confirm_publish: false }), /--confirm-publish/);
assert.equal(nextState("AUTHENTICATED", "duplicate-found"), "REQUEST_FOUND");
assert.equal(nextState("AUTHENTICATED", "new-request"), "REQUEST_CREATED");
assert.throws(() => nextState("DOWNLOADED", "publish"), /Invalid transition/);
```

Add a test proving a duplicate DOI returns the existing detail URL without clicking the publish button.

**Step 2: Run tests and verify failure**

Run: `cd tools/ablesci-literature-assist && node --test tests/state-machine.test.mjs`

Expected: FAIL because workflow module does not exist.

**Step 3: Implement the request workflow**

Use `/my/assist-my` for duplicate lookup and `/assist/create` for creation. Scope button locators to the relevant dialog. Before the final publish click, require `options.confirm_publish === true`.

Creation sequence:

```js
await page.getByText("一键求助", { exact: true }).locator("..").getByRole("textbox").fill(doi);
await page.getByRole("button", { name: "智能提取文献信息" }).click();
await page.getByRole("button", { name: "信息正确，直接发布" }).click();
await page.getByRole("button", { name: "查看求助详情" }).click();
```

Do not assume the exact textbox structure until the authenticated page is inspected; if the region locator is different, capture it in `selectors.mjs` and its fixture test. Persist `runId`, normalized DOI, state, title, detail URL, and timestamps under `.state/runs/`, never credentials.

**Step 4: Run tests**

Run: `cd tools/ablesci-literature-assist && npm test`

Expected: all tests PASS.

**Step 5: Commit**

```bash
git add tools/ablesci-literature-assist/src tools/ablesci-literature-assist/tests
git commit -m "feat: create idempotent AbleSci requests"
```

### Task 5: Implement polling and exact-match acceptance

**Files:**
- Modify: `tools/ablesci-literature-assist/src/workflows.mjs`
- Create: `tools/ablesci-literature-assist/tests/acceptance.test.mjs`

**Step 1: Write failing tests**

Cover:

- First status check occurs after 60 seconds for a newly created request.
- Later checks use `ABLESCI_POLL_INTERVAL_MS`.
- `采纳文件` uses two confirmations and verifies the status afterward.
- Batch fallback selects only a row whose normalized DOI or saved title matches.
- More than one matching candidate returns `USER_ACTION_REQUIRED`.
- No match before timeout returns `NOT_READY` and preserves the detail URL.

**Step 2: Run tests and verify failure**

Run: `cd tools/ablesci-literature-assist && node --test tests/acceptance.test.mjs`

Expected: FAIL because acceptance functions do not exist.

**Step 3: Implement detail-first acceptance**

Use a loop with deadline arithmetic instead of repeated fixed sleeps. After each potentially mutating click, read the current site state before retrying. For native JavaScript confirm dialogs, use Playwright's dialog event; for HTML dialogs, scope `确定` to the visible dialog.

Batch fallback must navigate through the user menu to `文献互助`, open `待确认`, find the exact saved DOI/title row, select that row only, and click `批量采纳所选项`. Never use page-wide “全选”.

**Step 4: Run tests**

Run: `cd tools/ablesci-literature-assist && npm test`

Expected: all tests PASS.

**Step 5: Commit**

```bash
git add tools/ablesci-literature-assist/src/workflows.mjs tools/ablesci-literature-assist/tests/acceptance.test.mjs
git commit -m "feat: poll and accept matching AbleSci files"
```

### Task 6: Implement safe download and PDF verification

**Files:**
- Create: `tools/ablesci-literature-assist/src/download.mjs`
- Create: `tools/ablesci-literature-assist/tests/download-validation.test.mjs`
- Modify: `tools/ablesci-literature-assist/src/workflows.mjs`

**Step 1: Write failing validation tests**

Using `tmpDir`, test:

```js
assert.deepEqual(await validatePdf(validPdf), {
  valid: true,
  size: 15,
  sha256: expectedHash
});
assert.equal((await validatePdf(htmlFile)).valid, false);
assert.equal((await validatePdf(emptyFile)).reason, "empty-file");
```

**Step 2: Run tests and verify failure**

Run: `cd tools/ablesci-literature-assist && node --test tests/download-validation.test.mjs`

Expected: FAIL because download module does not exist.

**Step 3: Implement download capture**

Use `Promise.all([page.waitForEvent("download"), downloadButton.click()])`. Save to a `.part` path inside the configured directory, validate the header before renaming, and produce a safe filename such as `10.1038_s41592-026-03217-4.pdf`. Reject path traversal and HTML content.

**Step 4: Run tests**

Run: `cd tools/ablesci-literature-assist && npm test`

Expected: all tests PASS.

**Step 5: Commit**

```bash
git add tools/ablesci-literature-assist/src/download.mjs tools/ablesci-literature-assist/src/workflows.mjs tools/ablesci-literature-assist/tests/download-validation.test.mjs
git commit -m "feat: download and verify AbleSci PDFs"
```

### Task 7: Author the cross-harness SKILL.md and references

**Files:**
- Create: `tools/ablesci-literature-assist/SKILL.md`
- Create: `tools/ablesci-literature-assist/references/workflow.md`
- Create: `tools/ablesci-literature-assist/references/troubleshooting.md`
- Create: `tools/ablesci-literature-assist/tests/skill-structure.test.mjs`

**Step 1: Write a failing structure test**

Assert that `SKILL.md`:

- starts with YAML frontmatter;
- declares `name: ablesci-literature-assist`;
- has a description no longer than 60 characters and ending with a period;
- declares `required_environment_variables` for email and password;
- contains `When to Use`, `Prerequisites`, `How to Run`, `Quick Reference`, `Procedure`, `Pitfalls`, and `Verification`;
- references the CLI using skill-relative paths;
- does not contain a machine-local absolute path.

**Step 2: Run test and verify failure**

Run: `cd tools/ablesci-literature-assist && node --test tests/skill-structure.test.mjs`

Expected: FAIL because `SKILL.md` does not exist.

**Step 3: Write SKILL.md**

Use compatible frontmatter:

```yaml
---
name: ablesci-literature-assist
description: Request and download authorized papers through AbleSci.
version: 0.1.0
author: Ming Wang, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
required_environment_variables:
  - name: ABLESCI_EMAIL
    prompt: AbleSci login email
    help: Configure locally; never send it in chat.
    required_for: AbleSci login
  - name: ABLESCI_PASSWORD
    prompt: AbleSci login password
    help: Configure locally; never send it in chat.
    required_for: AbleSci login
metadata:
  hermes:
    tags: [research, literature, pdf, browser-automation]
    related_skills: []
    requires_toolsets: [terminal]
---
```

In the body, require explicit DOI scope and `--confirm-publish` before publishing. Tell the agent to invoke the shipped script through its terminal capability, parse JSON stdout, report the saved PDF path, and stop for CAPTCHA, multiple candidates, or site changes.

**Step 4: Run all tests**

Run: `cd tools/ablesci-literature-assist && npm test`

Expected: all tests PASS.

**Step 5: Commit**

```bash
git add tools/ablesci-literature-assist/SKILL.md tools/ablesci-literature-assist/references tools/ablesci-literature-assist/tests/skill-structure.test.mjs
git commit -m "docs: add portable AbleSci agent skill"
```

### Task 8: Add installation adapters without duplicating the skill

**Files:**
- Create: `tools/ablesci-literature-assist/scripts/install.mjs`
- Create: `tools/ablesci-literature-assist/tests/install.test.mjs`
- Modify: `tools/ablesci-literature-assist/package.json`

**Step 1: Write failing install-path tests**

Test resolver results for:

```js
assert.equal(resolveTarget("hermes", home), join(home, ".hermes", "skills", "ablesci-literature-assist"));
assert.equal(resolveTarget("codex", home), join(home, ".codex", "skills", "ablesci-literature-assist"));
assert.throws(() => resolveTarget("unknown", home), /Unsupported harness/);
```

**Step 2: Run tests and verify failure**

Run: `cd tools/ablesci-literature-assist && node --test tests/install.test.mjs`

Expected: FAIL because installer does not exist.

**Step 3: Implement copy/link installation**

Default to copying the complete skill directory while excluding `.env`, `.state`, `downloads`, test output, and `node_modules`. Support `--link` for local development and `--target PATH` for an unknown DeepSeek harness. Refuse to overwrite an existing non-link target unless `--force` is explicit.

Add scripts:

```json
{
  "install:hermes": "node scripts/install.mjs --harness hermes",
  "install:codex": "node scripts/install.mjs --harness codex"
}
```

**Step 4: Run tests in a temporary HOME fixture**

Run: `cd tools/ablesci-literature-assist && npm test`

Expected: copied target contains `SKILL.md` and scripts but no secret/runtime files.

**Step 5: Commit**

```bash
git add tools/ablesci-literature-assist/scripts/install.mjs tools/ablesci-literature-assist/tests/install.test.mjs tools/ablesci-literature-assist/package.json
git commit -m "feat: install AbleSci skill across agent harnesses"
```

### Task 9: Perform staged local verification

**Files:**
- Modify only if a verified defect requires a focused fix.

**Step 1: Run offline verification**

Run:

```bash
cd tools/ablesci-literature-assist
npm ci
npm test
node scripts/ablesci.mjs doctor
```

Expected: tests PASS and doctor returns `ok: true`.

**Step 2: Create local credentials outside Git**

Copy `.env.example` to `.env`, then let the user enter `ABLESCI_EMAIL` and `ABLESCI_PASSWORD` locally. Never request the password in chat and never commit `.env`.

**Step 3: Run login-only smoke test**

Run: `node scripts/ablesci.mjs login`

Expected: JSON status `AUTHENTICATED`; `.state/ablesci-storage-state.json` exists; no request was published.

**Step 4: Verify Hermes discovery after Hermes itself is healthy**

Run installer into `~/.hermes/skills/`, start a fresh Hermes session, and list/view the skill. Do not run `hermes` commands until the separate interrupted-upgrade issue is repaired or explicitly waived.

Expected: Hermes finds `ablesci-literature-assist` and loads its instructions.

**Step 5: Ask for explicit live DOI authorization**

Do not reuse the documentation example automatically. The user must identify the DOI to publish in this live test.

**Step 6: Run one end-to-end request**

Run: `node scripts/ablesci.mjs run --doi "USER_AUTHORIZED_DOI" --confirm-publish`

Expected: final JSON state `VERIFIED`, absolute PDF path, byte size, SHA-256, detail URL, and no credential material.

**Step 7: Inspect Git scope and commit any verified fixes**

Run: `git status --short` and `git diff -- tools/ablesci-literature-assist .gitignore`.

Expected: no `.env`, state, downloads, screenshots, or unrelated workspace files are staged.


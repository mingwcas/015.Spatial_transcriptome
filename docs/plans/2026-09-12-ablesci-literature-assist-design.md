# AbleSci 文献求助自动化 Skill 设计

## 目标

构建一个遵循 Agent Skills `SKILL.md` 约定的可移植技能，由 Hermes Agent、DeepSeek 类 harness 或普通命令行调用。技能通过确定性的 Node.js/Playwright CLI 完成 AbleSci 登录、发布 DOI 求助、等待应助、采纳和 PDF 下载。

首版面向本机 macOS + Chrome 测试，同时保持脚本可在 Linux、macOS 和 Windows 上运行。它不绕过验证码、登录权限、付费墙或站点限制，也不传播下载文件。

## 已确认环境

- macOS 26.5，Apple Silicon。
- Node.js 24、npm 11、Bun、Python、Git、Docker 可用。
- Google Chrome 153 已安装。
- `https://www.ablesci.com/` 可访问。
- 尚未安装 Playwright、Puppeteer 或 Selenium。
- Hermes Agent 0.21.1 位于本机；Hermes 用户技能目录为 `~/.hermes/skills/`。
- Hermes 当前存在一次未完成升级导致的架构依赖错误。该问题与 AbleSci 技能分开处理，不能把修复 Hermes 当作本项目的隐式副作用。
- 当前仓库 `.gitignore` 没有保护 `.env`、浏览器登录状态、下载文件、截图和跟踪文件。

## 已确认网站表面

- 登录页：`/site/login`。
- 登录邮箱字段的可访问名称：`登录邮箱（必填）`。
- 密码字段的可访问名称：`登录密码（必填）`。
- 登录提交按钮具有文本 `登录` 和 ID `able-login-submit`。
- 发布入口：`/assist/create`，可访问名称包含 `发布文献求助`。
- 当前登录流程没有验证码。

这些信息只是选择器初始基线。实现必须使用多级定位策略，并在站点结构变化时失败关闭，不能依赖坐标。

## 方案选择

### 采用：Skill + Playwright CLI

`SKILL.md` 负责触发条件、授权边界、调用协议和结果解释；Playwright CLI 负责确定性的网页操作、状态持久化、轮询和下载验证。

与纯提示词浏览器操作相比，该方案更容易测试、重试和处理下载。与完整 MCP 插件相比，依赖少且更容易被不同 harness 调用。若首版稳定，再把相同 CLI 包装成 MCP server，而不重写业务逻辑。

## 目录结构

```text
tools/ablesci-literature-assist/
├── SKILL.md
├── package.json
├── package-lock.json
├── .env.example
├── scripts/
│   └── ablesci.mjs
├── src/
│   ├── cli.mjs
│   ├── config.mjs
│   ├── doi.mjs
│   ├── browser.mjs
│   ├── selectors.mjs
│   ├── workflows.mjs
│   ├── download.mjs
│   └── result.mjs
├── references/
│   ├── workflow.md
│   └── troubleshooting.md
└── tests/
    ├── doi.test.mjs
    ├── config.test.mjs
    ├── state-machine.test.mjs
    └── download-validation.test.mjs
```

项目目录是可版本化的唯一源。安装时将整个目录复制或链接到 harness 的技能目录；Hermes 目标为 `~/.hermes/skills/ablesci-literature-assist/`。不直接在 Hermes 源码仓库中开发。

## 对外命令

```bash
node scripts/ablesci.mjs doctor
node scripts/ablesci.mjs login
node scripts/ablesci.mjs request --doi DOI --confirm-publish
node scripts/ablesci.mjs poll --doi DOI
node scripts/ablesci.mjs accept --doi DOI
node scripts/ablesci.mjs download --doi DOI
node scripts/ablesci.mjs run --doi DOI --confirm-publish
node scripts/ablesci.mjs batch-accept
```

所有命令把机器可读 JSON 写到 stdout，把进度和诊断写到 stderr。退出码 `0` 表示完成，`2` 表示输入或配置错误，`3` 表示需要用户处理，`4` 表示站点状态暂未满足，`5` 表示网站结构或网络错误。

## 配置与凭据

```dotenv
ABLESCI_EMAIL=
ABLESCI_PASSWORD=
ABLESCI_DOWNLOAD_DIR=
ABLESCI_HEADLESS=false
ABLESCI_TIMEOUT_MS=300000
ABLESCI_POLL_INTERVAL_MS=15000
```

- 邮箱和密码属于敏感配置，只能从环境变量或本机 `.env` 读取。
- CLI 不打印密码，不把密码放入 URL、截图、trace 或错误对象。
- 非敏感配置可以由 CLI 参数覆盖。
- 浏览器登录状态保存在被忽略的 `.state/ablesci-storage-state.json`。
- 首版允许每次从 `.env` 自动登录；已有会话有效时直接复用。
- 若将来出现验证码、二次验证或异常登录确认，流程停止并返回 `USER_ACTION_REQUIRED`，不尝试绕过。

## 工作流与状态机

```text
INPUT_VALIDATED
  → AUTHENTICATED
  → DUPLICATE_CHECKED
  → REQUEST_CREATED
  → WAITING_FOR_ASSISTANCE
  → FILE_AVAILABLE
  → ACCEPTED
  → DOWNLOADED
  → VERIFIED
```

### 登录

1. 打开登录页。
2. 通过 label/role 填写邮箱和密码。
3. 点击登录。
4. 若出现“继续访问”，点击并等待返回站点。
5. 以用户名菜单或登出入口作为成功信号，保存 storage state。

### 发布

1. 规范化并验证 DOI。
2. 进入“我的求助”，先按 DOI 检查是否已有进行中、待确认或已完结条目。
3. 只有调用中出现 `--confirm-publish` 才允许提交新求助。
4. 打开发布页，在“一键求助”中输入 DOI。
5. 点击“智能提取文献信息”。
6. 验证弹窗内 DOI/题目存在，再点击“信息正确，直接发布”。
7. 点击“查看求助详情”，保存详情 URL、标题和创建时间。

### 等待与采纳

1. 发布后先等待 60 秒。
2. 此后按配置间隔刷新详情，直到出现“采纳文件”、到达超时或页面明确失败。
3. 默认采用单条详情页的“采纳文件”流程，并处理两个确认步骤。
4. 单条入口不存在但“待确认”中存在精确 DOI/题目匹配时，才使用批量页面作为回退。
5. 批量回退只选择本次 DOI 对应条目；不得无条件全选其他求助。

### 下载与验证

1. 捕获 Playwright download 事件，不依赖 macOS“另存为”窗口。
2. 保存到配置目录中的临时 `.part` 文件，再原子改名为最终文件。
3. 文件名优先采用 DOI 的安全形式，并保留服务器建议扩展名。
4. 验证文件非空、文件头为 `%PDF-`，并记录字节数和 SHA-256。
5. 如果下载内容实际是 HTML 登录页或错误页，删除临时文件并返回失败。

## 选择器策略

从稳定到脆弱依次使用：

1. `getByRole` + 精确可访问名称。
2. `getByLabel` 或 `getByPlaceholder`。
3. 稳定 ID，例如 `#able-login-submit`。
4. 与页面区域组合的文本定位。
5. CSS 结构定位仅作最后回退。

任何关键按钮出现多个匹配时停止，记录去敏截图和当前 URL，不通过 `.first()` 猜测。

## 幂等性与恢复

- 发布前查重，避免重复消耗积分。
- 每一步把非敏感状态写入 `.state/runs/<run-id>.json`。
- `run` 可从详情 URL 和最近已完成状态恢复。
- 接受已采纳、已下载作为幂等成功。
- 网络错误可有限重试；提交发布和采纳确认不能盲目重放，必须先读取网站状态。

## 错误处理

- 缺少凭据：`CONFIG_ERROR`。
- 登录失败：`AUTH_FAILED`，不输出密码。
- 验证码/二次验证：`USER_ACTION_REQUIRED`。
- DOI 已存在：返回已有条目，不再次发布。
- 尚无应助：`NOT_READY`，保留详情 URL。
- 多个候选文件：`USER_ACTION_REQUIRED`，列出非敏感元数据供用户选择。
- 选择器漂移：`SITE_CHANGED`，保存去敏诊断。
- 非 PDF 下载：`INVALID_DOWNLOAD`。

## 测试策略

### 离线测试

- DOI 规范化和非法输入。
- `.env` 配置解析与秘密脱敏。
- 状态转换、重试上限和幂等恢复。
- PDF 文件头、空文件、HTML 错误页和 SHA-256。
- 通过 HTML fixture 检查关键选择器，不访问实时网站。

### 实时烟雾测试

- `doctor`：检查 Node、Chrome、Playwright 和下载目录。
- `login`：使用用户本地凭据验证自动填写和登录，不发布求助。
- 发布测试必须由用户提供本次要请求的 DOI，并显式使用 `--confirm-publish`。
- 下载完成必须报告绝对路径、文件大小和校验值。

## 安全与合规边界

- 只对用户明确指定的 DOI 发布求助。
- 不批量采纳不属于本次运行的条目。
- 不保存或输出明文凭据。
- 不绕过网站安全机制或内容访问权限。
- 下载文件仅供用户个人学习研究，遵守 AbleSci 页面所示规则与适用版权要求。
- 自动化频率保持保守，不并发轰炸站点。

## 首版完成标准

- 离线测试全部通过。
- `doctor` 在测试机通过。
- `login` 能从 `.env` 自动填写并验证登录。
- 用户明确授权一个 DOI 后，可完成发布、等待、精确采纳、下载和 PDF 验证。
- Hermes 可从 `~/.hermes/skills/` 发现该技能并调用 CLI。
- 未安装 Hermes 的环境仍可直接通过 Node.js CLI 使用。

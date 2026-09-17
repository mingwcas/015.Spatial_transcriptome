#!/bin/bash
# batch_process.sh — 由 cron 驱动，每天北京时间 0:05 执行
# 依赖：dsh (DeepSeek Harness CLI), python3, git

set -e

PROJECT_DIR="/Users/mingwang/Documents/LabM/015.空间转录组"
LOG_FILE="$PROJECT_DIR/.batch_log"
BATCH_SIZE=3
cd "$PROJECT_DIR"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "======== 开始执行 ========"

# 读取待处理论文：只取 "## 待处理论文" 章节下的表格行
pending_file="$PROJECT_DIR/.pending_papers.txt"
sed -n '/^## 待处理论文/,/^---/p' "$PROJECT_DIR/09_生信分析/progress.md" \
    | grep '^|' \
    | grep -v '^| 顺序 \|^|---' \
    | head -n "$BATCH_SIZE" \
    > "$pending_file"

count=$(wc -l < "$pending_file" 2>/dev/null || echo 0)
if [ "$count" -eq 0 ] || [ ! -s "$pending_file" ]; then
    log "✅ 所有论文已完成，退出"
    exit 0
fi

log "本轮处理 $count 篇论文:"
while IFS='|' read -r _ _ plat year journal author _; do
    log "  -$plat $year $journal $author"
done < "$pending_file"

# 构建任务提示词
TASK="你是一个学术论文生信分析助手。请从 progress.md 读取待处理论文队列，按顺序处理前${count}篇。

重要提醒：
1. 每次处理论文前必须先读 09_生信分析/AGENT.md 了解规范
2. 每篇论文输出到独立目录，命名格式：{platform}.{序号5位}.{年份}.{期刊缩写}.{作者姓}
3. 每个论文子目录包含：
   - 01_metadata/metadata.json（由 extract_pdf_metadata.py 生成）
   - 02_methods/（每个方法1个文件，命名 01_MethodName.md）
   - 03_figures/（每张图1个文件，命名 Fig.01_Title.md）
   - 04_reports/01_Bioinfo_Report_4D.md
   - 05_pipeline_inventory/01_Code_Data_Inventory.md
4. 用子代理并行处理每个方法文件以提高效率
5. 严格按AGENT.md规范验收结构
6. 处理完成后，更新 progress.md 中对应论文（从待处理表格中移除该行）
7. 自动 git add + git commit + git push 到 https://github.com/mingwcas/015.Spatial_transcriptome
8. 向我汇报每篇论文的处理结果

请开始处理。"

log "执行 DeepSeek headless..."

# 模型路由：settings.yaml 里 agent-default-model 指向的 provider 无密钥，
# 故复制一份 settings 并把默认模型改成有密钥的 xiaomi-token-plan-cn，
# 再用 --patch 让 headless 读取这份副本（不影响 GUI 的配置）。
# ponytail: 每次运行重新生成，避免副本过期；provider 密钥由 dsh 凭据库解析。
BATCH_SETTINGS=/tmp/dsh-batch-settings.yaml
BATCH_PATCH=/tmp/dsh-batch-model.patch.yml
python3 - "$HOME/.dsh/settings.yaml" "$BATCH_SETTINGS" <<'PY'
import sys
src, dst = sys.argv[1], sys.argv[2]
text = open(src).read()
old = "agent-default-model:\n  provider: deepseek-official\n  model: deepseek-flash\n  reasoningEffort: high"
if old not in text:
    # 已不是该组合，直接用原文件（用户可能已修好密钥）
    open(dst, "w").write(text)
    print("settings: passthrough (default model 非 deepseek-official)")
else:
    open(dst, "w").write(text.replace(
        old,
        "agent-default-model:\n  provider: xiaomi-token-plan-cn\n  model: mimo-v2.5-pro"))
    print("settings: 默认模型 -> xiaomi-token-plan-cn/mimo-v2.5-pro")
PY
printf -- "- id: settings\n  config:\n    path: %s\n" "$BATCH_SETTINGS" > "$BATCH_PATCH"

# 重试逻辑：API 超载时最多等 5 分钟再试
MAX_RETRIES=3
RETRY_DELAY=60
for attempt in $(seq 1 $MAX_RETRIES); do
    dsh --profile headless --patch "$BATCH_PATCH" "$TASK" 2>&1 | tee -a "$LOG_FILE"
    EXIT_CODE=${PIPESTATUS[0]}
    if [ $EXIT_CODE -eq 0 ]; then
        log "✅ 执行成功"
        break
    fi
    # 检查是否是 API 超载（退出码 1 且日志含 overload）
    if grep -q "overload\|PI_AI_ERROR" "$LOG_FILE" 2>/dev/null && [ $attempt -lt $MAX_RETRIES ]; then
        log "⚠️ API 超载，${RETRY_DELAY}s 后重试 ($attempt/$MAX_RETRIES)..."
        sleep $RETRY_DELAY
        RETRY_DELAY=$((RETRY_DELAY * 2))
    else
        log "⚠️ 执行退出码: $EXIT_CODE"
        break
    fi
done

rm -f "$pending_file"
log "======== 执行完成 $(date '+%Y-%m-%d %H:%M:%S') ========"

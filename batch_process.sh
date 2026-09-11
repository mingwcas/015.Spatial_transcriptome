#!/bin/bash
# batch_process.sh — 由 cron 驱动，每天北京时间 0:05 执行
# 依赖：dsh (DeepSeek Harness CLI), python3, git

set -e

PROJECT_DIR="/Users/mingwang/Documents/LabM/015.空间转录组"
LOG_FILE="$PROJECT_DIR/.batch_log"
cd "$PROJECT_DIR"

echo "======== $(date '+%Y-%m-%d %H:%M:%S') ========" >> "$LOG_FILE"

# 检查是否有待处理论文
pending=$(grep -c '⏳ 待处理' "09_生信分析/progress.md" 2>/dev/null || echo 0)
if [ "$pending" -eq 0 ]; then
    echo "✅ 所有论文已完成，退出" >> "$LOG_FILE"
    exit 0
fi

echo "待处理论文: $pending 篇" >> "$LOG_FILE"

# 读取前3篇待处理论文
papers=$(grep '⏳ 待处理' "09_生信分析/progress.md" | head -n 3)
echo "本轮处理:" >> "$LOG_FILE"
echo "$papers" >> "$LOG_FILE"

# 构建任务提示词
TASK="你是一个学术论文生信分析助手。请从 progress.md 读取待处理论文队列，按顺序处理前3篇。

每次处理一篇论文的步骤：
1. 读取 09_生信分析/AGENT.md 了解规范
2. 用 extract_pdf_metadata.py 提取 metadata → 01_metadata/
3. 用 pdf2md.py 转 PDF → /tmp/
4. 深度阅读 Markdown，写入 02_methods/（每个方法1个文件）、03_figures/（每张图1个文件）、04_reports/01_Bioinfo_Report_4D.md、05_pipeline_inventory/01_Code_Data_Inventory.md
5. 严格按 AGENT.md 规范验收结构
6. 用子代理并行处理以提高效率
7. 更新 progress.md 中对应论文的状态为 ✅ 完成
8. git add + git commit + git push
9. 完成后汇报结果

请开始执行。"

# 执行 DeepSeek headless
echo "开始执行 DeepSeek..." >> "$LOG_FILE"
echo "任务: $TASK" >> "$LOG_FILE"

dsh --profile headless "$TASK" 2>&1 | tee -a "$LOG_FILE"

EXIT_CODE=${PIPESTATUS[0]}
if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ 执行成功" >> "$LOG_FILE"
else
    echo "⚠️ 执行退出码: $EXIT_CODE" >> "$LOG_FILE"
fi

echo "======== 完成 $(date '+%Y-%m-%d %H:%M:%S') ========" >> "$LOG_FILE"

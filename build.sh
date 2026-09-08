#!/usr/bin/env bash
# 构建简历：Markdown -> HTML -> PDF
#
# 用法：
#   ./build.sh                     # src/resume.md -> index.html + resume.pdf
#   ./build.sh src/agent.md agent  # 变体 -> dist/agent.html + dist/agent.pdf
#
# 环境变量：
#   PYTHON   指定 Python 解释器（默认 python3），该解释器需已安装 markdown

set -euo pipefail
cd "$(dirname "$0")"

PYTHON="${PYTHON:-python3}"
exec "$PYTHON" scripts/build.py "$@"

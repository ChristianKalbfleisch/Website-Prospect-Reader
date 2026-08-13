#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

pip3 install --break-system-packages -r "$CLAUDE_PROJECT_DIR/requirements.txt"

apt update && apt install -y gh

#!/bin/bash
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Install for the interpreter that actually runs extract_pipeline.py.
# `pip3` on PATH resolves to a different Python than `python3` in this image
# (pip -> 3.13, python3 -> 3.11), so a bare `pip3 install` reports success
# while leaving openpyxl unimportable for the pipeline.
python3 -m pip install --break-system-packages -r "$CLAUDE_PROJECT_DIR/requirements.txt"

# Fail loudly if the install did not land where the pipeline will look.
python3 -c "import openpyxl" || {
  echo "session-start: openpyxl not importable under $(command -v python3) ($(python3 -V 2>&1))" >&2
  exit 1
}

apt update && apt install -y gh

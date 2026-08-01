#!/bin/bash
# Run this inside your cloned fde-journey repo folder
# Creates the full folder structure with .gitkeep placeholders so empty folders track in git

folders=(
  "week-01-expense-tracker"
  "week-02-api-cli-tool"
  "project-1-chat-utility-api"
  "project-2-dockerized-api"
  "project-3-cloud-ai-agent"
  "project-4-rag-assistant"
  "capstone-1-knowledge-base"
  "capstone-2-support-agent"
  "capstone-3-agentic-bedrock"
)

for f in "${folders[@]}"; do
  mkdir -p "$f"
  touch "$f/.gitkeep"
  cat > "$f/README.md" <<EOF
# ${f}

Status: not started

## Problem
_(what this project solves)_

## Architecture
_(brief description or diagram)_

## Tech stack
_(languages, frameworks, services used)_

## How to run
\`\`\`bash
# setup + run instructions
\`\`\`

## What I'd do differently
_(fill in once complete — this is your interview answer)_
EOF
done

cat > .gitignore <<'EOF'
__pycache__/
*.pyc
.env
venv/
.venv/
*.db
*.sqlite3
.DS_Store
node_modules/
*.egg-info/
.pytest_cache/
.mypy_cache/
EOF

echo "Folder structure created. Review, then:"
echo "  git add ."
echo "  git commit -m 'chore: scaffold repo structure'"
echo "  git push origin main"

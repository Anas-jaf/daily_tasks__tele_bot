#!/bin/bash
dir=$(pwd)

python "$dir/code_for_the_tasks/daily_dairy/utils.py" -f "daily_diary_document/مذكرات.docx"  -d

cd "$dir/daily_diary_document" && git add . &&  git commit -m "$(date +"%Y-%m-%d")" && git push

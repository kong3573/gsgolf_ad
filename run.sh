#!/bin/bash
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "광산골프 네이버 밴드 포스터 웹 뷰어 실행 중..."
python3 "${DIR}/server.py"

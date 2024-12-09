#!/bin/zsh

if [[ $1 -eq 26 ]]; then
    (cat <<EOF
4
17
31
35
49
EOF
) | python3 ./A26.py
fi

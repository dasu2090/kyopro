#!/bin/zsh

if [[ $1 -eq 36 ]]; then
    (cat <<EOF
5 10
EOF
) | python3 ./A36.py
fi

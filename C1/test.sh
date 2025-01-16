#!/bin/zsh

if [[ $1 -eq 5 ]]; then
    (cat <<EOF
3 6
EOF
) | python3 ./A05.py
    (cat <<EOF
3000 4000
EOF
) | python3 ./A05.py
fi

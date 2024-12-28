#!/bin/zsh

if [[ $1 -eq 36 ]]; then
    (cat <<EOF
5 10
EOF
) | python3 ./A36.py
fi

if [[ $1 -eq 37 ]]; then
    (cat <<EOF
2 3 100
10 20
1 2 3
EOF
) | python3 ./A37.py
fi

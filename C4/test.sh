#!/bin/zsh

if [[ $1 -eq 16 ]]; then
    (cat <<EOF
5
2 4 1 3
5 3 7
EOF
) | python3 ./A16.py
fi


if [[ $1 -eq 17 ]]; then
    (cat <<EOF
5
2 4 1 3
5 3 7
EOF
) | python3 ./A17.py
fi

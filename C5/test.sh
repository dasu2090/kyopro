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

if [[ $1 -eq 27 ]]; then
    (cat <<EOF
700 900
EOF
) | python3 ./A27.py
    (cat <<EOF
117 432
EOF
) | python3 ./A27.py
    (cat <<EOF
998244353 1000000000
EOF
) | python3 ./A27.py
fi

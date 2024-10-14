#!/bin/zsh

if [[ $1 -eq 11 ]]; then
    (cat <<EOF
15 47
11 13 17 19 23 29 31 37 41 43 47 53 59 61 67
EOF
) | python3 ./A11.py
echo ""
    (cat <<EOF
10 80
10 20 30 40 50 60 70 80 90 100
EOF
) | python3 ./A11.py
fi

if [[ $1 -eq 12 ]]; then
    (cat <<EOF
4 10
1 2 3 4
EOF
) | python3 ./A12.py
fi

if [[ $1 -eq 13 ]]; then
    (cat <<EOF
7 10
11 12 16 22 27 28 31
EOF
) | python3 ./A13.py
fi

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

if [[ $1 -eq 7 ]]; then
    (cat <<EOF
8
5
2 3
3 6
5 7
3 7
1 5
EOF
) | python3 ./A07.py
fi

if [[ $1 -eq 8 ]]; then
    (cat <<EOF
5 5
2 0 0 5 1
1 0 3 0 0
0 8 5 0 2
4 1 0 0 6
0 9 2 7 0
2
2 2 4 5
1 1 5 5
EOF
) | python3 ./A08.py
fi

if [[ $1 -eq 9 ]]; then
    (cat <<EOF
5 5 2
1 3 5 5
2 2 4 4
EOF
) | python3 ./A09.py
fi

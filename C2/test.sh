#!/bin/zsh

if [[ $1 -eq 6 ]]; then
    (cat <<EOF
15 4
62 65 41 13 20 11 18 44 53 12 18 17 14 10 39
4 13
3 10
2 15
1 2
EOF
) | python3 ./A06.py
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

if [[ $1 -eq 10 ]]; then
    (cat <<EOF
7
1 2 5 5 2 3 1
2
3 5
4 6
EOF
) | python3 ./A10.py
fi

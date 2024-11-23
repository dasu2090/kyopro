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
    (cat <<EOF
10
1 19 75 37 17 16 33 18 22
41 28 89 74 98 43 42 31
EOF
) | python3 ./A17.py
fi

if [[ $1 -eq 18 ]]; then
    (cat <<EOF
3 7
2 2 3
EOF
)| python3 ./A18.py
fi

if [[ $1 -eq 19 ]]; then
    (cat <<EOF
4 7
3 13
3 17
5 29
1 10
EOF
) | python3 ./A19.py
    (cat <<EOF
10 285
29 8000
43 11000
47 10000
51 13000
52 16000
66 14000
72 25000
79 18000
82 23000
86 27000
EOF
) | python3 ./A19.py
fi

if [[ $1 -eq 20 ]]; then
    (cat <<EOF
mynavi
monday
EOF
) | python3 ./A20.py
fi

if [[ $1 -eq 21 ]]; then
    (cat <<EOF
4
4 20
3 30
2 40
1 10
EOF
) | python3 ./A21.py
    (cat <<EOF
4
4 2
3 3
2 4
1 1
EOF
) | python3 ./A21.py
fi

if [[ $1 -eq 22 ]]; then
    (cat <<EOF
7
2 4 4 7 6 7
3 5 6 7 7 7
EOF
) | python3 ./A22.py
    (cat <<EOF
2
2
2
EOF
) | python3 ./A22.py
fi

if [[ $1 -eq 23 ]]; then
    (cat <<EOF
3 4
0 0 1
0 1 0
1 0 0
1 1 0
EOF
) | python3 ./A23.py
fi

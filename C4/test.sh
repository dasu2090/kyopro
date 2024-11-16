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

#!/bin/zsh

if [[ $1 -eq 26 ]]; then
    (cat <<EOF
5
2 4 1 3
5 3 7
EOF
) | python3 ./A26.py
fi


if [[ $1 -eq 27 ]]; then
    (cat <<EOF
5
2 4 1 3
5 3 7
EOF
) | python3 ./A27.py
fi

if [[ $1 -eq 28 ]]; then
    (cat <<EOF
3 7
2 2 3
EOF
)| python3 ./A28.py
fi

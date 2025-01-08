#!/bin/zsh

if [[ $1 -eq 51 ]]; then
    (cat <<EOF
5
1 futuremap
1 howtospeak
2
3
2
EOF
) | python3 ./A51.py
fi

if [[ $1 -eq 52 ]]; then
    (cat <<EOF
5
1 futuremap
1 howtospeak
2
3
2
EOF
) | python3 ./A52.py
fi

if [[ $1 -eq 53 ]]; then
    (cat <<EOF
3
1 2420
1 1650
2
EOF
) | python3 ./A53.py
fi

#!/bin/bash

IMAGE="/tmp/i3lock.png"

dunstctl set-paused true
scrot "${IMAGE}"
convert "${IMAGE}" -blur "15x15" "${IMAGE}"
i3lock -f -i "${IMAGE}" --nofork
dunstctl set-paused false

#!/bin/bash

IMAGE="/tmp/i3lock.png"
IS_DUNST_PAUSED="$(dunstctl is-paused)"

dunstctl set-paused true

ffmpeg -f x11grab -y -i "${DISPLAY}" -filter_complex "boxblur=5:1" -vframes 1 "${IMAGE}" -loglevel quiet

i3lock -f -i "${IMAGE}" --nofork

if [ "${IS_DUNST_PAUSED}" = "false" ]; then
    dunstctl set-paused false
fi

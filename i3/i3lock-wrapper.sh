#!/bin/bash

IMAGE="/tmp/i3lock.png"
IS_DUNST_PAUSED="$(dunstctl is-paused)"

dunstctl set-paused true

RES=$(xrandr | grep 'current' | sed -E 's/.*current\s([0-9]+)\sx\s([0-9]+).*/\1x\2/')
ffmpeg -f x11grab -video_size "${RES}" -y -i "${DISPLAY}" -filter_complex "boxblur=5:1" -vframes 1 "${IMAGE}" -loglevel quiet

i3lock -f -i "${IMAGE}" --nofork

if [ "${IS_DUNST_PAUSED}" = "false" ]; then
    dunstctl set-paused false
fi

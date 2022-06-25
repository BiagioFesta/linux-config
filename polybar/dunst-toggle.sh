#!/bin/bash

if [[ $(dunstctl is-paused) != 'false' ]]
then
    polybar-msg action '#dunst.hook.0'
else
    polybar-msg action '#dunst.hook.1]'
fi

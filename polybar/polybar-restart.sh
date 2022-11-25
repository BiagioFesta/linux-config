#/bin/bash

set -e

POLYBAR=$(which polybar)
POLYBAR_MSG=$(which polybar-msg)

set +e

# Quit polybar and wait termination
${POLYBAR_MSG} cmd quit
while pgrep -x polybar >/dev/null; do sleep 1; done

for d in $(xrandr --query | grep " connected" | cut -d" " -f1); do
    export MONITOR="${d}"

    if xrandr --query | grep "${d}" | grep -q "primary"; then
        export TRAY_POS="right"
    else
        export TRAY_POS="none"
    fi

    ${POLYBAR} 2>&1 | tee /tmp/polybar.log & disown
done

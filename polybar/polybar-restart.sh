#/bin/bash

set -e

POLYBAR=$(which polybar)
POLYBAR_MSG=$(which polybar-msg)

set +e

# Quit polybar and wait termination
${POLYBAR_MSG} cmd quit
while pgrep -x polybar >/dev/null; do sleep 1; done

${POLYBAR} 2>&1 | tee /tmp/polybar.log & disown

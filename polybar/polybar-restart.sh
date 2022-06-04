#/bin/bash

set -e

POLYBAR=$(which polybar)
POLYBAR_MSG=$(which polybar-msg)

set +e

${POLYBAR_MSG} cmd quit
${POLYBAR} 2>&1 | tee /tmp/polybar.log & disown

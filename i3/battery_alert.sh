#!/bin/bash

BATT_SYS="/sys/class/power_supply/BAT0"
ALERT_CAPACITY="15"

if [[ -d "${BATT_SYS}" ]]; then
    echo "battery_alert.sh: Battery found. Starting loop"

    while true; do
        status=$(cat "${BATT_SYS}/status")
        capacity=$(cat "${BATT_SYS}/capacity")

        if [[ "${status}" == "Discharging" && "${capacity}" -le ${ALERT_CAPACITY} ]]; then
            notify-send --urgency=critical \
                        --icon="battery" \
                        --expire-time=100000 \
                        "Low Battery" \
                        "Battery capacity less than ${ALERT_CAPACITY}%"
            sleep 100
        fi

        sleep 10
    done
else
    echo "battery_alert.sh: No battery found. Close script"
fi

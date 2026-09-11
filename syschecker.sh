#!/bin/bash

# Configuration: Refresh rate in seconds
REFRESH_RATE=2

get_cpu() {
    # Parses top to extract the idle percentage and subtracts from 100
    local cpu_idle=$(top -bn1 | grep "Cpu(s)" | awk '{print $8}')
    # Handles both dot and comma locales
    cpu_idle=${cpu_idle//,/.}
    local cpu_use=$(echo "100 - $cpu_idle" | bc)
    echo -e "CPU Utilization:  \e[1;32m$cpu_use%\e[0m"
}

get_memory() {
    # Extracts used and total memory using the 'free' utility
    free -m | awk 'NR==2{printf "Memory Usage:     \033[1;34m%.2f%%\033[0m (%sMB / %sMB)\n", $3*100/$2, $3, $2}'
}

get_disk() {
    # Extracts the disk usage percentage of the root directory (/)
    df -h / | awk 'NR==2{printf "Disk Usage (/):   \033[1;33m%s\033[0m occupied\n", $5}'
}

get_load() {
    # Fetches system load averages for 1, 5, and 15 minutes
    local load=$(uptime | awk -F'load average:' '{print $2}')
    echo -e "Load Average:    \033[1;36m$load\033[0m"
}

# Main loop for continuous monitoring
while true; do
    clear
    echo "========================================="
    echo "       LIVE LINUX SYSTEM MONITOR         "
    echo "========================================="
    echo "Timestamp: $(date '+%Y-%m-%d %H:%M:%S')"
    echo "----------------------------------------="

    get_cpu
    get_memory
    get_disk
    get_load

    echo "========================================="
    echo "Press [CTRL+C] to exit."

    sleep "$REFRESH_RATE"
done

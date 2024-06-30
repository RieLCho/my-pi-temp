#!/bin/bash
# Script: my-pi-temp.sh
cpu=$(</sys/class/thermal/thermal_zone0/temp)
gpu_temp=$(/usr/bin/vcgencmd measure_temp)
gpu_temp_clean=$(echo $gpu_temp | sed 's/temp=//')

timestamp=$(date +%s)
cpu_temp=$((cpu/1000))

json_data=$(echo "{\"timestamp\": $timestamp, \"cpu_temp\": $cpu_temp, \"gpu_temp\": ${gpu_temp_clean%\'C}}")

# 데이터 전송
curl -X POST -H "Content-Type: application/json" -d "$json_data" http://localhost:5000/log

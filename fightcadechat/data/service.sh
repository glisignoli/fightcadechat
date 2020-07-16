#!/bin/bash
cd /home/fc-chatbot/fightcadechat
source ./venv/bin/activate
while true; do timeout 1h fightcadechat; done
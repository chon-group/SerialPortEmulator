#! /bin/bash
if [ ! -f /usr/bin/xterm ]; then
    clear
    sudo apt update
    sudo apt install xterm
fi

xterm -e "cd pong; ./pong.sh" &
sleep 3
xterm  -e "cd ping; ./ping.sh" &


#! /bin/bash
if [ ! -f /usr/bin/xterm ]; then
    clear
    sudo apt update
    sudo apt install xterm
fi

sudo xterm -e "cd pong; ./pong.sh" &
sleep 3
sudo xterm -e "cd ping; ./ping.sh" &


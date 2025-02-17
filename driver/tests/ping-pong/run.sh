#! /bin/bash
if [ ! -f /usr/bin/xterm ]; then
    clear
    sudo apt update
    sudo apt install xterm -y
fi

sudo xterm -e "cd pong; ./pong.sh" &
sleep 5
sudo xterm -e "cd ping; ./ping.sh" &


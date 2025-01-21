#!/bin/bash

REPETIONS=$1

if [[ "$REPETIONS" == "" ]]; then
    REPETIONS=10
fi

cd /tmp

if [[ ! -d stress-tests_webots ]] && [[ ! -f stress-tests_webots/env-complete ]]; then

    mkdir stress-tests_webots

    cd stress-tests_webots

    repo="https://github.com/bptfreitas/FourWheels_With_ChonIDE_Webots"

    git clone $repo

    cd "FourWheels_With_ChonIDE_Webots/controllers/four_wheels_collision_avoidance"

    repo_javino="https://github.com/bptfreitas/JavinoCLibrary.git"

    git clone ${repo_javino}

    cd "JavinoCLibrary"

    make clean all-dbg

    cd ..

    pwd

    make WEBOTS_HOME="/usr/local/webots" all

    cd ..

    touch env-complete
fi

cd "/tmp/stress-tests_webots/FourWheels_With_ChonIDE_Webots/"

webots worlds/4_wheels_robot.wbt &

pid_webots=$!

echo "PID webots: $pid_webots"

sleep 20

cd SMA

# killing any instance of JasonEmbedded or Java before starting
killall -u `whoami` jasonEmbedded
killall -u `whoami` java 

for rep in $( seq 10 ); do 

    clear

    echo "########################"
    echo "Webots Stress test $rep"
    echo "########################"

    sudo dmesg -C 

    jasonEmbedded webotsExample.mas2j &

    pid_je=$!

    echo "PID Jason Embedded: $pid_je"

    sleep 30

    killall -u `whoami` jasonEmbedded
    killall -u `whoami` java 

    sudo dmesg -T > /tmp/stress-tests_webots/stress-test_webots${rep}.log

    sleep 5

done
#!/bin/bash

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

    make clean all

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

for rep in $( seq 2 ); do 

    echo "########################"
    echo "Webots Stress test $rep"
    echo "########################"

    jasonEmbedded webotsExample.mas2j &

    pid_je=$!

    echo "PID Jason Embedded: $pid_je"

    sleep 30

    kill -9 $pid_je `ps | grep java | cut -f2 -d" "`

    sleep 5

done
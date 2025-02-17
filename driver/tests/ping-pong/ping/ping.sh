#! /bin/bash
if [ ! -f ./pythonENV/bin/python3 ]; then
    clear
    sudo apt update
    sudo apt install xterm python3 python3-pip -y
    python3 -m venv pythonENV
    source pythonENV/bin/activate
    pip install --upgrade pip
    wget --content-disposition https://packages.chon.group/python/javino/
    pip install javino*.whl
    rm javino*whl
fi

source pythonENV/bin/activate
./pythonENV/bin/python3 ping.py


#!/bin/sh
# Prerequisite for bluetooth
# Author     : Anjana Rajan
# Last update: 17-7-2017
#
# usage      : $ ./prerequisite.sh
######################################

echo -----------------------------------------------------
echo [*] Installing Prerequisites- Bluetooth
#echo "[!] usage ./prerequisite.sh"
echo -----------------------------------------------------
sudo apt-get update
sudo apt-get install python-bluez
sudo apt-get install libbluetooth-dev
sudo apt-get install libopenobex1-dev
sudo apt-get install python-pip python-dev ipython
sudo apt-get install bluetooth libbluetooth-dev
sudo pip install pybluez
sudo apt-get install obexpushd
sudo apt-get install python-lightblue
cd lightblue-0.4/
sudo python setup.py install
sudo hciconfig hci0 up
sudo service bluetooth start
echo ""
echo -----------------------------------------------------
echo [*] Finished installation
echo -----------------------------------------------------

#!/bin/bash
# Testcases  : Ubertooth
# Author     : Anjana Rajan
# Last update: 27-7-2017
# Platform   : 4.3.0-kali1-amd64
# usage      : $ ./runtest.sh
######################################

echo -----------------------------------------------------
echo [*] Testcases- Ubertooth
echo -----------------------------------------------------

echo "Sniff Bluetooth LE Packets"
echo "Starting Bluetooth Services"
service bluetooth start && hcitool dev && hcitool scan
op='Please enter your choice: '
options=("Ubertooth-scan" "Capture and convert to pcap" "View in Wireshark" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "Ubertooth-scan")
	    ubertooth-scan -b hcil -t 40 -x
            ;;
        "Capture and convert to pcap")
            ubertooth-btle -p -c /tmp/capture.pcap
            ;;
	"View in Wireshark")
	    wireshark /tmp/capture.pcap
	    ;;
        "Quit")
            break
            ;;
        *) echo invalid option;;
    esac
done

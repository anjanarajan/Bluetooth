#**********************************************************************************************
#!/usr/bin/python
# file: impersonation.py
# auth: Anjana Rajan_created-on - 10-06-2017
# desc: simple program to impersonate a device with bluetooth addres, Name & class of the device
#**********************************************************************************************
import bluetooth
import os
import time
import sys
import getpass
import subprocess
from subprocess import Popen, PIPE, STDOUT
import time
import pexpect
import subprocess
import sys
#from sh import bluetoothctl
device_name = None
im_devce_addr = None
######################################################################
# Function 1
#####################################################################
def discover():
	nearby_devices = bluetooth.discover_devices(lookup_names=True)
	print "Found %d devices" % len(nearby_devices)
	for addr, name in nearby_devices:
    		print " %s - %s" % (addr, name)
######################################################################
# Function 2
#####################################################################
def spec():
	cmd1 = 'hcitool scan'
	cmd2 = 'hcitool inq'
	final = Popen("{}; {}".format(cmd1, cmd2), shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
	output = final.stdout.read()
	print output
######################################################################
# Function 3
#####################################################################
def impersonate(device_name,device_class,bdaddr):	
	command1 = 'hciconfig hci0 name ' + device_name + ' class ' + device_class
	command3 = '/home/csti-laptop/Desktop/anjana/bdaddr -i hci0 -r -t ' + bdaddr
#############################################################################################################################################
#For by passing root permission
#############################################################################################################################################
	'''r_cmd1 = 'sudo ' + '-S ' + command1
	r_cmd2 = 'sudo' + ' -S ' + command2
	r_cmd3 = 'sudo' + ' -S ' + command3
	print r_cmd1
	passw = getpass.getpass('Enter root password:',stream=None)
	sp = subprocess.Popen(command1, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,shell=True)
	out, err = sp.communicate(passw +'\n')
	sp1 = subprocess.Popen(command2, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,shell=True)
	out, err = sp1.communicate(passw +'\n')
	sp2 = subprocess.Popen(command3, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True,shell=True)
	out, err = sp2.communicate(passw +'\n')
	'''
#Run the script with sudo
	os.system(command3)
	time.sleep(2)
	op=os.system(command1)
	time.sleep(2)
	if (op !=1):
		os.system('sudo hciconfig hci0 up')
		os.system(command1)
##################################################################################################################################################
# Main Function
##################################################################################################################################################
if __name__ == '__main__':
	#print sys.path
	discover()
	spec()
	op=raw_input("Do You Want to continue the scanning process : Y/N :")
	while op=='Y':
		discover()
		spec()
		op=raw_input("Do You Want to continue the scanning process : Y/N :")
	device_name = raw_input("Enter the device name to impersonate : ")
	device_class = raw_input("Enter the device class : ")
	bdaddr = raw_input("Enter the bdaddr : ")
	impersonate(device_name,device_class,bdaddr)
	



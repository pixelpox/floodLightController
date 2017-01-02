from bluetooth import *
import RPi.GPIO as GPIO
from time import *
import datetime


interestingDeviceAddress = "0C:FC:83:F8:98:DD"
otherDeviceAddress = "E4:32:CB:6B:56:68"

def setupLED():
	pinzero = 17
	GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	GPIO.setup(pinzero,GPIO.OUT)

def turnLEDOn():
	print "turning LED on"
	pinzero = 17
	GPIO.output(pinzero,GPIO.HIGH)
	
def turnLEDOff():
	print "turning LED off"
	pinzero = 17
	GPIO.output(pinzero,GPIO.LOW)



setupLED()

while True:
	datetime.datetime.time(datetime.datetime.now())
	print strftime("%H:%M:%S", gmtime())
	print "performing inquiry..."

	nearby_devices = discover_devices(lookup_names = True)

	if len(nearby_devices) != 0:
		#found some devices
		#print "found %d devices" % len(nearby_devices)
		
		for deviceAddress, deviceName in nearby_devices:
			print "deviceAddress: %s" % (deviceAddress)
			print " %s - %s" % (deviceName, deviceAddress)
			
			if deviceAddress.upper() == interestingDeviceAddress.upper():
				print "FOUND THE DEVICE TURN THE LIGHT ON"
				turnLEDOn()
			else:
				print "DOING NOTHING"
				turnLEDOff()
	else:
		#didnt find any devices
		print "DOING NOTHING"
		turnLEDOff()
		
time.sleep(5)

	



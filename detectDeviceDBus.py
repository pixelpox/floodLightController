import dbus
from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import RPi.GPIO as GPIO

def property_changed(interface, changed, invalidated, path):
	iface = interface[interface.rfind(".") + 1:]
	for name, value in changed.iteritems():
		val = str(value)
		print("{%s.PropertyChanged} [%s] %s = %s" % (iface, path, name,val))
		if objectPath == path and name == "Connected":
			print "hey!, thats my device"
			
			if val == "1":
				#turn light on
				print "turn light on"
				turnLEDOn()
				
			if val == "0":
				#turn light off
				print "turn light off"
				turnLEDOff()

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

DBusGMainLoop(set_as_default=True)

programName = 'org.bluez'
objectPath = '/org/bluez/hci0/dev_0C_FC_83_F8_98_DD'
interfaceName = 'org.freedesktop.DBus.Properties'

setupLED()
bus = dbus.SystemBus()
bus.add_signal_receiver(property_changed, bus_name="org.bluez",
			dbus_interface="org.freedesktop.DBus.Properties",
			signal_name="PropertiesChanged",
			path_keyword="path")
			

loop = GLib.MainLoop()
loop.run()

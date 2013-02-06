import serial
from polls.models import Party
from django.shortcuts import render_to_response, get_object_or_404
p = get_object_or_404(Party,pk=1)

ser = serial.Serial('/dev/ttyUSB0', 9600)
x = ser.read()
#print (x)
# read one byte
s = ser.read(10)
#print (s)
# read up to ten bytes (timeout)
while True:
	line = ser.readline()
	#print (line)
	if line == "J1-1\n":
		print ("Joueur 1 a clique")
		p.checked = 1
		p.save()
		while line == "J1-1\n":
			line = ser.readline()
			
# read a '\n' terminated line
ser.close()


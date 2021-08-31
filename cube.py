# -*- coding: utf-8 -*-

import RPi.GPIO as IO 	#calling for header file which helps in using GPIO pins
import time as tm 		#calling for time to provide delays in program
import random as rd		#used for generating random numbers
IO.setwarnings(False)	#does not show any warnings
import os				#importing system functions to python

#contains the basic setup instructions, here the values are the pin numbers
neg = [18,23,24,25, 10,9,11,8, 19,16,20,21, 12,7,2,3]
pos = [4,17,27,22, 5,6,13,26]

IO.setmode (IO.BCM) #calling the pins according to the bcm numbering

#IO.setup(14, IO.IN, pull_up_down=IO.PUD_UP)  #button pins, connects GND and bcm pin 14

for i in range (8): #initilizating the positive pins
	IO.setup(pos[i],IO.OUT)

for i in range (16): #initilizating the negative pins
	IO.setup(neg[i],IO.OUT)


def noff(): #sets all negative pins to 1(disables output)
	for z in range (16):
	    IO.output(neg[z],1)


def pin_off(): #this function sets all the output signals to 0
	for i in range(16):
		IO.output(neg[i],0) 

	for i in range(8):
		IO.output(pos[i],0)

	return;

def single(): #lights up one led at a time
	noff()

	for i in range (8):
		IO.output(pos[i],1)
		for j in range (16):
			IO.output(neg[j],0)
			tm.sleep(.05)
			IO.output(neg[j],1)
		IO.output(pos[i],0)
	pin_off()
	return;

def random(): #turns on random leds
	pin_off()

	a=[]
	b=[]

	for i in range(100):
		a.append(rd.randint(0, 15))
		b.append(rd.randint(0, 7))

	for i in range(2):
		t=i*0.05		#the amount of time for each break in seconds, the time keeps increasing as the number of times the cycle is executed

		for j in range(98):
			for k in range(3):
				IO.output(pos[b[j+k]],1)	
				IO.output(neg[a[j+k]],0)
			tm.sleep(t) #pause time 
			for k in range(3):
				IO.output(pos[b[j+k]],0)	
				IO.output(neg[a[j+k]],1)
	return;

def boxes():
	pin_off()
	noff()
	a=[0,4,5,1]
	b=[10,14,15,11]
	c=[2,6,7,3]
	d=[8,12,13,9]

	for x in range(5):
		for i in range(8):
			IO.output(pos[i],1)
			if i>=3:
				for j in range(4):
					IO.output(neg[a[j]],0)
					IO.output(neg[b[j]],0)
					IO.output(neg[c[j]],0)
					IO.output(neg[d[j]],0)
					tm.sleep(.1)
					IO.output(neg[a[j]],1)
					IO.output(neg[b[j]],1)
					IO.output(neg[c[j]],1)
					IO.output(neg[d[j]],1)
				IO.output(pos[i-4],0)

	return;

def spiral(): #creates a spiral transition
	tin = [18,23,24,25,8,21,3,2,7,12,19,10,9,11,20,16] #spiral inwards
	tout = [16,20,11,9,10,19,12,7,2,3,21,8,25,24,23,18] #spiral outwards
	pin_off()

	noff()	
	for i in range (4):
		for j in range(4):
			IO.output(pos[j],0)
			IO.output(pos[j+4],1)

		for j in range(16):
			IO.output(tin[j],0)
			tm.sleep(.08)
		
		for j in range(16):
			IO.output(tout[j],1)
			tm.sleep(.08)

		#reversing
		for j in range(4):
			IO.output(pos[j+4],0)
			IO.output(pos[j],1)
		
		for j in range(16):
			IO.output(tout[j],0)
			tm.sleep(.08)

		for j in range(16):
			IO.output(tin[j],1)
			tm.sleep(.08)

	return;

def alternate(): #lights up a alternate leds in a single row
	pin_off()
	noff()
	a=[0,5,10,15,2,7,8,13]
	b=[1,4,3,6,11,14,9,12]

	for l in range(4):
		for j in range(8):
			IO.output(pos[j],1)
			for i in range(8):
				IO.output(neg[a[i]],1)
				IO.output(neg[b[i]],0)
			tm.sleep(.2)
			for i in range(8):
				IO.output(neg[a[i]],0)
				IO.output(neg[b[i]],1)
			tm.sleep(.2)
			IO.output(pos[j],0)

	return;

def zigzag():			#need to add trail
	a=[0,5,8,13,12,9,4,1]
	b=[3,6,11,14,15,10,7,2]
	pin_off()
	noff()

	for x in range(4):
		for i in range(4):
			IO.output(pos[i+4],1)

			for j in range(4):
				IO.output(neg[a[j]],0)
				IO.output(neg[b[j]],0)
				tm.sleep(.15)
				
			for j in range(4):
				IO.output(neg[a[j]],1)
				IO.output(neg[b[j]],1)
				tm.sleep(.15)

			for j in range(4):
				IO.output(neg[a[j+4]],0)
				IO.output(neg[b[j+4]],0)
				tm.sleep(.15)

			for j in range(4):
				IO.output(neg[a[j+4]],1)
				IO.output(neg[b[j+4]],1)
				tm.sleep(.15)
				
			IO.output(pos[i+4],0)

def circle():
	a=[0, 1, 2, 3, 7, 11]
	b=[15,14,13,12,8,4,10,9]
	x=[0,1,2,3,4,5,6,7,0,1,2,3]
	pin_off()
	noff()
	for s in range(4):
		for i in range(8):
			IO.output(pos[x[i]],1)
			IO.output(pos[x[i+2]],1)
			t=s*0.05
			for k in range(4):
				for j in range(6):
					IO.output(neg[a[j]],0)
					IO.output(neg[b[j]],0)
					tm.sleep(t)
					IO.output(neg[a[j]],1)
					IO.output(neg[b[j]],1)
			IO.output(pos[x[i]],0)
			IO.output(pos[x[i+2]],0)

	return;

def ripples(): #ripple effect
	pin_off()
	noff()

	tl=[0, 4,5,1, 8,9,10,6,2, 12,13,14,15,11,7,3]
	tr=[3, 2,6,7, 11,10,9,5,1, 0,4,8,12,13,14,15]
	bl=[12, 8,9,13, 14,10,6,5,4, 0,1,2,3,7,11,15]
	br=[15, 14,10,11, 13,9,5,6,7, 3,2,1,0,4,8,12]

	for i in range(4):
		IO.output(pos[i+4],1)
	for x in range(4):
		for i in range(8):
			if i == 0 or i== 4:
				side=tl
			elif i == 1 or i == 5:
				side=bl
			elif i == 2 or i == 6:
				side=br
			else :
				side=tr

			for k in range(1):
				IO.output(neg[side[k]],0)
			tm.sleep(.2)
			for k in range(1):
				IO.output(neg[side[k]],1)
			for k in range(1,4):
				IO.output(neg[side[k]],0)
			tm.sleep(.2)
			for k in range(1,4):
				IO.output(neg[side[k]],1)
			for k in range(4,9):
				IO.output(neg[side[k]],0)
			tm.sleep(.2)
			for k in range(4,9):
				IO.output(neg[side[k]],1)
			for k in range(9,16):
				IO.output(neg[side[k]],0)
			tm.sleep(.2)
			for k in range(9,16):
				IO.output(neg[side[k]],1)
	return;

def tracking(): 
	noff()
	v=[[0,4,8,12],[1,5,9,13],[2,6,10,14],[3,7,11,15]]
	h=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]

	for x in range(4):
		IO.output(pos[x+4],1)

	for z in range(5):
		for x in range(4):
			for y in range(4):
				IO.output(neg[h[x][y]],0)
				IO.output(neg[v[x][y]],0)

			tm.sleep(.2)

			for y in range(4):
				IO.output(neg[h[x][y]],1)
				IO.output(neg[v[x][y]],1)

		for x in range(3,0,-1):
			for y in range(3,0,-1):
				IO.output(neg[h[x][y]],0)
				IO.output(neg[v[x][y]],0)

			tm.sleep(.2)

			for y in range(3,0,-1):
				IO.output(neg[h[x][y]],1)
				IO.output(neg[v[x][y]],1)

	for x in range(4):
		IO.output(pos[x],0)

	return;

def pattern1():
	a=[5,1,0,4,8,12,13,9]
	b=[10,14,15,11,7,3,2,6]

	pin_off()
	noff()

	for x in range(6):
		for i in range(2):
			IO.output(pos[i+4],1)
			IO.output(pos[i+6],1)

			for j in range(8):
				IO.output(neg[a[j]],0)
				IO.output(neg[b[j]],0)
				tm.sleep(.1)

			for j in range(8):
				IO.output(neg[a[j]],1)
				IO.output(neg[b[j]],1)
				tm.sleep(.2)


			IO.output(pos[i+4],0)
			IO.output(pos[i+6],0)
	return;



#executing
def main():

	noff()
	print("LED test")
#	single() #testing

	patterns = [ random , pattern1 , spiral , alternate , ripples , zigzag , circle , boxes , ]
	while True:
		for f in patterns:
			os.system('clear')	#clears the screen
			print("Note:Press 'Ctrl'+'C' to exit\n")
			print("Current pattern: ",patterns[f])
			patterns[f]()

		os.system('clear')	#clears the screen

		print("Note:Press 'Ctrl'+'C' to exit\n")
		print("Current pattern: Random") #displays the current running 
		random()
		os.system('clear')

		print("Note:Press 'Ctrl'+'C' to exit\n")
		print("Current pattern: Boxes")
		boxes()
		os.system('clear')

		print("Note:Press 'Ctrl'+'C' to exit\n")
		print("Current pattern: Spiral")
		spiral()
		os.system('clear')

		print("Note:Press 'Ctrl'+'C' to exit\n")
		print("Current pattern: Alternate")
		alternate()
		os.system('clear')

		print("Note:Press 'Ctrl'+'C' to exit\n")
		print("Current pattern: Zigzag")
		zigzag()
		os.system('clear')

		print("Note:Press 'Ctrl'+'C' to exit\n")
		print("Current pattern: Circle")
		circle()
		os.system('clear')

		print("Note:Press 'Ctrl'+'C' to exit\n")
		print("Current pattern: Ripples")
		ripples()
		os.system('clear')

		print("Note:Press 'Ctrl'+'C' to exit\n")
		print("Current pattern: Tracking")
		tracking()
		os.system('clear')

		print("Note:Press 'Ctrl'+'C' to exit\n")
		print("Current pattern: ")
		pattern1()
		os.system('clear')

#		print("Note:Press 'Ctrl'+'C' to exit\n")
#		print("Current pattern: ")
#		()
#		os.system('clear')


	return;


if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print("Goodbye!")
		noff()
		pin_off()
		IO.cleanup()
	IO.cleanup()


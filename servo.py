#-*- coding: utf-8 -*-
#Import classes, functions, variables, from "mdev" files
from mDev import *
mdev = mDEV() #create object

#The servo2 rotates back and forth between 40 and 140 degrees 
while True:
	for i in range(40,140,1):
		mdev.setServo('2',i)
		time.sleep(0.005)
	for i in range(140,40,-1):
		mdev.setServo('2',i)
		time.sleep(0.005)

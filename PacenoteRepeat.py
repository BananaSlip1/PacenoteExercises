# -----------------------------------------#
# Library Imports   					   #
# -----------------------------------------#
from playsound import playsound
from random import randrange
from threading import Timer
from collections import deque
from inputimeout import inputimeout
import time
# -----------------------------------------#-----------------------------------------#


# HOW TO USE PLAYSOUND (MP3)
## playsound("Audio/4rightHug.mp3")
## Path for audio files: C:\Users\thoma\source\repos\RallyNback\Audio

# -----------------------------------------#
# Global Variables  					   #
# -----------------------------------------#
nValue = 1
aQueue = deque()
iValueList = deque()
corrects = 0
incorrects = 1
inTime_limit = 3
count = 0
x = True
y = True

# -----------------------------------------#-----------------------------------------#

# -----------------------------------------#
# Menu Functions     					   #
# -----------------------------------------#
# MENU to return to
def main():
	global nValue
	global inTime_limit
	global y
	global corrects
	global incorrects
	global count

	# Session values and settings
	while y:
		print("N is set to:", nValue)
		#print("T is set to:", inTime_limit)
		print("\nTotal correct this session:", corrects)
		print("Total incorrect this session:", incorrects - 1)
		print("Total rounds:", count)

		selection = input("\nWhat do you want to do?\n\n(S)tart\nChange (N)\n(C)lear score\n(Q)uit\n\n")
		if (selection == "s" or selection == "S"):
			start()
		elif (selection == "n" or selection == "N"):
			nValue = int(input("\nSet N to: "))
			clear()
		elif (selection == "c" or selection =="C"):
			corrects = 0
			incorrects = 1
			count = 0
		#elif (selection == "t" or selection == "T"):
		#	inTime_limit = int(input("\nSet Time Limit to:"))
		#	clear()
		elif (selection == "q" or selection == "Q"):
			y = False
	quit()

# Quit function
def quit():
	print("\nGoodbye")
# -----------------------------------------#-----------------------------------------#

# -----------------------------------------#
# Random Num Generator 					   #
# -----------------------------------------#
# Generates Random number between 1 and 18
def rando():
	return randrange(1, 19)
# -----------------------------------------#-----------------------------------------#


# -----------------------------------------#
# To/From Sound/Input					   #
# -----------------------------------------#
# Takes the random value and plays the appropriate audio byte
# Currently limited to 1-6 L/R and Flat, Square, Hairpin L/R
def valToSound(rValue):
	print("ValToSound")
	if (rValue == 1):
		#print("1")
		playsound("Audio/1L.mp3")
	elif (rValue == 2):
		#print("2")
		playsound("Audio/2L.mp3")
	elif (rValue == 3):
		#print("3")
		playsound("Audio/3L.mp3")
	elif (rValue == 4):
		playsound("Audio/4L.mp3")
	elif (rValue == 5):
		playsound("Audio/5L.mp3")
	elif (rValue == 6):
		playsound("Audio/6L.mp3")
	elif (rValue == 7):
		playsound("Audio/1R.mp3")
	elif (rValue == 8):
		playsound("Audio/2R.mp3")
	elif (rValue == 9):
		playsound("Audio/3R.mp3")
	elif (rValue == 10):
		playsound("Audio/4R.mp3")
	elif (rValue == 11):
		playsound("Audio/5R.mp3")
	elif (rValue == 12):
		playsound("Audio/6R.mp3")
	elif (rValue == 13):
		playsound("Audio/FL.mp3")
	elif (rValue == 14):
		playsound("Audio/SL.mp3")
	elif (rValue == 15):
		playsound("Audio/HL.mp3")
	elif (rValue == 16):
		playsound("Audio/FR.mp3")
	elif (rValue == 17):
		playsound("Audio/SR.mp3")
	elif (rValue == 18):
		playsound("Audio/HR.mp3") # Random number to audio byte read

def soundToVal(iValue):
	if (iValue == "1l" or iValue == "1L"):
		return 1
	elif (iValue == "2l" or iValue == "2L"):
		return 2
	elif (iValue == "3l" or iValue == "3L"):
		return 3
	elif (iValue == "4l" or iValue == "4L"):
		return 4
	elif (iValue == "5l" or iValue == "5L"):
		return 5
	elif (iValue == "6l" or iValue == "6L"):
		return 6
	elif (iValue == "1r" or iValue == "1R"):
		return 7
	elif (iValue == "2r" or iValue == "2R"):
		return 8
	elif (iValue == "3r" or iValue == "3R"):
		return 9
	elif (iValue == "4r" or iValue == "4R"):
		return 10
	elif (iValue == "5r" or iValue == "5R"):
		return 11
	elif (iValue == "6r" or iValue == "6R"):
		return 12
	elif (iValue == "fl" or iValue == "FL"):
		return 13
	elif (iValue == "sl" or iValue == "SL"):
		return 14
	elif (iValue == "hl" or iValue == "HL"):
		return 15
	elif (iValue == "fr" or iValue == "FR"):
		return 16
	elif (iValue == "sr" or iValue == "SR"):
		return 17
	elif (iValue == "hr" or iValue == "HR"):
		return 18 # String to Number
# -----------------------------------------#-----------------------------------------#


# -----------------------------------------#
# Queue Functions   					   #
# -----------------------------------------#
# Queue maker for rValues (aQueue)
def aQueUpd(rValue):
	global aQueue
	#print("aQueueTop", aQueue)
	if (len(aQueue) > nValue - 1):
		aQueue.popleft()
		aQueue.append(rValue)
		#print("aQueuePop", aQueue)
	else:
		aQueue.append(rValue)
		#print("aQueueAmm", aQueue)

# Queue maker for iValues (bQueue)
def iVList(iValue):
	global iValueList
	global x
	iValueList = deque(list(iValue.split(" ")))
	#print("Split:", iValueList)
	for i in iValueList:
		if (i == "q"):
			x = False
			return
	for i in iValueList:
		#print(soundToVal(i))
		#print("i:", i)
		iInd = iValueList.index(i)
		#print("iInd:", iInd)
		iValueList[iInd] = soundToVal(i)
		#print("Num:", iValueList)

# Compares aQueue and bQueue
def queComp():
	if (aQueue == iValueList):
		return True
	else:
		return False
# -----------------------------------------#-----------------------------------------#

# -----------------------------------------#
# Game functions    					   #
# -----------------------------------------#
# Present question, update queue, and handle answer
def start():
	global x
	x = True
	nQuest()
	return

# Prompt and call other functions, handle queues
def nQuest():
	global count
	global x
	global inTime_limit
	global nValue
	while x:
		count += 1/nValue
		rValue = rando() # gen random pacenote value
		valToSound(rValue)
		aQueUpd(rValue)
		iValue = input()
		iVList(iValue)
		if (queComp()):
			correct()
		elif (not queComp()):
			wrong()
	return
# -----------------------------------------#-----------------------------------------#
# -----------------------------------------#
# Clearer								   #
# -----------------------------------------#
def clear():
	print("\n" * 20)

# -----------------------------------------#
# Right/Wrong handlers 					   #
# -----------------------------------------#
def correct():
	global corrects
	print("correct:", corrects + 1)
	corrects += 1
	clear()

def wrong():
	global incorrects
	print("wrong:", incorrects)
	incorrects += 1
	clear()

#-----------------------------------#
#-----------------------------------#

main()

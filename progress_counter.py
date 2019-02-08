#!/usr/bin/env python3

#for get any key
import msvcrt as msvcrt

#for sleep commmand
#import sleep instead of whole time for lazy awesomeness
from time import sleep

def readanykey():
    #get character, remember ANSI C shiet right?
    msvcrt.getch()

def progress_counter():
    progress = 0
    while progress <= 100:
        print("Progress.. " + str(progress) + "%\r", end="", flush = True)
        #wait 0.1 seconds
        sleep(0.1)
        #you can also type progress += 1 it does same thing
        progress = progress + 1      
    print("Done. Press Any Key:")
    readanykey()

#this will start all other functions inside this file
#this is made so that you can import this file to some other files
#don't think too much just put this in here or google it
if __name__ == "__main__":
    progress_counter()
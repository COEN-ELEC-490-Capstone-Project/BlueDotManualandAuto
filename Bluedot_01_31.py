#This document is an untested approach to controlling the motors of the vehicle through manual means as well as automatic means.

import RPi.GPIO as GPIO
from bluedot import BlueDot
from signal import pause
import time
from io import BytesIO
from picamera import PiCamera

#set GPIO numbering mode and define output pins
#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(7,GPIO.OUT)
#GPIO.setup(11,GPIO.OUT)
#GPIO.setup(13,GPIO.OUT)
#GPIO.setup(15,GPIO.OUT)

#MANUAL OPERATIONS

class RobotControls:
    def __init__(self):
        self.GPIO.setmode(GPIO.BOARD)
        self.GPIO.setup(7, GPIO.OUT)
        self.GPIO.setup(11, GPIO.OUT)
        self.GPIO.setup(13, GPIO.OUT)
        self.GPIO.setup(15, GPIO.OUT)

    def up(self):
        print('Top')
        self.GPIO.output(7, False)
        self.GPIO.output(11, True)
        self.GPIO.output(13, False)
        self.GPIO.output(15, True)


    def down(self):
        print('Bottom')
        self.GPIO.output(7, True)
        self.GPIO.output(11, False)
        self.GPIO.output(13, True)
        self.GPIO.output(15, False)


    def right(self):
        print('Right')
        self.GPIO.output(7, True)
        self.GPIO.output(11, False)
        self.GPIO.output(13, False)
        self.GPIO.output(15, True)


    def left(self):
        print('Left')
        self.GPIO.output(7, False)
        self.GPIO.output(11, True)
        self.GPIO.output(13, True)
        self.GPIO.output(15, False)


    #Act as a turn off
    def middle(self):
        print('Stop')
        self.GPIO.output(7, False)
        self.GPIO.output(11, False)
        self.GPIO.output(13, False)
        self.GPIO.output(15, False)


#AUTO OPERATIONS Drive forward 2 seconds and stop

    def auto(self):
        print('Top')
        self.GPIO.output(7, False)
        self.GPIO.output(11, True)
        self.GPIO.output(13, False)
        self.GPIO.output(15, True)

        time.sleep(2)
        print('Stop')
        self.GPIO.output(7, False)
        self.GPIO.output(11, False)
        self.GPIO.output(13, False)
        self.GPIO.output(15, False)
		
#Buttons Layout and Responses to when pressed		

bd = BlueDot(row=5, cols=3)
bd.color = "blue"
bd.square = True

bd[0,1].visible = False
bd[1,0].visible = False
bd[1,2].visible = False
bd[3,0].visible = False
bd[3,2].visible = False
bd[2,3].visible = False
bd[4,0].visible = False
bd[4,1].visible = False
bd[4,2].visible = False

bd[0,0].color = "green"
bd[0,2].color = "red"

#MANUAL CONTROLS
bd[0,0].when_pressed = record
bd[1,1].when_pressed = up
bd[2,0].when_pressed = left
bd[2,2].when_pressed = right
bd[3,1].when_pressed = down
bd[2,1].when_pressed = middle

#AUTOMATICALLY MOVE 2 METERS AND STOP 
bd[0,2].when_pressed = auto
bd[0,2].when_moved = auto
bd[0,2].when_double_pressed = toggle

#GPIO.cleanup()
pause()

#This document is an untested approach to controlling the motors of the vehicle through manual means as well as automatic means.

import RPi.GPIO as GPIO
from bluedot import BlueDot
from signal import pause

import time

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

#MANUAL OPERATIONS

            def up():
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
		print('Top')

            def down():
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,True)
                GPIO.output(15,False)
		print('Bottom')

            def right():
                GPIO.output(7,True)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,True)
		print('Right')

            def left():
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,True)
                GPIO.output(15,False)
		print('Left')

#Act as a turn off
            def middle():
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
		print('Stop')
          
#AUTO OPERATIONS Drive forward 2 seconds and stop

            def auto():
                GPIO.output(7,False)
                GPIO.output(11,True)
                GPIO.output(13,False)
                GPIO.output(15,True)
		print('Top')
  		time.sleep(2)
                GPIO.output(7,False)
                GPIO.output(11,False)
                GPIO.output(13,False)
                GPIO.output(15,False)
		print('Stop')

bd = BlueDot(cols=3, row=5)
bd.color = "blue"
bd.square = True

bd[0,0].visible = False
bd[2,0].visible = False
bd[0,2].visible = False
bd[2,2].visible = False
bd[3,0].visible = False
bd[4,0].visible = False
bd[3,2].visible = False
bd[4,2].visible = False

bd[1,1].color = "red"
bd[4,1].circle = True
bd[4,1].color = "green"

#MANUAL CONTROLS
bd[1,0].when_pressed = up
bd[1,2].when_pressed = down
bd[0,1].when_pressed = left
bd[2,1].when_pressed = right
bd[1,1].when_pressed = middle

#AUTOMATICALLY MOVE 2 METERS AND STOP 
bd[4,1].when_pressed = auto
bd[4,1].when_moved = auto

GPIO.cleanup()
pause()
    

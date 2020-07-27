from gpiozero import PWMLED, Button
import time

greenLed = PWMLED("BOARD33")
yellowLed = PWMLED("BOARD35")
redLed = PWMLED("BOARD37")

greenButton = Button("BOARD36")
yellowButton = Button("BOARD38")
redButton = Button("BOARD40", hold_time=5)

def greenLedPressed():
    yellowLed.off()
    redLed.off()
    greenLed.on()
    
def yellowLedPressed():
    greenLed.off()
    redLed.off()
    yellowLed.pulse()

def redLedPressed():
    yellowLed.off()
    greenLed.off()
    redLed.pulse()

def allLedOn():
    greenLed.on()
    redLed.on()
    yellowLed.on()
    
def allLedOff():
    greenLed.off()
    redLed.off()
    yellowLed.off()
    
def shutAllDown():
    allLedOn()
    time.sleep(1)
    allLedOff()
    GPIO.cleanup()
    
greenButton.when_pressed = greenLedPressed
yellowButton.when_pressed = yellowLedPressed
redButton.when_pressed = redLedPressed

redButton.when_held = shutAllDown
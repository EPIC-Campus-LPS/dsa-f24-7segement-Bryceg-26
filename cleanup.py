import RPi.GPIO as GPIO
import time as timr
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
pins = []
for i in range(2, 28):
    pins.append(i)
GPIO.setup(pins,GPIO.OUT)
GPIO.output(pins,GPIO.HIGH)
timr.sleep(1)
GPIO.output(pins,GPIO.LOW)


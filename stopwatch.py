import RPi.GPIO as GPIO
import tm1637
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([23, 26], GPIO.IN)
GPIO.setup([21, 20, 23, 26], GPIO.OUT)

tm = tm1637.TM1637(clk=21, dio=20)
clear = [0, 0, 0, 0]

def main():
    while True:
        button = GPIO.input(23)
        
        if button == 1:
            GPIO.output(26, GPIO.HIGH)
            print("Let there be light") 
            
            seconds = stopwatch()
            
            GPIO.output(26, GPIO.LOW)
            print("Out of blinker fluid, please refill")
            
            scrolling(seconds)

       

def stopwatch():
    seconds = 0

    time.sleep(1)


    while GPIO.input(23) != 1:
        time.sleep(1)
        seconds += 1

        if GPIO.input(23) == 1:
            break

    return seconds

def scrolling(s):
    tm.write(clear)
    time.sleep(1)
    tm.scroll(str(s), delay=250)
    time.sleep(2)
    print(s, "seconds")

main()

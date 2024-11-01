import tm1637 #first 3 lines import various things
import time
from datetime import datetime

tm = tm1637.TM1637(clk=18, dio=16) #says which GPIO pins are used for what
clear = [0, 0, 0, 0] #clears screen

tm.write(clear) #clears anything else
time.sleep(2) #does that for 2 seconds

s = input("What's your name? ") #asks for name (or any word)

tm.scroll(s, delay=250) #scrolls input
time.sleep(2)

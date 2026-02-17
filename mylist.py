from machine import Pin
import time

r1 = Pin(2, Pin.OUT)
r2 = Pin(4, Pin.OUT)
r3 = Pin(18, Pin.OUT)
r4 = Pin(19, Pin.OUT)
while True:
    numbers=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    for i in numbers:
        r1.value(i[0])
        r2.value(i[1])
        r3.value(i[2])
        r4.value(i[3])
        time.sleep(0.5)
    #Create any list

from servo.servo import *
import time
import wiringpi as gpio

gpio.wiringPiSetupGpio()

s = Servo(18)
t = Servo(17)


while True:
    t.move4time(1)
    time.sleep(1)
    s.move4time(1)
    time.sleep(1)
    t.move4time(1, forwards=False)
    time.sleep(1)
    s.move4time(1, forwards=False)
    time.sleep(1)

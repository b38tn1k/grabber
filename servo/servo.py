import wiringpi as gpio
import threading

class Servo():
    def __init__(self, pin):
        self.pin = pin
        self.forwards_pulse = 10
        self.backwards_pulse = 30
        gpio.softPwmCreate(pin, 50, 100)
        gpio.softPwmWrite(self.pin, 0)

    def __del__(self):
        gpio.softPwmWrite(self.pin, 0)

    def start(self, forwards=True):
        if forwards is True:
            gpio.softPwmWrite(self.pin, self.forwards_pulse)
        else:
            gpio.softPwmWrite(self.pin, self.backwards_pulse)

    def stop(self):
        gpio.softPwmWrite(self.pin, 0)

    def move4time(self, time, forwards=True):
        t = threading.Timer(time, self.stop)
        self.start(forwards)
        t.start()

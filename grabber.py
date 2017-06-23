import RPi.GPIO as GPIO
import threading
# setup up pin layout when this clas is imported
GPIO.setmode(GPIO.BOARD)

class Grabber():
    
    def __init__(self, dir_p=11, step_p=12, stepper_steps=200, lead_travel=50, frequency=200):
        # Pins
        GPIO.setup(step_p, GPIO.OUT)
        GPIO.setup(dir_p, GPIO.OUT)
        self.step_interface = GPIO.PWM(step_p, frequency)
        self.step_interface.stop()
	self.step_p = step_p
	self.dir_p = dir_p
        # Motor Characteristics
        self.stepper_steps = stepper_steps
        # Time
	self.frequency = frequency
        # Model
	self.rps = frequency / stepper_steps
        self.clockwise = True
        self.lead_travel = lead_travel # how far the lead screw travels in one revolution
    
    def stop(self):
        self.step_interface.stop()

    def drive(self, forwards=True):
        if self.clockwise is True:
            GPIO.output(self.dir_p, GPIO.HIGH)
        else:
            GPIO.output(self.dir_p, GPIO.LOW)
        self.step_interface.start(50)

    def move_to_position(self, position):
        # UNTESTED!
        pulse_count = (float(position)/(self.lead_travel)) * self.stepper_steps
        time = pulse_count / self.frequency
        t = threading.Timer(time, self.stop)
        if position < 0:
            self.clockwise = True
        else:
            self.clockwise = False
        self.drive()
        t.start()

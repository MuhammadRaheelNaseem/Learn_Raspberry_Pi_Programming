# Make l298n class then import and use this
import RPi.GPIO as io

class L298N():
    """A class to control one side of an L298N dual H bridge motor driver."""
    def __init__(self, in1, in2):
        self.in1 = in1
        self.in2 = in2
        all_pins = [self.in1, self.in2]
        io.setmode(io.BCM)
        io.setup(all_pins, io.OUT)
        io.setwarnings(False)

    def forwards(self):
        io.output(self.in1, 1)
        io.output(self.in2, 0)

    def backwards(self):
        io.output(self.in1, 0)
        io.output(self.in2, 1)

    def stop(self):
        io.output(self.in1, 0)
        io.output(self.in2, 0)

    def cleanup(self):
        io.cleanup()
        io.setmode(io.BCM)

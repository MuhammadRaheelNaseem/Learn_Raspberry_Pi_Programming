from l298n import l298n
motor = l298n(2, 3)
motor.forwards()
motor.backwards()
motor.stop()

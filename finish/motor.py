import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
#for anable 1 and 2
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
#for input 1
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
#for input 2
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
pwm1 = GPIO.PWM(11, 50)
pwm2 = GPIO.PWM(13, 50)
pwm3 = GPIO.PWM(19, 50)
pwm4 = GPIO.PWM(21, 50)

def stop():
    GPIO.output(3, GPIO.LOW)
    GPIO.output(5, GPIO.LOW)

def f_forward():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)

def b_backward():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    GPIO.output(13, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)

def l_forward():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    pwm1.start(50)
    GPIO.output(19, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)

def r_forward():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    pwm3.start(50)
    GPIO.output(11, GPIO.HIGH)
    GPIO.output(13, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)

def r_backward():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    pwm2.start(50)
    GPIO.output(21, GPIO.HIGH)

def l_backward():
    GPIO.output(3, GPIO.HIGH)
    GPIO.output(5, GPIO.HIGH)
    GPIO.output(11, GPIO.LOW)
    GPIO.output(19, GPIO.LOW)
    pwm4.start(50)
    GPIO.output(11, GPIO.HIGH)


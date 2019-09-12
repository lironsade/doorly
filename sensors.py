import RPi.GPIO as GPIO
from time import sleep
from picamera import PiCamera


is_locked = False
is_lights_are_on = False
camera = PiCamera()

################################################### GPIO pins setup #############################################################
GPIO.setmode(GPIO.BOARD)

#Servo
GPIO.setup(3, GPIO.OUT)
pwm=GPIO.PWM(3, 50)
pwm.start(0)
#LEDs
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)

def set_angle(angle):
    duty = angle / 18 + 2
    GPIO.output(3, True)
    pwm.ChangeDutyCycle(duty)
    sleep(1)
    GPIO.output(3, False)
    pwm.ChangeDutyCycle(0)

def lock():
    if is_locked:
        set_angle(0)
        is_locked = False

def unlock():
    if not is_locked:
        set_angle(90)
        is_locked = True

def is_locked():
    return is_locked

def take_picture():
    camera.capture('/home/pi/Desktop/image.jpg')
    return '/home/pi/Desktop/image.jpg'



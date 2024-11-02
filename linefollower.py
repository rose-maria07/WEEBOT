import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define motor pins
motor1_in1 = 4
motor1_in2 = 14
motor2_in1 = 17
motor2_in2 = 18

# Define IR sensor pins
left_sensor = 2
right_sensor = 3

# Set up GPIO pins
GPIO.setup(motor1_in1, GPIO.OUT)
GPIO.setup(motor1_in2, GPIO.OUT)
GPIO.setup(motor2_in1, GPIO.OUT)
GPIO.setup(motor2_in2, GPIO.OUT)
GPIO.setup(left_sensor, GPIO.IN)
GPIO.setup(right_sensor, GPIO.IN)

# Function to move forward
def move_forward():
    GPIO.output(motor1_in1, GPIO.HIGH)
    GPIO.output(motor1_in2, GPIO.LOW)
    GPIO.output(motor2_in1, GPIO.HIGH)
    GPIO.output(motor2_in2, GPIO.LOW)

# Function to turn left
def turn_left():
    GPIO.output(motor1_in1, GPIO.HIGH)
    GPIO.output(motor1_in2, GPIO.HIGH)
    GPIO.output(motor2_in1, GPIO.HIGH)
    GPIO.output(motor2_in2, GPIO.LOW)

# Function to turn right
def turn_right():
    GPIO.output(motor1_in1, GPIO.HIGH)
    GPIO.output(motor1_in2, GPIO.LOW)
    GPIO.output(motor2_in1, GPIO.LOW)
    GPIO.output(motor2_in2, GPIO.HIGH)

# Function to stop
def stop():
    GPIO.output(motor1_in1, GPIO.LOW)
    GPIO.output(motor1_in2, GPIO.LOW)
    GPIO.output(motor2_in1, GPIO.LOW)
    GPIO.output(motor2_in2, GPIO.LOW)

try:
    while True:
        # Read IR sensor values
        left_value = GPIO.input(left_sensor)
        right_value = GPIO.input(right_sensor)

        # Print sensor values
        print(f"Left Sensor: {left_value}, Right Sensor: {right_value}")

        # Line-following logic
        if left_value == 0 and right_value == 0:
            move_forward()
        elif left_value == 1 and right_value == 0:
            turn_right()
        elif left_value == 0 and right_value == 1:
            turn_left()
        else:
            stop()

except KeyboardInterrupt:
    # Clean up GPIO on program exit
    GPIO.cleanup()

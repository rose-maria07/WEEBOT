import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BCM)

# Define laser pin
laser_pin = 26 # You can change this to any available GPIO pin

# Set up GPIO pin
GPIO.setup(laser_pin, GPIO.OUT)

# Function to turn on the laser
def laser_on():
    GPIO.output(laser_pin, GPIO.HIGH)

# Function to turn off the laser
def laser_off():
    GPIO.output(laser_pin, GPIO.LOW)

try:
    # Turn on the laser
    print("Laser ON")
    laser_on()

    # Keep the laser on for 5 seconds
    time.sleep(5)

    # Turn off the laser
    print("Laser OFF")
    laser_off()

except KeyboardInterrupt:
    pass

finally:
    # Clean up GPIO on program exit
    GPIO.cleanup()

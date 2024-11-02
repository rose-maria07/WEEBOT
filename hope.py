from ultralytics import YOLO
import time
import pigpio

# Load your model
model = YOLO('weed.pt')

# Initialize pigpio
pi = pigpio.pi()

# Define GPIO pins for servos and laser
SERVO_X_PIN = 5  # GPIO pin for X-direction servo
SERVO_Y_PIN = 6  # GPIO pin for Y-direction servo
LASER_PIN = 26    # GPIO pin for laser

# Function to move servos
def move_servos(x, y):
    # Convert coordinates to servo angles or positions
    x_position = int(x / 640 * 2000) + 500  # Example mapping for x
    y_position = int(y / 480 * 2000) + 500  # Example mapping for y
    
    # Move the servos
    pi.set_servo_pulsewidth(SERVO_X_PIN, x_position)
    pi.set_servo_pulsewidth(SERVO_Y_PIN, y_position)

# Function to activate laser
def activate_laser(duration=5):
    pi.write(LASER_PIN, 1)  # Turn on laser
    time.sleep(duration)    # Keep the laser on for the duration
    pi.write(LASER_PIN, 0)  # Turn off laser

# Run detection on the live feed from ESP32-CAM
results = model(source=0, conf=0.2, show=True, save=True)

# Loop through the results
for result in results:
    print(result)
    # Loop through the detections
    for detection in result:
        # Get the class name and coordinates
        class_name = detection['name']
        if class_name == 'weed':
            x1, y1, x2, y2 = detection['box']
            x_center = (x1 + x2) / 2
            y_center = (y1 + y2) / 2
            
            # Move the servos to the detected coordinates
            move_servos(x_center, y_center)
            
            # Activate the laser for 5 seconds
            activate_laser()

# Cleanup
pi.set_servo_pulsewidth(SERVO_X_PIN, 0)
pi.set_servo_pulsewidth(SERVO_Y_PIN, 0)
pi.stop()

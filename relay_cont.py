import RPi.GPIO as GPIO
import time

# Use BCM pin numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins
RELAY_1 = 17
RELAY_2 = 27

# Setup GPIO pins as output
GPIO.setup(RELAY_1, GPIO.OUT)
GPIO.setup(RELAY_2, GPIO.OUT)

# Turn both relays OFF initially
GPIO.output(RELAY_1, GPIO.HIGH)
GPIO.output(RELAY_2, GPIO.HIGH)

print("Relay control started. Press Ctrl+C to exit.")

try:
    while True:
        print("Turning ON Relay 1")
        GPIO.output(RELAY_1, GPIO.LOW)
        time.sleep(2)

        print("Turning ON Relay 2")
        GPIO.output(RELAY_2, GPIO.LOW)
        time.sleep(2)

        print("Turning OFF Relay 1 and Relay 2")
        GPIO.output(RELAY_1, GPIO.HIGH)
        GPIO.output(RELAY_2, GPIO.HIGH)
        time.sleep(2)

except KeyboardInterrupt:
    print("\nExiting and cleaning up GPIO.")
    GPIO.cleanup()

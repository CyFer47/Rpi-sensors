import RPi.GPIO as GPIO
import time

PIR_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN)

print("PIR Sensor Test: Watching GPIO 22")

try:
    while True:
        value = GPIO.input(PIR_PIN)
        if value == 1:
            print("Motion Detected")
        else:
            print("No motion")
        time.sleep(0.2)  # faster polling

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Exit")

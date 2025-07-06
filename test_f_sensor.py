import RPi.GPIO as GPIO
import time

FLOW_SENSOR = 23
pulse_count = 0

def pulse_callback(channel):
    global pulse_count
    pulse_count += 1
    print("Pulse detected")

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    GPIO.add_event_detect(FLOW_SENSOR, GPIO.FALLING, callback=pulse_callback)
    print("Listening for pulses (10 seconds)...")
    time.sleep(10)
    print("Total Pulses:", pulse_count)

finally:
    GPIO.cleanup()

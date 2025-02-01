import RPi.GPIO as GPIO
import time

# Define the GPIO pin for the relay
RELAY_PIN = 15  # GPIO15

# Set up GPIO
GPIO.setmode(GPIO.BCM)  # Use BCM numbering
GPIO.setup(RELAY_PIN, GPIO.OUT)  # Set GPIO14 as output

try:
    while True:
        print("Relay ON")
        GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn ON relay
        time.sleep(2)  # Wait for 2 seconds

        print("Relay OFF")
        GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn OFF relay
        time.sleep(2)  # Wait for 2 seconds

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Clean up GPIO on exit

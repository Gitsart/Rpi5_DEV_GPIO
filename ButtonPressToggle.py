import RPi.GPIO as GPIO
import time

# Define GPIO pins
RELAY_PIN = 14  # GPIO14 for the relay
BUTTON_PIN = 15  # GPIO15 for the button

# Set up GPIO
GPIO.setmode(GPIO.BCM)  
GPIO.setup(RELAY_PIN, GPIO.OUT)  # Set relay as output
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PULLUP)  # Button with pull-up

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)  # Read button state
        
        if button_state == GPIO.LOW:  # Button pressed
            print("Button Pressed - Relay ON")
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn ON relay
        else:
            print("Button Released - Relay OFF")
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn OFF relay
        
        time.sleep(0.1)  # Small delay to avoid bouncing

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Clean up GPIO on exit

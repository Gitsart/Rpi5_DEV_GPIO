import RPi.GPIO as GPIO
import time

# Define GPIO pins
RELAY_PIN = 14  # GPIO14 for the relay
BUTTON_PIN = 15  # GPIO15 for the button

# Set up GPIO
GPIO.setmode(GPIO.BCM)  
GPIO.setup(RELAY_PIN, GPIO.OUT)  # Set relay as output
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Set pull-up resistor

count = 0  # Initialize count variable
button_previous = GPIO.HIGH  # Track previous button state

try:
    while True:
        button_state = GPIO.input(BUTTON_PIN)  # Read button state
        
        # Detect button press (falling edge)
        if button_state == GPIO.LOW and button_previous == GPIO.HIGH:
            count += 1  # Increment count
            print(f"COUNTNUM: {count}")  # Print count
            print("Button Pressed - Relay ON")
            GPIO.output(RELAY_PIN, GPIO.HIGH)  # Turn ON relay

        # Detect button release (rising edge)
        elif button_state == GPIO.HIGH and button_previous == GPIO.LOW:
            print("Button Released - Relay OFF")
            GPIO.output(RELAY_PIN, GPIO.LOW)  # Turn OFF relay

        button_previous = button_state  # Update previous button state
        time.sleep(0.1)  # Small delay to avoid bouncing

except KeyboardInterrupt:
    print("\nExiting...")
    GPIO.cleanup()  # Clean up GPIO on exit
t
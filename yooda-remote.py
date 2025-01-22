import RPi.GPIO as GPIO
from time import sleep
import sys

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Relay pins
RELAYS = [14, 18, 23, 24, 4, 25, 27, 22]

# Initialize all relay pins to OFF
for pin in RELAYS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)

print("[Press Ctrl+C to stop the script]")


def toggle_pin(pin, delay=0.2):
    """Toggle a relay pin ON and OFF."""
    GPIO.output(pin, GPIO.HIGH)
    print(f"Pin {pin} turned OFF")
    sleep(delay)
    GPIO.output(pin, GPIO.LOW)
    print(f"Pin {pin} triggered")
    sleep(delay)
    GPIO.output(pin, GPIO.HIGH)


def activate_remote():
    """Activate the remote control."""
    GPIO.output(22, GPIO.HIGH)
    sleep(0.1)
    GPIO.output(22, GPIO.LOW)
    sleep(3)


def deactivate_remote():
    """Deactivate the remote control."""
    GPIO.output(22, GPIO.HIGH)
    sleep(0.1)


def control_shutter(position, direction):
    """
    Control the shutter based on the given position and direction.

    Args:
        position (int): Position of the shutter (0 to 15).
        direction (str): Direction to move the shutter ('open' or 'close').
    """
    activate_remote()

    current_position = 1  # Yooda Remote always starts at position 1 after a Restart.
    if position == current_position:
        print("No position change needed.")
    elif position == 0:
        print("Moving to position 0.")
        toggle_pin(14)  # Jump directly to position 0. Avoiding unnecessary triggering for the left key.
    else:
        steps = abs(15 + current_position - position)
        print(f"Moving {steps} step(s) to position {position}.")
        for _ in range(steps):
            toggle_pin(14)

    # Open or close the shutter
    if direction == "open":
        toggle_pin(23)  # Open
    elif direction == "close":
        toggle_pin(18)  # Close
    else:
        print("Error: Invalid direction parameter!")

    deactivate_remote()


def main():
    """Main function to parse arguments and control the shutter."""
    if len(sys.argv) != 3:
        print("Usage: python yooda-remote.py [position: 0-15] [direction: open|close] \nError: 001 - Check your arguments!" )
        sys.exit(1)

    try:
        position = int(sys.argv[1])
        direction = sys.argv[2].lower()

        if position < 0 or position > 15:
            print("Usage: python yooda-remote.py [position: 0-15] [direction: open|close] \nError: 002 - Position must be between 0 and 15.")
            sys.exit(2)

        if direction not in ["open", "close"]:
            print("Usage: python yooda-remote.py [position: 0-15] [direction: open|close] \nError: 003 - Direction must be 'open' to open or 'close' to close.")
            sys.exit(3)

        control_shutter(position, direction)
    except ValueError:
        print("Error: Position must be an integer.")
        sys.exit(4)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    finally:
        GPIO.cleanup()

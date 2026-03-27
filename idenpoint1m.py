# idenpoint 1m, github version

import sys
import time
import threading
import itertools

# Improved spinner with message
def spinner_task(stop_event, message="Processing"):
    spinner = itertools.cycle(["|", "/", "-", "\\"])
    while not stop_event.is_set():
        sys.stdout.write(f"\r{next(spinner)} {message}...")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write("\rDone!           \n")

# Reusable function to run spinner for a fixed duration
def run_spinner(duration=4, message="Processing"):
    stop_event = threading.Event()
    spinner_thread = threading.Thread(target=spinner_task, args=(stop_event, message))
    spinner_thread.start()
    time.sleep(duration)
    stop_event.set()
    spinner_thread.join()

# Slow printing function for effect
def slow_print(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# --- Main Program ---
print("Welcome to IdenPoint!")
print("To set status, press Enter, to see version and about IdenPoint, press V, and to exit, press E.")
print()

status = input().strip()

if status.lower() == "v":
    slow_print("Version 1.0m")
    slow_print("Version 1m is the mobile released version of IdenPoint, made by GBCosine Corp, licensed and used by Gupolev, and made by an 8 year old as of 2026. Version 1m is also 2 kilobytes large.")
    slow_print("Note: If your name is gab, the application will recognize you as the 8 year old that created the program.")
    slow_print("Ending Program...")
    run_spinner(message="Closing")
    sys.exit()

elif status.lower() == "e":
    slow_print("Ending Program...")
    run_spinner(message="Closing")
    sys.exit()

elif status == "":
    name = input("Name: ")
    age = input("Age: ")
    if name.lower() == "gab":
        slow_print("Your updating again!")
    else:
        input("Press Enter to confirm ")
        print("Saving...")
        run_spinner(message="Saving")
        print("Done!")

else:
    slow_print("Invalid input! Exiting...")
    run_spinner(message="Exiting")

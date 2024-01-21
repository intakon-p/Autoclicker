import time
import pyautogui
import keyboard

def auto_clicker(duration, start_hotkey, stop_hotkey):
    running = False

    while True:
        if keyboard.is_pressed(start_hotkey):
            running = not running
            time.sleep(0.5)  # Small delay to avoid multiple toggles

        if keyboard.is_pressed(stop_hotkey):
            running = False
            pyautogui.mouseUp()  # Release the mouse button
            time.sleep(0.5)  # Small delay to avoid multiple toggles

        if running:
            pyautogui.mouseDown()
            time.sleep(duration)
            pyautogui.mouseUp()

# Example usage: Click and hold for 10 seconds, toggle with 'z' to start and 'x' to stop
auto_clicker(10, 'z', 'x')

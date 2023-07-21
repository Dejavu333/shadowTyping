import pyautogui
import win32api
import win32gui
import win32con
import threading
import keyboard

def is_hotkey_pressed():
    # Get the state of the Alt key.
    alt_key_state = win32api.GetAsyncKeyState(win32con.VK_F2)
    # Return True if the Alt key is pressed, otherwise return False.
    return alt_key_state


# Then, create a list to store the window handles that have been selected by the user.
selected_windows = []


# Use a while loop to wait for the Alt key to be pressed on another thread.
def register_selected_windows():
    while True:
        # Check if the Alt key is pressed.
        if is_hotkey_pressed():
            # Use the mouse to click on a window.
            pyautogui.click()
            # Get the handle of the window that was clicked on.
            clicked_window_handle = pyautogui.getActiveWindow()
            # Add the clicked window handle to the list of selected windows.
            if clicked_window_handle not in selected_windows:
                selected_windows.append(clicked_window_handle)


# Start the thread and run the function.
t = threading.Thread(target=register_selected_windows)
t.start()

def f(p_str_to_type):
    # Use a for loop to iterate through the selected windows and type into each one.
    starting_window = pyautogui.getActiveWindow()._hWnd
    for window_handle in selected_windows:
        hWnd = window_handle._hWnd
        # Focus on the window # Type the string
        win32api.Sleep(100)
        win32gui.SetForegroundWindow(hWnd);pyautogui.typewrite(p_str_to_type)
    # Return to the starting window
    win32gui.SetForegroundWindow(starting_window)


text = ""
while True:
    rec = keyboard.record(until='space')
    # Or this
    for event in rec:
        if event.event_type == "down":
            if event.name == "space" or event.name == "f2" or event.name=="backspace":
                text += " "
                try:
                    f(text)
                except:
                    pass
                text = ""
            else:
                text += event.name
    print(text)

import pyautogui
import time

message = (input("Enter your message: "))
total_messages = int(input("Enter the number of messages you want to send: "))

while total_messages > 0:
    time.sleep(3)
    pyautogui.typewrite(message)
    time.sleep(1)
    pyautogui.press('enter')
    total_messages = total_messages - 1
import pyautogui
import time

print("Começando..")
time.sleep(2)

for i in range(10):
    for i in range(340):
        pyautogui.write('a')
        pyautogui.press('backspace')
        print(i)

    pyautogui.click(x=494, y=378)
    time.sleep(0.2)
    pyautogui.click(x=1117, y=517)


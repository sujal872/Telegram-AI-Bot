import pyautogui
import time

print("Move your mouse to desired location.")
print("Press CTRL + C to stop.\n")

try:
    time.sleep(5)
    while True:
        print(pyautogui.position())
        
except KeyboardInterrupt:
    print("\nStopped.")

# 558,96
# 1286,647





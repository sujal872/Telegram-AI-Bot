import pyautogui
import pyperclip
import time
import os
from google import genai
from dotenv import load_dotenv

# -------------------------
# LOAD ENV
# -------------------------
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "models/gemini-flash-latest"

pyautogui.FAILSAFE = True

print("Starting Smart Auto Telegram Bot in 5 seconds...")
time.sleep(5)

last_chat = "" # stores previous message

# -------------------------
# COORDINATES
# (Change according to your screen)
# -------------------------

CHAT_CLICK = (850,746)
SELECT_START = (511, 99)
SELECT_END = (967, 664)
CANCEL_SELECTION = (1318, 52)
INPUT_BOX = (565, 704)
SEND_BUTTON = (1338, 705)

# Click Telegram Chat
pyautogui.click(CHAT_CLICK)
time.sleep(0.8)

# -------------------------
# MAIN LOOP
# -------------------------
while True:

    # Select chat messages
    pyautogui.moveTo(SELECT_START)
    pyautogui.dragTo(SELECT_END, duration=1.2)
    time.sleep(0.5)

    # Copy messages
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)

    chat_history = pyperclip.paste()

    if chat_history.strip() == "":
        continue

    # Check new message
    if chat_history == last_chat:
        print("No new message...")
        time.sleep(5)
        continue

    last_chat = chat_history

    print("\nNEW MESSAGE:\n", chat_history)

    # Cancel selection
    pyautogui.click(CANCEL_SELECTION)
    time.sleep(0.3)

    # Send to Gemini
    prompt = f"""
You are chatting as a real human(Your Name) on Telegram.

Rules:
- Keep replies short and natural
- Use casual Hinglish or simple English
- Avoid robotic tone

Message:
{chat_history}

Reply:
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    reply = response.text

    print("\nBOT REPLY:\n", reply)

    # Click input box
    pyautogui.click(INPUT_BOX)
    time.sleep(0.3)

    # Paste reply
    pyperclip.copy(reply)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)

    # Send
    pyautogui.click(SEND_BUTTON)

    print("Reply Sent ✔")

    time.sleep(8)
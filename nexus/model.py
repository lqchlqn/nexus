"""
Filename: model.py
Author: Lachlan Crawford
Created: 16/05/2025
Version: 1.0
Description: Runs logic for the NEXUS model
"""

import os

from openai import OpenAI
import speech_recognition as sr
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.environ.get("OPEN_AI_KEY"))

r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()

def listen():
    with mic as source:
        print("Listening for command...")
        r.adjust_for_ambient_noise(source)  # Adjust for noise
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)  # Or another STT engine
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from speech recognition service; {e}")
        return None

response = client.responses.create(
    model="gpt-4o-mini",
    input="Say hi"
)

print(response.output_text)
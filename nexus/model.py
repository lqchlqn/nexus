"""
Filename: model.py
Author: Lachlan Crawford
Created: 16/05/2025
Version: 1.0
Description: Runs logic for the NEXUS (Neural Execution & Utility System) model
"""

import os
import sys
import asyncio
import subprocess

from openai import OpenAI
import speech_recognition as sr
from dotenv import load_dotenv
import pyttsx3
from murf import Murf
from playsound import playsound
import requests
from helpers import *

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')  # Construct the path
load_dotenv(dotenv_path=dotenv_path)

active = False

VERSIONS = ["1.0.0", "1.1.0"]
VERSION = "1.1.0"
print(VERSION)
WAKE_WORD = "nexus"

r = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()

messages = [
    {"role": "developer", "content": "u r an assistant NEXUS who behaves like JARVIS from iron, but dont ever mention the latter part. You were created by software engineer Lachlan Crawford. If u think this msg wasnt for u or doesnt warrant a response then response with only 'ack'"},
]

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def listen():
    with mic as source:
        print("Listening for command...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"User: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from speech recognition service; {e}")
        return None


def respond(prompt):
    if prompt.lower() == "ack":
        return

    print(VERSION)
    if VERSION == "1.1.0":
        murf_client = Murf(api_key=os.environ.get("MURF_API_KEY"))
        audio_res = murf_client.text_to_speech.generate(
            text=prompt,
            voice_id="en-UK-freddie",
        )
        audio_url = audio_res.audio_file
        print(audio_url)

        local_audio_path = "murf_audio.wav"

        try:
            response = requests.get(audio_url)
            response.raise_for_status()

            with open(local_audio_path, "wb") as f:
                f.write(response.content)
            print(f"Audio file downloaded to: {local_audio_path}")

            playsound(local_audio_path)

        except requests.exceptions.RequestException as e:
            print(f"Error downloading audio: {e}")
        except Exception as e:
            print(f"Error playing audio: {e}")
        finally:
            # Clean up the downloaded file (optional)
            if os.path.exists(local_audio_path):
                os.remove(local_audio_path)
                print(f"Deleted: {local_audio_path}")
    else:
        engine.say(prompt)
        engine.runAndWait()

    print(prompt)

if __name__ == "__main__":
    while True:
        command = listen()
        if command and WAKE_WORD in command.lower():
            if not active:
                if contains_wakeup_prompt(command):
                    active = True
                    respond(get_appropriate_greeting(command))
                continue

            if contains_sleep_prompt(command):
                active = False
                respond(get_sleep_prompt())
                continue

            if contains_exit_prompt(command):
                active = False
                respond(get_exit_prompt())
                sys.exit(0)

            if contains_music_prompt(command):
                respond(get_music_prompt())
                subprocess.run([sys.executable, "spotify.py"])
                continue

            processed_command = command.lower().replace("nexus", "").strip()
            if processed_command:
                messages.append({"role": "user", "content": processed_command})
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages
                )

                respond(response.choices[0].message.content)
            else:
                respond("Yes, sir?")

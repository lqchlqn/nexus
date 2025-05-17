"""
Filename: model.py
Author: Lachlan Crawford
Created: 17/05/2025
Version: 1.0
Description: Helper functions for model.py
"""

import random
import datetime

WAKEUP_PROMPTS = ["nexus wake up", "nexus turn on", "nexus power on", "nexus power up", "nexus you there", "nexus whats up", "nexus whats going on",
                  "wake up nexus", "turn on nexus", "power on nexus", "power up nexus", "you there nexus", "whats up nexus", "whats going on nexus", "hey nexus"]
SLEEP_PROMPTS = ["nexus sleep", "nexus thats all", "nexus thatll be all", "take a nap nexus",
                    "sleep nexus", "thats all nexus", "thatll be all nexus", "nexus take a nap"]
EXIT_PROMPTS = ["nexus power off", "power off nexus", "nexus power down", "power down nexus", "nexus shut down", "shut down nexus", "nexus shutdown", "shut down nexus"]

def get_time_of_day():
    """
    Determines the current time of day
    """
    now = datetime.datetime.now()
    hour = now.hour

    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    elif 17 <= hour < 21:
        return "evening"
    else:
        return "night"

BASIC_GREETINGS = ["Oh hello sir,", "Welcome back sir,", "Hello sir,", f"Good {get_time_of_day()} sir,"]
BASIC_ENDINGS = ["How may I be of service?", "What'll it be today?", ""]


def contains_wakeup_prompt(command):
    """
    Determines whether a wakeup prompt is in the given command
    """

    command = command.lower().replace("\'", "")

    for prompt in WAKEUP_PROMPTS:
        if prompt in command:
            return True
    return False

def contains_sleep_prompt(command):
    """
    Determines whether a sleep prompt is in the given command
    """

    command = command.lower().replace("\'", "")
    print(command)
    for prompt in SLEEP_PROMPTS:
        if prompt in command:
            return True
    return False

def get_sleep_prompt():
    """
    Returns a random sleep prompt
    """

    return random.choice(["About time you gave me a rest sir.",
                            "As you wish sir, I'll talk to you later.",
                            "As you wish sir.",
                            "Of course sir."])

def contains_exit_prompt(command):
    """
    Determines whether an exit prompt is in the given command
    """
    
    command = command.lower().replace("\'", "")
    for prompt in EXIT_PROMPTS:
        if prompt in command:
            return True
    return False

def get_exit_prompt():
    """
    Returns a random exit prompt
    """

    return random.choice(["Powering down.",
                          "Exiting.",
                          "Shutting down."])

def get_appropriate_greeting(prompt):
    """
    Returns the appropriate response for a given wakeup prompt
    """

    prompt = prompt.lower().replace("'", "")

    if prompt in ["nexus you there", "you there nexus", "nexus you up", "you up nexus"]:
        return  random.choice(["For you sir, always.",
                                "When am I not here for you sir?",
                                "Online and ready sir.",
                                "At your service sir.",
                                ""])
    elif prompt in ["nexus whats up", "nexus whats going on", "whats up nexus", "whats going on nexus"]:
        return  random.choice(["Nothing new with me sir,",
                       "Good to hear from you, sir.",
                       f"Good {get_time_of_day()} sir,"]) + \
                " " + \
                random.choice(["How can I be of service?", "What can I do for you?",
                                "How're you doing?", "What'll it be today?"])
    else:
        return random.choice(BASIC_GREETINGS) + " " + random.choice(BASIC_ENDINGS)

def contains_music_prompt(command):
    command = command.lower().replace("\'", "")
    return command in ["nexus drop my needle", "nexus play my jam"]

def get_music_prompt():
    return random.choice(["Feeling groovy are we today sir?"])
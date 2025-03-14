#######################################################################
#           ___                       ______            __            #
#          /   | __  ___________ _   /_  __/___  ____  / /____        #
#         / /| |/ / / / ___/ __ `/    / / / __ \/ __ \/ / ___/        #
#        / ___ / /_/ / /  / /_/ /    / / / /_/ / /_/ / (__  )         #
#       /_/  |_\__,_/_/   \__,_/    /_/  \____/\____/_/____/          #
#                       https://auratools.xyz/                        #
#                    https://discord.gg/auratools                     #
#                            Neptune Free                             #
#######################################################################
              
from src import *
from src.utils import *
from src.utils.checkforupdates import *
from src.utils.ui import *
from src.utils.moreutils import *

import time
import threading

# skids going to love this 💀

# this is encrypted with an anti-skid mechanism
# 1. creating comments, so that i can distract you and waste your time
# 2. naming my functions weird. you never gonna know what fucking "freshlymadeproductfromchina" is, unless you know a bit of python, or have a brain i guess
# - but you wouldnt be skidding if you had a brain or knew python. right?
# eh, cant really stop you
# giv credits ig
# thats motivation, wtf
# why am i motivating you
# why are you still reading this
# ive wasted my time aswell
# am i trolling myself?
# am i going crazy?
# crazy?
# Rocks, they're crazy. I used to be crazy once. The locked me in a rubber room with rubber rocks. Oh well. That's life. Life is like a 
# magazine. It only cost $0.50. 50 cents? Rats! Rats are as small as rocks. Rocks, they're crazy... I used to be crazy once...
# Rocks, they're crazy. I used to be crazy once. The locked me in a rubber room with rubber rocks. Oh well. That's life. Life is like a 
# magazine. It only cost $0.50. 50 cents? Rats! Rats are as small as rocks. Rocks, they're crazy... I used to be crazy once...
# Rocks, they're crazy. I used to be crazy once. The locked me in a rubber room with rubber rocks. Oh well. That's life. Life is like a 
# magazine. It only cost $0.50. 50 cents? Rats! Rats are as small as rocks. Rocks, they're crazy... I used to be crazy once...
# Rocks, they're crazy. I used to be crazy once. The locked me in a rubber room with rubber rocks. Oh well. That's life. Life is like a 
# magazine. It only cost $0.50. 50 cents? Rats! Rats are as small as rocks. Rocks, they're crazy... I used to be crazy once...
# Rocks, they're crazy. I used to be crazy once. The locked me in a rubber room with rubber rocks. Oh well. That's life. Life is like a 
# magazine. It only cost $0.50. 50 cents? Rats! Rats are as small as rocks. Rocks, they're crazy... I used to be crazy once...

def mocktext(text):
    start_upper = random.choice([True, False])
    return "".join(
        char.upper() if (i % 2 == 0) == start_upper else char.lower()
        for i, char in enumerate(text)
    )

def messagespammer():
    clear()
    showbanner()

    message = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Message: {w}")
    
    channelid = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Channel ID: {w}")
    einput = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Emoji (y/n): {w}")

    if einput.lower() == 'y':
        emojiam = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Emoji Amount: {w}")
        try:
            emojiam = int(emojiam)
            if emojiam < 0 or emojiam > 50:
                raise ValueError
        except ValueError:
            print(f"                        {w}[{red}!{w}] {red} Max Emoji amount is 50!")
            return
    else:
        emojiam = 0

    mpinput = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Massping (y/n): {w}")

    if mpinput.lower() == 'y':
        print(f"                        {w}[{red}~{w}] {red} Mass Ping is a Premium Feature!{w}")
        time.sleep(1.5)
        webbrowser.open("https://auratools.xyz/")
        webbrowser.open("https://discord.gg/auratools")

    minput = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Mock (y/n): {w}")

    rsinput = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Random String (y/n): {w}")
    if rsinput.lower() == 'y':
        rstringam = input(f"                        {w}[{cs[1]}~{w}] {cs[1]} Random String Amount: {w}")
        try:
            rstringam = int(rstringam)
        except ValueError:
            print(f"                        {w}[{red}!{w}] {red} Invalid number for Random String Amount!")
            return
    else:
        rstringam = 0

    clear()
    showbanner()
    threads = []
    for token in tokens:
        thread = threading.Thread(target=coolthread, args=(token, channelid, message, minput, emojiam, emojilist, rstringam))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def coolthread(token, channelid, message, mock_input, emoji_amount, emojilist, random_string_amount):
    while True:
        theworthyemojis = "".join(random.choices(emojilist, k=emoji_amount)) if emoji_amount > 0 else ""
        randomstring = "".join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", k=random_string_amount)) if random_string_amount > 0 else ""

        mockingbird = mocktext(message) if mock_input.lower() == 'y' else message

        freshlymadeproductfromchina = f"{mockingbird} ~> {theworthyemojis}" + f"~> {randomstring}"

        res = requests.post(
            f"https://discord.com/api/v9/channels/{channelid}/messages",
            data={"content": freshlymadeproductfromchina},
            headers={"Authorization": token},
            proxies=getrandomproxy(),
        )
        if res.status_code == 200:
            print(f"                        {w}[{cs[1]}~{w}]{cs[1]} Sent {w}~> {cs[2]}{token[:-35]}************{re}")
        elif res.status_code in [401, 403]:
            print(f"                        {w}[{red}~{w}]{red} Failed {w}~> {red}{token[:-35]}************{re}")
        elif res.status_code == 429:
            print(f"                        {w}[{ye}~{w}] {ye}Ratelimit {w}~> {ye}{token[:-35]}************{re}")

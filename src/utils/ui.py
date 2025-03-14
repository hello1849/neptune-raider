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
from src.utils.checkforupdates import *

from colorama import Fore, Style

def terminaltheme(color):
    color_codes = {
        'blue':    [21,  20,  19,  18,  17,  16],
        'pink':    [200, 201, 207, 213, 219, 225],
        'green':   [22, 28, 64, 34, 46, 82],
        'red':     [52, 88, 124, 160, 196, 15],
        'white':   [244, 245, 246, 248, 251, 255],
    }
    shades = color_codes.get(color, [])
    if shades:
        return [f"\x1b[38;5;{shade}m" for shade in shades]
    else:
        return []

cs = terminaltheme('blue')  # change this if u want a diff color, too lazy to add the config support
w = Fore.WHITE
b = Style.BRIGHT
n = Style.NORMAL
re = Style.RESET_ALL
bl = Fore.BLUE
di = Style.DIM
gr = Fore.GREEN
inf = di + bl
ye = Fore.YELLOW
red = Fore.RED

banner = rf"""
            {cs[1]}                       _____ _____ _____ _____ _____ _____ _____
            {cs[2]}                      |   | |   __|  _  |_   _|  |  |   | |   __|
            {cs[3]}                      | | | |   __|   __| | | |  |  | | | |   __|
            {cs[4]}                      |_|___|_____|__|    |_| |_____|_|___|_____|
"""

gui = rf""" 
            {cs[1]}                       _____ _____ _____ _____ _____ _____ _____
            {cs[2]}                      |   | |   __|  _  |_   _|  |  |   | |   __| <~> {w}Free Version
            {cs[3]}                      | | | |   __|   __| | | |  |  | | | |   __| <D> {w}Discord
            {cs[4]}                      |_|___|_____|__|    |_| |_____|_|___|_____| Version {w}- {cs[4]}{vers} 
            {cs[3]}                                 discord.gg/auratools
            {cs[1]}                                   {w}FREE VERSION

            {cs[0]}      <01>{cs[1]} {w}Joiner    {cs[0]}<06>{cs[2]} {w}Nick Changer   {cs[0]}<11>{cs[1]} {w}Channel Spammer  {cs[0]}<16>{cs[2]} {w}VC Joiner
            {cs[0]}      <02>{cs[1]} {w}Leaver    {cs[0]}<07>{cs[2]} {w}Bio Changer    {cs[0]}<12>{cs[1]} {w}Group Spammer    {cs[0]}<17>{cs[2]} {w}Member Scraper
            {cs[0]}      <03>{cs[1]} {w}Checker   {cs[0]}<08>{cs[2]} {w}Pron. Changer  {cs[0]}<13>{cs[1]} {w}Reaction Spammer {cs[0]}<18>{cs[2]} {w}Webhook Menu
            {cs[0]}      <04>{cs[1]} {w}Formatter {cs[0]}<09>{cs[2]} {w}Remove Dupes   {cs[0]}<14>{cs[1]} {w}Reply Spammer    {cs[0]}<19>{cs[2]} {w}Bypass Menu
            {cs[0]}      <05>{cs[1]} {w}Onliner   {cs[0]}<10>{cs[2]} {w}Mass Typer     {cs[0]}<15>{cs[1]} {w}Server Check     {cs[0]}<20>{cs[2]} {w}Spam Menu

            {cs[0]}      NEP{cs[1]}TUN{cs[2]}E {w}» """

def showbanner():
    print(banner)

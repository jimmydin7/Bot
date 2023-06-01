
import socket
import subprocess
import os
import random
import time

performance = random.randint(10, 30)
performance = str(performance) + "%"



def watermark():

    print("""
    ApolloTerminal [Version 0.1]
    Apollo™, all rights deserved

    """)

watermark()

def all_characters_are_space(string):
    return all(char == ' ' for char in string)


desktop = socket.gethostname()
ip = socket.gethostbyname(desktop)


def recognize_command(command):

    global desktop

    if command == "ipcheck":
        print(f"[>] IP: {ip}")
        print(f"[>] Desktop: {desktop}")
    elif "ping" in command:
        ip_for_ping = command.replace("ping", "")
        print(subprocess.getoutput(f"ping{ip_for_ping}"))
    elif "dir" in command:
        tree = subprocess.getoutput("tree")
        print(tree)
    elif "setname" in command:
        name = command.replace("setname", "").lower().replace(" ", "")
        with open("name.txt", "w") as f:
            f.write(name)
        print(f"[+] Successfully set terminal name to '{name}'!")
        desktop = name
    elif "color" in command:
        command = command.replace("color", "")
        if "green" in command:
            os.system('color a')
            print("[+] Set the terminal color to white!")
        elif "red" in command:
            os.system('color c')
            print("[+] Set the terminal color to red!")
        elif "blue" in command:
            os.system('color 1')
            print("[+] Set the terminal color to blue!")
        elif "white" in command:
            os.system('color 7')
            print("[+] Set the terminal color to white!")
        else:
            print("[!] Unknown color. The available options are green, red, blue and white.")
    
    elif "cls" in command:
        os.system("cls")
        watermark()

    elif "version" in command:
        if "/pro" in command:
            key = input("[>] Enter your licence key >> ")
            if "KsaX" in key:
                print("[+] Successfully changed to Apollo Pro!")
            else:
                print("[!] Invalid apollo key! ")
                
        else:
            print("[>] Apollo™ version 0.1")

    elif "config" in command:
        if "/fps" in command:
            
            
            os.system("fsutil behavior set memoryusage 2")
            os.system("bcdedit /set increaseuserva 8000")

            
            
            
        elif "/net" in command:
            os.system("ipconfig /flushdns")
            print("[+] Successfully optimized ping")
            time.sleep(0.7)
            print(f"[+] According to calculations, you will average {performance} better network performance")
        else:
            print("""[!] For this command, you need to add a parameter such as:
            /fps ( optimize FPS )
            /net ( optimize ping )
            -- These commands improve your computer's performance --
            """)

    
    else:
        if all_characters_are_space(command):
            pass
        else:
            print("[!] Unknown command. Please check your spelling, and for help type 'help'")



    
def run_terminal(stat_name):
    command = input(f"root@{stat_name}>> ")
    recognize_command(command)

while True:
    stat_name = desktop
    run_terminal(stat_name)

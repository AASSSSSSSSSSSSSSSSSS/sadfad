from datetime import datetime
from itertools import cycle
from colorama import Fore
import proxy_generator
import threading
import requests
import psutil
import ctypes
import json
import sys
import os

# Title : Ukiyo - A Discord Vanity Sniper
# Date : 31/12/2021
# Author https://github.com/1x12

with open('config.json') as config_file:
    config = json.load(config_file)
class Change:
    def __init__(self):
        self.proxies = proxy_generator.grab_proxies()
        self.proxy_pool = cycle(self.proxies)
        self.proxy = next(self.proxy_pool)
        self.webhook = config["webhook_url"]
        self.token = config["token"]
        self.datetime = datetime.now().strftime('[On %Y-%m-%d @ %H:%M:%S]')
        self.cpu_usage = psutil.cpu_percent()
        self.ram_usage = psutil.virtual_memory().percent
        self.headers = {"authorization": self.token,
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

    def print_logo(self):
        if os.name == "nt":
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Ukiyo - RAM Usage @ {self.ram_usage}% | CPU Usage @ {self.cpu_usage}%]")
        elif os.name == "posix":
            sys.stdout.write(f"\x1b]2;[Ukiyo - RAM Usage @ {self.ram_usage}% | CPU Usage @ {self.cpu_usage}%]\x07")
        else:
            print("Unsupported operating system - could not change window title.")
        print(f"""
         *   *    .  *      .        .  *   .          *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
   *  .  . *       *    .        .        .   *    ..  *    *            .      *   *         *   *    .  *      .        .  *   .
 .    *        .        .      .        .            *         *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
    *.   *          .     *      *        *    .     *.   *          .     *      *        *    .
         *   *    .  *      .        .  *   .          *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
   .        ..    *    .      *  .  ..  *    .        ..    *    .      *  .  ..  *         *   *    .  *      .        .  *   .
         *   *    .  *      .        .  *   .          *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .

                                    {Fore.LIGHTBLUE_EX}:::    ::: :::{Fore.MAGENTA}  ::: ::::{Fore.BLUE}::::::: :::{Fore.LIGHTMAGENTA_EX}   :::  ::::::::  
                                    {Fore.LIGHTBLUE_EX}:+:    :+: :+:{Fore.MAGENTA} :+:      {Fore.BLUE}:+:     :+:{Fore.LIGHTMAGENTA_EX}   :+: :+:    :+: 
                                    {Fore.LIGHTBLUE_EX}+:+    +:+ +:+{Fore.MAGENTA}+:+       {Fore.BLUE}+:+      +:{Fore.LIGHTMAGENTA_EX}+ +:+  +:+    +:+ 
                                    {Fore.LIGHTBLUE_EX}+#+    +#+ +#+{Fore.MAGENTA}+#+       {Fore.BLUE}+#+        {Fore.LIGHTMAGENTA_EX}+#+    +#+    +#+ 
                                    {Fore.LIGHTBLUE_EX}#+#    #+# #+#{Fore.MAGENTA} #+#      {Fore.BLUE}#+#        {Fore.LIGHTMAGENTA_EX}#+#    #+#    #+# 
                                     {Fore.LIGHTBLUE_EX}########  ###{Fore.MAGENTA}  ### ####{Fore.BLUE}#######    {Fore.LIGHTMAGENTA_EX}###     ######## 

                                                       {Fore.LIGHTCYAN_EX}[DEVELOPER INFO]{Fore.RESET}
                                  {Fore.LIGHTGREEN_EX}Donate {Fore.RESET}|{Fore.LIGHTGREEN_EX} bc1qarzdvq6z8tfj45f4runsajaqtmywlh4y76862m 
                                     {Fore.LIGHTMAGENTA_EX}Dev {Fore.RESET}|{Fore.LIGHTMAGENTA_EX} https://github.com/1x12

{Fore.LIGHTCYAN_EX}{self.datetime} {Fore.LIGHTGREEN_EX}Ukiyo was launched.""")   

    def change_vanity(self):
        self.proxy = next(self.proxy_pool)
        payload = {"code": vanity_url}
        response = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/vanity-url", headers=self.headers, json=payload, proxies={"http": self.proxy})
        if response.status_code == 200:
            data = {"content" : f"discord.gg/{vanity_url} bu urlyi aldım @everyone", "username" : "Spidey Bot"}
            requests.post(self.webhook, json=data)
            print(f"{Fore.LIGHTGREEN_EX}{self.datetime}VANITY SNIPED : discord.gg/{vanity_url} has been sniped successfully!{Fore.RESET}")
            sys.exit()

        else:
            print(f"{Fore.LIGHTRED_EX}Unknown Error! Could not snipe discord.gg/{vanity_url}! Status Code : {response.status_code} | Better luck next time :(")

    def check_vanity(self):
        self.proxy = next(self.proxy_pool)
        response = requests.get(f"https://discord.com/api/v9/invites/{vanity_url}?with_counts=true&with_expiration=true", headers=self.headers, proxies={"http": self.proxy})
        if response.status_code == 404:
            Change().change_vanity()
            sys.exit()
        else:
            print(f'{Fore.LIGHTRED_EX}[ + ] Vanity is still taken. [attempting to snipe discord.gg/{vanity_url}]{Fore.RESET}')

    def multi_vanityCheck(self):
        with open('vanities.txt', 'r') as vanity_urls:
            for vanity in vanity_urls:
                vanity_url = vanity.strip()
                self.proxy = next(self.proxy_pool)
                response = requests.get(f"https://discord.com/api/v9/invites/{vanity_url}?with_counts=true&with_expiration=true", headers=self.headers, proxies={"http": self.proxy})
                if response.status_code == 404:
                    payload = {"code" : vanity}
                    requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}/vanity-url", headers=self.headers, json=payload)
                    data = {"content" : f"Vanity URL : discord.gg/{vanity_url} has been sniped successfully! | GGs :flushed: ||@everyone||", "username" : "Ukiyo."}
                    requests.post(self.webhook, json=data)
                    print(f"{Fore.LIGHTGREEN_EX}VANITY SNIPED : discord.gg/{vanity_url} has been sniped successfully!{Fore.RESET}")
                    sys.exit()
                else:
                    print(f'{Fore.LIGHTRED_EX}[ + ] Vanity is still taken. [attempting to snipe discord.gg/{vanity_url}]{Fore.RESET}')

Change().print_logo()
print(f"""{Fore.LIGHTMAGENTA_EX}Select one of the options below. (input either 1 or 2)
{Fore.RESET}[ 1. ] {Fore.LIGHTGREEN_EX}Single Vanity Snipe
{Fore.RESET}[ 2. ] {Fore.LIGHTGREEN_EX}Multi-vanity Snipe{Fore.RESET}""")

option = int(input(f"{Fore.LIGHTCYAN_EX}Option{Fore.RESET} > "))
if option == 1:
    vanity_url = input(f'{Fore.LIGHTCYAN_EX}Vanity To Snipe {Fore.RESET}> ')
    guild_id = input(f'{Fore.LIGHTCYAN_EX}The guild to swap the sniped vanity to [GUILD ID] {Fore.RESET}> ')
    thread_count = int(input(f'{Fore.LIGHTCYAN_EX}Thread Count {Fore.RESET}> '))
    while True:
        for i in range(thread_count):
            threading.Thread(target=Change().check_vanity, daemon=False).start()
elif option == 2:
    print(f"{Fore.RED}WARNING! :{Fore.RESET}To use this feature the vanities you're trying to snipe must be in vanities.txt")
    guild_id = input(f'{Fore.LIGHTCYAN_EX}The guild to swap the sniped vanity to [GUILD ID] {Fore.RESET}> ')
    thread_count = int(input(f'{Fore.LIGHTCYAN_EX}Thread Count {Fore.RESET}> '))
    while True:
        for i in range(thread_count):
            threading.Thread(target=Change().multi_vanityCheck, daemon=False).start()
else:
    print(f"{Fore.LIGHTRED_EX}INVALID OPTION! Re-open the program and try again!{Fore.RESET}")
    input("Press Enter To Close The Program...")

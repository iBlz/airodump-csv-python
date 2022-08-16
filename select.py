from simple_term_menu import TerminalMenu
from rich.console import Console
from colorama import Fore
from tabulate import tabulate
import fileinput
import re
import pandas
import time
import os

def selectnet():
    global bssid
    bssids = []
    essids = []
    enc = []
    power = []

    df = pandas.read_csv('out-01.csv', skipinitialspace=True, usecols=['BSSID'])
    df = df.to_string(justify="left").split("Station MAC", 1)[0]
    df = df[:df.rfind('\n')].split("\n",1)[1]
    for line in df.splitlines():
        bssids.append(f"{Fore.RED}%s{Fore.WHITE}" % line[3:].replace(" ",""))
    df = pandas.read_csv('out-01.csv', skipinitialspace=True, usecols=['ESSID'])
    df = df.dropna()
    df = df.to_string(justify="left").split("Station MAC", 1)[0]
    df = df.split("\n",1)[1]
    for line in df.splitlines():
        essids.append(f"{Fore.RED}%s{Fore.WHITE}" % line[3:].replace(" ",""))
    df = pandas.read_csv('out-01.csv', skipinitialspace=True, usecols=['Privacy'])
    df = df.to_string(justify="left").split("BSSID", 1)[0]
    df = df[:df.rfind('\n')].split("\n",1)[1]
    for line in df.splitlines():
        enc.append(f"{Fore.RED}%s{Fore.WHITE}" % line[3:].replace(" ",""))
    df = pandas.read_csv('out-01.csv', skipinitialspace=True, usecols=['Power'])
    df = df.dropna()
    df = df.to_string(justify="left").split("Station MAC", 1)[0]
    df = df.split("\n",1)[1]
    for line in df.splitlines():
        power.append(f"{Fore.RED}%s{Fore.WHITE}" % line[2:].replace(" ",""))

    table = {f'{Fore.RED}ESSID{Fore.WHITE}': essids, f'{Fore.RED}BSSID{Fore.WHITE}': bssids, f'{Fore.RED}Encryption{Fore.WHITE}': enc, f'{Fore.RED}Power (dBm){Fore.WHITE}': power}
    print(tabulate(table, tablefmt='fancy_grid', headers='keys'))

#    print(f"{Fore.GREEN}Choose BSSID")
#    mac = TerminalMenu(macs).show()
#    print("")
#    bssid = macs[mac]
#    print(bssid)

def selectcli():
    global cli
    found = False
    for line in fileinput.input("out-01.csv",inplace=True):
        if re.match("Station MAC",line):
            found = True
        if found:
            print(line,end="")
        else:
            print(end="")
    df = pandas.read_csv('out-01.csv', skipinitialspace=True, usecols=['Station MAC'])
    df = df.to_string(justify="left")
    df = df.split("\n",1)[1]
    macs = []
    for line in df.splitlines():
        macs.append(line[3:])
    print(f"{Fore.GREEN}Choose Client")
    cli = TerminalMenu(macs).show()
    print("")
    cli = macs[cli]

selectnet()

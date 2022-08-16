
from colorama import Fore
from tabulate import tabulate
import re
import pandas

bssids = []
essids = []
enc = []
power = []

file = 'out-01.csv'

df = pandas.read_csv(file, skipinitialspace=True, usecols=['BSSID'])
df = df.to_string(justify="left").split("Station MAC", 1)[0]
df = df[:df.rfind('\n')].split("\n",1)[1]
for line in df.splitlines():
    bssids.append(f"{Fore.RED}%s{Fore.WHITE}" % line[3:].replace(" ",""))

df = pandas.read_csv(file, skipinitialspace=True, usecols=['ESSID'])
df = df.dropna()
df = df.to_string(justify="left").split("Station MAC", 1)[0]
df = df.split("\n",1)[1]
for line in df.splitlines():
    essids.append(f"{Fore.RED}%s{Fore.WHITE}" % line[3:].replace(" ",""))

df = pandas.read_csv(file, skipinitialspace=True, usecols=['Privacy'])
df = df.to_string(justify="left").split("BSSID", 1)[0]
df = df[:df.rfind('\n')].split("\n",1)[1]
for line in df.splitlines():
    enc.append(f"{Fore.RED}%s{Fore.WHITE}" % line[3:].replace(" ",""))
    
df = pandas.read_csv(file, skipinitialspace=True, usecols=['Power'])
df = df.dropna()
df = df.to_string(justify="left").split("Station MAC", 1)[0]
df = df.split("\n",1)[1]
for line in df.splitlines():
    power.append(f"{Fore.RED}%s{Fore.WHITE}" % line[2:].replace(" ",""))

table = {f'{Fore.RED}ESSID{Fore.WHITE}': essids, f'{Fore.RED}BSSID{Fore.WHITE}': bssids, f'{Fore.RED}Encryption{Fore.WHITE}': enc, f'{Fore.RED}Power (dBm){Fore.WHITE}': power}
print(tabulate(table, tablefmt='fancy_grid', headers='keys'))

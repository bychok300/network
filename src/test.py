import os
import time

class txtcolors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


while True:

    hostname = "192.168.0.1"

    response = os.system("ping -c 4 " + hostname)


    if response == 0:

        print (hostname, 'is up!\n')
        time.sleep(10)

    else:
        print (hostname, 'is down!\n')

        disable_wifi = os.system("ifconfig wlp7s0 down")

        print("wlp7s0 interface was off")
        time.sleep(2)
        disable_wifi = os.system("ifconfig wlp7s0 up")
        print("wlp7s0 interface was on")
        time.sleep(10)
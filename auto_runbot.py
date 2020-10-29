import subprocess
import time
import os, signal

while True:
    print("Launch Caca`s script...")
    PIPE = subprocess.PIPE
    p = subprocess.Popen("python test_bot_hard_for_auto.py", shell = True)
    #time.sleep(30)
    subprocess.Popen.kill(p)

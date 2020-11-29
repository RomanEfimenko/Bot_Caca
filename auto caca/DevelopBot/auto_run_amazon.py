import subprocess
import time
import os, signal

print("Start work malaya...\n")

while True:
    PIPE = subprocess.PIPE
    p = subprocess.Popen("python develop_bot_sobaka.py", shell = True)
    time.sleep(472)
    #time.sleep(32)
    print("Update bot...")

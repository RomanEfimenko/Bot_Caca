import subprocess
import time
import os, signal

print("Start work malaya...\n")

while True:
    PIPE = subprocess.PIPE
    p = subprocess.Popen("python develop_bot_sobaka.py", shell = True)
    time.sleep(475) # Через 472 секунды запустит бота заново
    print("Update bot...\n")
    subprocess.Popen.kill(p)

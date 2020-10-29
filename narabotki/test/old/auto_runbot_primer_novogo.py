import subprocess
import time
import os
import signal
import psutil

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

print("Start test...")

count = 1

while True:
    print("Run: "+str(count))
    count = count + 1
    proc = subprocess.Popen("python exit_script.py", shell=True)
    try:
        proc.wait(timeout=8)
    except subprocess.TimeoutExpired:
        kill(proc.pid)

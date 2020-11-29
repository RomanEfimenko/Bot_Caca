import subprocess
import time
import os, signal

def kill(proc_pid):
    process = psutil.Process(proc_pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()

print("Start work malaya...\n")

while True:
    path_controll_proces = "python develop_bot_sobaka.py";
    proc = subprocess.Popen(path_controll_proces, shell=True)

    time.sleep(35) # Через 472 секунды запустит бота заново
    print("Update bot...\n")
    try:
        kill(proc.pid)
    except:
        print("Процесс отсутствует");

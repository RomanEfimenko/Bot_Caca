import subprocess
import time
import os
import signal

while True:
    print("update bot")
    PIPE = subprocess.PIPE
    cmd = "exec "+"python exit_script.py"
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell = True)
    time.sleep(10);
    p.kill()
    #os.killpg(os.getpgid(p.pid), signal.SIGTERM)
    #subprocess.Popen.kill(p)

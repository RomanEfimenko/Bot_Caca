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

def console_reaction(input_txt):
    if input_txt == "!" :
        print("Работаю только на команды, предурок йобаный.");
    if input_txt == "!log" :
        print("Ещё не доделано!!!!!");
    print("пизда ты чорт");

print("Start AutoRunBot...")
#pulse_time = time.time();
read_nowsession_time = time.time();
read_cns_inpt_time = time.time();
start_script_time = time.time();
restart_script_time = time.time();

def update_time():
    #pulse_time = time.time();
    read_nowsession_time = time.time();
    read_cns_inpt_time = time.time();
    start_script_time = time.time();
    restart_script_time = time.time();

def get_secs(str_time):
    if str_time.find("now") != -1 :
        str_time = str(time.time());
    str_time.rstrip();
    if len(str_time) < 3 :
        str_time = "228"
        print("24: "+str_time)
        str_time = time.time()
    str_time = float(str_time);
    #str_time -= 1603999000.0;
    return str_time;

working = True;
restart_script_bool = False;
input_console_text = "22814322";
#count = 1;

path_controll_proces = "python exit_script.py";
path_console_script = "python auto_runbot_cnsle.py"

proc = subprocess.Popen(path_controll_proces, shell=True)
my_cnsole = subprocess.Popen(path_console_script, shell=True)

while working:
    #print("Run: "+str(count))
    #count = count + 1;

    #---- check time session ---------------------------------------
    if (time.time()-start_script_time) > 1000: # каждые 1000 секунд
        start_script_time = time.time();
        kill(proc.pid)
        proc = subprocess.Popen("python exit_script.py", shell=True)
        update_time()
    #---- check restart_script bool var ---------------------------------
    if restart_script_bool:
        restart_script_time = time.time();
        kill(proc.pid)
        proc = subprocess.Popen("python exit_script.py", shell=True)
        update_time()
    #---- read info nowsession.txt -------------------------------------
    if (time.time()-read_nowsession_time) > 5: # каждые 2 секунд
        read_nowsession_time = time.time();
        nowsession_file = open("data_arn/nowsession.txt", "r");
        nowsession_file_text_ahahaha = nowsession_file.read();
        print("Read nowsession... "+nowsession_file_text_ahahaha+"\n")
        nowsession_file.close();
        if time.time()-get_secs(nowsession_file_text_ahahaha) > 20 : # 20 секунд назад последняя запись? рестарт
            print("Read nowsession... Nowsession dont answer for 20 second...\n");
            #print("Read nowsession... "+str(time.time()-get_secs(nowsession_file_text_ahahaha))+"\n")
            #kill(proc.pid)
            proc = subprocess.Popen(path_controll_proces, shell=True)
            update_time()
    #---- read input_console.txt ------------
    if (time.time()-read_cns_inpt_time) > 1: # каждые 2 секунд
        read_cns_inpt_time = time.time();
        cns_inpt_file = open("data_arn/input_console.txt", "r");
        input_console_text = cns_inpt_file.read();
        cns_inpt_file.close();
        if input_console_text.find("22814322") == -1 :
            print("Read Input console... "+str(input_console_text)+"\n")
            cns_inpt_file = open("data_arn/input_console.txt", "w");
            cns_inpt_file.write("22814322");
            cns_inpt_file.close();
            #console_reaction(input_console_text);
            if input_console_text.find("!log") != -1 :
                print("Ещё не доделано!!!!!"+"\n");
            elif input_console_text.find("!exitcon") != -1 and len(input_console_text) == 9 :
                print("Выключаем контрольный скрипт нахуй...."+"\n\n");
                kill(proc.pid);
            elif input_console_text.find("!exit") != -1 and len(input_console_text) == 6 :
                print("Выключаем всё нахуй...."+"\n\n");
                kill(proc.pid);
                kill(my_cnsole.pid);
                working = False;
            elif input_console_text.find("!") != -1 :
                print("Работаю только на команды, предурок йобаный."+"\n");
            input_console_text = "22814322";

    time.sleep(1);

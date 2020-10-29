import time

pulse_time = time.time();

print("exit_script run\n\n")

#a = input();
#print(a);

time_last = time.time();

while True:
    t = time.time();
    if (t-time_last) > 1 :
        time_last = time.time();
        #print("Прошла секунда сучары, time: "+str(time.time())+"\n");
        #time.sleep(1);


    # ОЦЕ ОЦЕ ОЦЕ

    #---- write info to nowsession.txt -------------------------------------
    if (time.time()-pulse_time) > 1:   # каждую секунду выполнение
        pulse_time = time.time();
        text_file = open("data_arn/nowsession.txt", "w");
        #print("write: "+str(pulse_time));
        text_file.write(str(pulse_time)+"\n");
        text_file.close();

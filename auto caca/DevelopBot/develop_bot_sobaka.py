import amino
import random
import time
import sys
from gtts import gTTS

#---------------------------------------------------------------------------
#----- F "если данная строка входит - вернуть тру"
def fInMsg(txt_res,text_find) :
    if txt_res.find(text_find) != -1:
        return True;
    else :
        return False
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#----- F "Если данные слова в начале строки - вернуть тру"
def fInStMsg(txt_res,text_find) :
    if txt_res.startswith(text_find) :
        return True;
    else :
        return False
#---------------------------------------------------------------------------

#---------------------------------------------------------------------------
#----- F "Если данные слова в начале строки - вернуть тру"
def getChatName(cht_Id) :
    if cht_Id.find('ec7f1dc8-d418-4873-905b-e1544401dd28') != -1 :
        return "ЛЗ.Чат 18+";
    elif cht_Id.find('d2946d45-8835-4e01-b886-fadad4357be7') != -1 :
        return "ЛЗ.Нейрочат";
    elif cht_Id.find("228") != -1 :
        return "228";
    else :
        return "undefined chat name"
#---------------------------------------------------------------------------

start_bot_time = time.time();
fInMsg_msg_content = '';

#try:
if True :

    random.seed(); # my code

    client = amino.Client()

    client.login(email='karapass@bk.ru', password='123456789karapas');

    subclient = amino.SubClient(comId='131410019', profile=client.profile); # 18+
    #subclient = amino.SubClient(comId='41242618', profile=client.profile);  # TEST TEST

    print(time.asctime()+" Malaya autorization...")

    id_chat_test_18 = 'd2946d45-8835-4e01-b886-fadad4357be7';

    id_chat_test = 'ec7f1dc8-d418-4873-905b-e1544401dd28'; # 18+
    #id_chat_test = 'd2946d45-8835-4e01-b886-fadad4357be7'; # TEST ()
    #id_chat_test = '8c6d96a2-58a0-4bae-a499-0efc2b75c98c'; # TEST TEST

    @client.callbacks.event("on_text_message")
    def on_text_message(message):
        data_sms = message.message;
        #---------------------------------------------------
        # Запись сообщения в глобальную переменную
        fInMsg_msg_content = data_sms.content.lower();
        #---------------------------------------------------
        if (str(data_sms.chatId) == id_chat_test or str(data_sms.chatId) == id_chat_test_18) :

            chat_id_name = getChatName(data_sms.chatId);
            print(f"{chat_id_name}:{data_sms.author.nickname}: {data_sms.content}");
            us_id = [];
            us_id.append(data_sms.author.userId);
            if str(data_sms.author.nickname) != "малая" :
                #---------------------------------------------------
                # ---- КОМАНДЫ БОТА
                if fInStMsg(fInMsg_msg_content,"!ping") :
                    subclient.send_message(data_sms.chatId, "pong!");
                elif fInStMsg(fInMsg_msg_content,"!кости") :
                    r = random.randint(1,99);
                    otvet = data_sms.author.nickname+", тобі випала така хуйня: "+str(r);
                    if r > 97:
                        otvet = data_sms.author.nickname+", пізда ти лакєр, випало 99(хуїв тобі за щоку, я таких нє люблю)";
                    subclient.send_message(data_sms.chatId, otvet);
                elif fInStMsg(fInMsg_msg_content,"!дия") :
                    text_plus = data_sms.content[5:len(data_sms.content)]
                    if random.randint(0,100) > 49:
                        subclient.send_message(data_sms.chatId, "[I]"+data_sms.author.nickname+" "+text_plus+" [True]")
                    else :
                        subclient.send_message(data_sms.chatId, "[I]"+data_sms.author.nickname+" "+text_plus+" [Піздьож]")
                elif fInStMsg(fInMsg_msg_content,"!ду") :
                    text_plus = data_sms.content[4:len(data_sms.content)]
                    if random.randint(0,100) > 49:
                        subclient.send_message(data_sms.chatId, "[I]"+text_plus+" [True]")
                    else :
                        subclient.send_message(data_sms.chatId, "[I]"+text_plus+" [Піздьож]")
                elif fInStMsg(fInMsg_msg_content,"!спик") :
                    tts = gTTS(data_sms.content[6:len(data_sms.content)], lang='ru')
                    tts.save('speak.mp3')
                    #subclient.send_message(chatId=data_sms.chatId, message="<$@"+str(data_sms.author.nickname)+"$>", mentionUserIds=[data_sms.author.userId])
                    with open("speak.mp3","rb") as file:
                        subclient.send_message(chatId=data_sms.chatId, file=file, fileType="audio")
                elif fInStMsg(fInMsg_msg_content,"!спік") :
                    tts = gTTS(data_sms.content[6:len(data_sms.content)], lang='uk')
                    tts.save('speak.mp3')
                    #subclient.send_message(chatId=data_sms.chatId, message="<$@"+str(data_sms.author.nickname)+"$>", mentionUserIds=[data_sms.author.userId])
                    with open("speak.mp3","rb") as file:
                        subclient.send_message(chatId=data_sms.chatId, file=file, fileType="audio")
                elif fInStMsg(fInMsg_msg_content,"!speak") :
                    tts = gTTS(data_sms.content[7:len(data_sms.content)], lang='en')
                    tts.save('speak.mp3')
                    #subclient.send_message(chatId=data_sms.chatId, message="<$@"+str(data_sms.author.nickname)+"$>", mentionUserIds=[data_sms.author.userId])
                    with open("speak.mp3","rb") as file:
                        subclient.send_message(chatId=data_sms.chatId, file=file, fileType="audio")
                elif fInStMsg(fInMsg_msg_content,"!help") or fInStMsg(fInMsg_msg_content,"!хелп"):
                    subclient.send_message(data_sms.chatId, "[I]Меджік букви:")
                    subclient.send_message(data_sms.chatId, "!кости !ду !дия !спик !speak")
                #---------------------------------------------------
                #subclient.send_message(data_sms.chatId, "@добрий день\nПідори", replyTo = data_sms.messageId);

    @client.callbacks.event("on_group_member_join")
    def on_group_member_join(message):
        data_sms = message.message;
        if (str(data_sms.chatId) == id_chat_test or str(data_sms.chatId) == id_chat_test_18) :
            print(f"К чату присоеденился: {data_sms.author.nickname}");
            us_id = [];
            #us_id.append(str(data_sms.author.userId));
            us_id.append(data_sms.author.userId);
            #print("mentionUserIds: "+str(data_sms.mentionUserIds))
            if str(data_sms.author.nickname) != "малая" :
                subclient.send_message(data_sms.chatId, "[I]- "+str(data_sms.author.nickname)+"!\n\n[CB]Добро пoжаловать в чат 18+\n\n[I]1.Ознакомься с правилами чата\n[I]2.Скажи нам, кто ты?\n[I]3.Cкинь hi mark(Организатору чата) пруфы своего совершеннолетия!");
                with open("hi.mp3","rb") as file:
                    subclient.send_message(chatId=data_sms.chatId, file=file, fileType="audio")

    # Через 470 секунд после запуска скрипт завершается
    while True :
        #print("Time: "+str(time.time()-start_bot_time))
        if (time.time()-start_bot_time) > 470 :   # Если прошло 470 секунд после запуска вырубаем скрипт
            sys.exit()
    #prekol = True
    #while prekol :
    #    prekol = input()
#except :
    #print("Ошибка во время работы бота!")
    #exit()

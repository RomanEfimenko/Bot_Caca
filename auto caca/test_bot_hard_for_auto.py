import amino
import random
import os
import time

pulse_time = time.time();
offchathimark = False; # Если тру - не пишет смс в общий чат 18+
meAlertSound = False; # Если тру - выдает звук когда меня упоминают в чате.


random.seed(); #

client = amino.Client()

client.login(email='efimenko@ucoz-team.net', password='123456789')

subclient = amino.SubClient(comId="131410019", profile=client.profile) # заходим в сообщество "ЛЗ"

print(time.asctime()+" #--- Begin work caca...");

#------ Выбираем в какой чат будем отправлять сообщения через скрипт "send_sms_cmd.py"
id_chat_send_sms = 'd2946d45-8835-4e01-b886-fadad4357be7'; # TEST
#id_chat_send_sms = 'ec7f1dc8-d418-4873-905b-e1544401dd28'; # 18+
if id_chat_send_sms == 'd2946d45-8835-4e01-b886-fadad4357be7':
    id_chat_send_sms = 'd2946d45-8835-4e01-b886-fadad4357be7';
    #print("--- Choose TEST CHAT");
elif id_chat_send_sms == 'ec7f1dc8-d418-4873-905b-e1544401dd28':
    id_chat_send_sms = 'ec7f1dc8-d418-4873-905b-e1544401dd28';
    #print("--- Choose chat 18+");
#---------------------------------------------------------------------------

oldMessages = []

with open("oldMessages.txt", "r") as oldFile:
    for messageId in oldFile.read().split("\n")[:-1]:
        oldMessages.append(messageId)

while True:
    readChats = subclient.get_chat_threads().chatId

    for chatId in readChats:
        msg = subclient.get_chat_messages(chatId=chatId, size=25)
        for message, messageId, author in zip(msg.content, msg.messageId, msg.author.nickname):
            if not messageId in oldMessages:
                #---------------------------------------------------
                #----- Названия чатов
                chat_name = "ЛЗ общий чат 18+ : "
                if chatId == 'ec7f1dc8-d418-4873-905b-e1544401dd28' :
                    chat_name = "ЛЗ общий чат 18+ : "
                elif chatId == 'd2946d45-8835-4e01-b886-fadad4357be7' :
                    chat_name = "ЛЗ тестовый чат : "

                print(chat_name, author, message)
                #print(chatId, author, message)

                textMessageLower = str(message).lower();

                #---------------------------------------------------
                # "ping" me(Alert sound) - выдает звук когда меня упоминают в чате.
                if meAlertSound :
                    res1 = textMessageLower.find("добрий день");
                    res2 = textMessageLower.find("рома");
                    res3 = 0;
                    #print(str(res1)+"\n"+str(res2));
                    if res1 != -1 :
                        res3 = 228;
                    if res2 != -1 :
                        res3 = 228;
                    if res3 == 228 :
                        #os.system("ds.py");
                        print("\n***Play sound alert***(quiet mode)\n");
                #---------------------------------------------------
                # "18+ off@"
                if offchathimark :
                    if chatId.find('ec7f1dc8-d418-4873-905b-e1544401dd28') != -1 :
                        oldMessages.append(messageId)
                        with open("oldMessages.txt", "a") as oldFile:
                            oldFile.write(messageId + "\n")
                            oldFile.close()
                        continue;
                #---------------------------------------------------
                # "answer to caca sms off@" - бот не отвечает на свои же сообщения
                if author.find('цаца') != -1 :
                    oldMessages.append(messageId)
                    with open("oldMessages.txt", "a") as oldFile:
                        oldFile.write(messageId + "\n")
                        oldFile.close()
                    continue;
                #---------------------------------------------------
                # КОМАНДА БОТА ПРИМЕР
                if str(message).startswith("!ping"):
                    subclient.send_message(chatId, "Pong!")
                #---------------------------------------------------
                # МОИ КОМАНДЫ БОТА
                if textMessageLower.startswith("!кости"):
                    r = random.randint(1,99);
                    otvet = author+", тобі випала така хуйня: "+str(r);
                    if r > 97:
                        otvet = author+", пізда ти лакєр, випало 99(хуїв тобі за щоку, я таких нє люблю)";
                    subclient.send_message(chatId, otvet)
                elif textMessageLower.startswith("!дия"):
                    text_plus = message[5:len(message)]
                    if random.randint(0,100) > 49:
                        subclient.send_message(chatId, "[I]"+author+" "+text_plus+" [True]")
                    else :
                        subclient.send_message(chatId, "[I]"+author+" "+text_plus+" [Піздьож]")
                elif textMessageLower.startswith("!ду"):
                    text_plus = message[4:len(message)]
                    if random.randint(0,100) > 49:
                        subclient.send_message(chatId, "[I]"+text_plus+" [True]")
                    else :
                        subclient.send_message(chatId, "[I]"+text_plus+" [Піздьож]")
                elif textMessageLower.startswith("цаца"):
                    subclient.send_message(chatId, "Сосітє хуй фашисти праклятиє! Мене ше тіки строять, як піраміду")
                elif textMessageLower.startswith("оня"):
                    subclient.send_message(chatId, "Нагадую шо Оня алкоголічка. Слава Україні і всім героям кавказу!")
                elif textMessageLower.startswith("ден"):
                    subclient.send_message(chatId, "Нагадую шо Дєніс - це малолєтка з України, не дайте себе наїбать!")
                elif textMessageLower.startswith("!help") or textMessageLower.startswith("!хелп"):
                    subclient.send_message(chatId, "[I]Меджік букви:")
                    subclient.send_message(chatId, "!кости !ду !дия")
                #---------------------------------------------------

                oldMessages.append(messageId)
                with open("oldMessages.txt", "a") as oldFile:
                    oldFile.write(messageId + "\n")
                    oldFile.close()

    #---- send_sms_cmd.py ---------------------------------------

    text_file = open("send_message_cmd.txt", "r");
    send_message_cmd_string = text_file.read();
    text_file.close();

    text_file_bot = open("testbot_config.txt", "r");
    testbot_config_clac = text_file_bot.read();
    text_file_bot.close();

    if (testbot_config_clac == "!!!1") :
        if id_chat_send_sms == 'd2946d45-8835-4e01-b886-fadad4357be7':
            id_chat_send_sms = 'ec7f1dc8-d418-4873-905b-e1544401dd28';
            print("--- Choose chat 18+\n");
        elif id_chat_send_sms == 'ec7f1dc8-d418-4873-905b-e1544401dd28':
            id_chat_send_sms = 'd2946d45-8835-4e01-b886-fadad4357be7';
            print("--- Choose test chat\n");
    text_file_bot = open("testbot_config.txt", "w");
    text_file_bot.write("");
    text_file_bot.close();

    if (send_message_cmd_string != "") :
        print("Send message: "+send_message_cmd_string);
        subclient.send_message(message=send_message_cmd_string, chatId=id_chat_send_sms);
    text_file = open("send_message_cmd.txt", "w");
    text_file.write("");
    text_file.close();

    #---- write info to nowsession.txt -------------------------------------
    if (time.time()-pulse_time) > 1:   # каждую секунду выполнение
        pulse_time = time.time();
        text_file = open("data_arn/nowsession.txt", "w");
        #print("write: "+str(pulse_time));
        text_file.write(str(pulse_time)+"\n");
        text_file.close();

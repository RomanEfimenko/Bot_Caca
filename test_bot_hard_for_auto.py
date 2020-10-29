import amino
import random
import os
import time

global_time = time.time();

random.seed(); # my code

client = amino.Client()

client.login(email='efimenko@ucoz-team.net', password='123456789')

subclient = amino.SubClient(comId="131410019", profile=client.profile)

id_chat_send_sms = 'd2946d45-8835-4e01-b886-fadad4357be7'; # TEST
#id_chat_send_sms = 'ec7f1dc8-d418-4873-905b-e1544401dd28'; # 18+

print("Begin work...\n");

if id_chat_send_sms == 'd2946d45-8835-4e01-b886-fadad4357be7':
    print("--- Choose TEST CHAT\n\n");
if id_chat_send_sms == 'ec7f1dc8-d418-4873-905b-e1544401dd28':
    print("--- Choose chat 18+\n\n");

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

                print(chatId, author, message)

                # "ping" me comnand
                str_msg_lwr = str(message).lower();
                res1 = str_msg_lwr.find("добрий день");
                res2 = str_msg_lwr.find("рома");
                res3 = 0;
                #print(str(res1)+"\n"+str(res2));
                if str(res1) != "-1" :
                    res3 = 228;
                if str(res2) != "-1" :
                    res3 = 228;
                if str(res3) == "228" :
                    print("\n***Play sound alert***\n");
                    os.system("ds.py");

                #---------------------------------------------------
                # "!ping" comnand
                if str(message).startswith("!ping"):
                    subclient.send_message(chatId, "Pong!")
                #---------------------------------------------------
                # my test comnand
                textMessageLower = str(message).lower();
                if textMessageLower.startswith("!кости"):
                    r = random.randint(1,99);
                    otvet = author+", тобі випала така хуйня: "+str(r);
                    if r > 97:
                        otvet = author+", пізда ти лакєр, випало 99(хуїв тобі за щоку, я таких нє люблю)";
                    subclient.send_message(chatId, otvet)
                if textMessageLower.startswith("цаца"):
                    subclient.send_message(chatId, "Сосітє хуй фашисти праклятиє! Мене ше тіки строять, як піраміду")
                if textMessageLower.startswith("оня"):
                    subclient.send_message(chatId, "Нагадую шо Оня алкоголічка. Слава Україні і всім героям кавказу!")
                if textMessageLower.startswith("ден"):
                    subclient.send_message(chatId, "Нагадую шо Дєніс - це малолєтка з України, не дайте себе наїбать!")
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

    #---- read info to nowsession.txt ---------------------------------------

    if (time.time()-global_time) > 1:   # каждую секунду выполнение
        global_time = time.time();
        text_file = open("nowsession.txt", "w");
        text_file.write(str(global_time));
        text_file.close();

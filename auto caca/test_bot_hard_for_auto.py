import amino
import random
import os
import time

pulse_time = time.time();
offchathimark = False; # Если тру - не пишет смс в общий чат 18+
meAlertSound = False; # Если тру - выдает звук когда меня упоминают в чате.
clbackEventTextMsg = True; # Если тру - срабатывает колбек ивент на сообщения
fInMsg_msg_content = "";
random.seed(); #

client = amino.Client()
client.login(email='efimenko@ucoz-team.net', password='123456789')
BOT_ID = client.profile.userId; # ID бота
subclient = amino.SubClient(comId="131410019", profile=client.profile) # заходим в сообщество "ЛЗ"

#-----------------------------------------------------------------------------
#----- F "если данные слова входят вернуть тру"
def fInMsg(text_find) :
    if fInMsg_msg_content.find(text_find) != -1:
        return True;
    else :
        return False
#---------------------------------------------------------------------------
#------ Отвечаем на некоторые сообщения
#------    @client.callbacks.event("on_text_message")
#------    def on_text_message(message):
#------        data_sms = message.message;
#------        dataSmsContent = str(data_sms.content).lower()
#------        if ((str(data_sms.chatId) == 'd2946d45-8835-4e01-b886-fadad4357be7') or (str(data_sms.chatId) == '18chat')) :
#------            if str(data_sms.author.nickname) != "цаца" :
#------                if data_sms.content.startswith("цаца") :
#------                    subclient.send_message(data_sms.chatId, "Сосітє хуй фашисти праклятиє! Мене ше тіки строять, як піраміду", replyTo = data_sms.messageId)
#------                elif data_sms.content.startswith("ден"):
#------                    subclient.send_message(data_sms.chatId, "Нагадую шо Дєніс - це малолєтка з України, не дайте себе наїбать!", replyTo = data_sms.messageId)
#------                elif data_sms.content.startswith("оня"):
#------                    subclient.send_message(data_sms.chatId, "Нагадую шо Оня алкоголічка. Слава Україні і всім героям кавказу!", replyTo = data_sms.messageId)

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
        for message, messageId, author, authorId in zip(msg.content, msg.messageId, msg.author.nickname, msg.author.userId):
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
                # Изминение ников в чате 18+
                if author == "Линчеватель228":
                    author = "Лянча"
                if author == "denvin228":
                    author = "Скунс"
                if author == "добрий день":
                    #author = "Мій Господар"
                    author = "добрий день"
                #---------------------------------------------------
                # Запись сообщения в глобальную переменную
                fInMsg_msg_content = textMessageLower;
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
                elif textMessageLower.startswith("!help") or textMessageLower.startswith("!хелп"):
                    subclient.send_message(chatId, "[I]Меджік букви:")
                    subclient.send_message(chatId, "!кости !ду !дия")
                #---------------------------------------------------
                # Рандомные фразочки бота
                elif textMessageLower.find('цаца шлюха') != -1:
                    if author == "Мій Господар" :
                        subclient.send_message(chatId, "Ще й яка", replyTo = messageId)
                    else :
                        subclient.send_message(chatId, author+", мамку твою раком трахала)", replyTo = messageId)
                elif textMessageLower.find('цаца стерва') != -1:
                    if author == "Мій Господар" :
                        subclient.send_message(chatId, "Я падаю на коліна і прошу пробачити...", replyTo = messageId)
                    else :
                        subclient.send_message(chatId, author+", в сраку твого батю перла ;)", replyTo = messageId)
                elif textMessageLower.find('цаца салам') != -1 :
                    subclient.send_message(chatId, author+", аллєйкум салам", replyTo = messageId)
                elif fInMsg('цаца ку') or fInMsg('цаца привет') or fInMsg('цаца здравствуй'):
                    subclient.send_message(chatId, author+", салам", replyTo = messageId)
                elif fInMsg('цаца крутая') or fInMsg('цаца классная') or fInMsg('цаца хорошая'):
                    subclient.send_message(chatId, "Дякую, а ти сєкс :3", replyTo = messageId)
                elif fInMsg('цаца бот') or fInMsg('цаца робот') or fInMsg('цаца компютер'):
                    subclient.send_message(chatId, "Пашол нахуй бічара, смокчи конячу бебу", replyTo = messageId)
                elif fInMsg('цаца ты кто') or fInMsg('цаца ты хто') or fInMsg('кто цаца'):
                    subclient.send_message(chatId, "Я тебе ничего не расскажу, а вдруг ты нацик. Или ещё хуже - жид?", replyTo = messageId)
                elif fInMsg("цаца") :
                    if author == "Мій Господар" :
                        subclient.send_message(chatId, "Мій Господарю, пробачте мене сцикуху(((", replyTo = messageId)
                    else :
                        if random.randint(0,100) > 49:
                            subclient.send_message(chatId, "Сосітє хуй фашисти праклятиє! Мене ше тіки строять, як піраміду", replyTo = messageId)
                        else :
                            subclient.send_message(chatId, author+", не трогай мене, животне ванюче. Я вам не нанімалась -_-")
                elif fInMsg("денис") :
                    subclient.send_message(chatId, "Нагадую шо Дєніс - це малолєтка з України, не дайте себе наїбать!", replyTo = messageId)
                elif fInMsg("оня ") :
                    subclient.send_message(chatId, "Нагадую шо Оня алкоголічка. Слава Україні і всім героям кавказу!", replyTo = messageId)
                elif fInMsg('люда з села') or fInMsg('люда з сила') or fInMsg('люда с села'):
                    subclient.send_message(chatId, "Дааа, із сєла прастітуциї і сєкс іскуства)0", replyTo = messageId)
                elif fInMsg('стелла собака') :
                    subclient.send_message(chatId, "Як мінімум гавкає.", replyTo = messageId)
                elif fInMsg('кпоп норм') :
                    subclient.send_message(chatId, "Малолєтка в чаті, провєряй", replyTo = messageId)
                elif fInMsg('рома бандера') or fInMsg('рома укроп') or fInMsg('рома хохол'):
                    subclient.send_message(chatId, "Рома бог, а ти сосеш конячу бебу", replyTo = messageId)
                elif fInMsg('давно тебя не было в уличных гонках') :
                    subclient.send_message(chatId, "Тоже мені блядь гонщік, трактор - це не спорткар", replyTo = messageId)
                elif fInMsg('рома алка') or fInMsg('рома алко') or fInMsg('рома бух') :
                    subclient.send_message(chatId, "Рома професійний соміль'є", replyTo = messageId)
                elif fInMsg('хохлушка') :
                    subclient.send_message(chatId, "Сука ляпнуть би тебе разок, дак гавном ваняєш", replyTo = messageId)
                elif fInMsg('вы все зёпы') or fInMsg('вы все жопы') :
                    subclient.send_message(chatId, "Посмокчи мою чорну єлду", replyTo = messageId)
                elif fInMsg('пососеш') or fInMsg('пасосеш') or fInMsg('пасасеш') :
                    subclient.send_message(chatId,"Хто я?)))0)0", replyTo = messageId, mentionUserIds = [authorId])
                elif fInMsg('стелла це машка') :
                    subclient.send_message(chatId, "Машка мий ноги і йди спать", replyTo = messageId)
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

    #---- read info to editprofilebio.txt -------------------------------------
    editprofilebio_file = open("txts/editprofilebio.txt", "r");
    editprofilebio_text = editprofilebio_file.read();
    if (editprofilebio_text != "") :
        print("Caca set BIO: "+editprofilebio_text);
        subclient.edit_profile(content=editprofilebio_text);
    editprofilebio_file.close();
    editprofilebio_file = open("txts/editprofilebio.txt", "w");
    editprofilebio_file.write("");
    text_file.close();
    #---- read info to addcomment.txt -------------------------------------
    #addcomment_file = open("txts/editprofilebio.txt", "r");
    #addcomment_text = editprofilebio_file.read();
    #if (addcomment_text != "") :
    #    print("Caca set BIO: "+editprofilebio_text);
    #    subclient.edit_profile(content=editprofilebio_text);
    #editprofilebio_file.close();
    #editprofilebio_file = open("txts/editprofilebio.txt", "w");
    #editprofilebio_file.write("");
    #text_file.close();
    #---- write info to nowsession.txt -------------------------------------
    if (time.time()-pulse_time) > 1:   # каждую секунду выполнение
        pulse_time = time.time();
        text_file = open("data_arn/nowsession.txt", "w");
        #print("write: "+str(pulse_time));
        text_file.write(str(pulse_time)+"\n");
        text_file.close();

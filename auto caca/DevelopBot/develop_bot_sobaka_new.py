import amino
import random

random.seed(); # my code

client = amino.Client()

client.login(email='karapass@bk.ru', password='123456789karapas');

subclient = amino.SubClient(comId='131410019', profile=client.profile);

id_chat_test = 'd2946d45-8835-4e01-b886-fadad4357be7'; # TEST
#id_chat_test = 'ec7f1dc8-d418-4873-905b-e1544401dd28'; # 18+

@client.callbacks.event("on_text_message")
def on_text_message(message):
    data_sms = message.message;
    if (str(data_sms.chatId) == id_chat_test) :
        print(f"{data_sms.author.nickname}: {data_sms.content}");
        us_id = [];
        #us_id.append(str(data_sms.author.userId));
        us_id.append(data_sms.author.userId);
        #print("mentionUserIds: "+str(data_sms.mentionUserIds))
        if str(data_sms.author.nickname) != "Karapass" :
            subclient.send_message(data_sms.chatId, "@добрий день\nПідори", replyTo = data_sms.messageId);

@client.callbacks.event("on_group_member_join")
def on_group_member_join(message):
    if (str(data_sms.chatId) == id_chat_test) :
        print(f"К чату присоеденился: {data_sms.author.nickname}");
        us_id = [];
        #us_id.append(str(data_sms.author.userId));
        us_id.append(data_sms.author.userId);
        #print("mentionUserIds: "+str(data_sms.mentionUserIds))
        if str(data_sms.author.nickname) != "Karapass" :
            subclient.send_message(data_sms.chatId, "@добрий день\nПідори", replyTo = data_sms.messageId);

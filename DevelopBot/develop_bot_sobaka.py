import amino
import random

random.seed(); # my code

client = amino.Client()

client.login(email='karapass@bk.ru', password='123456789karapas');

subclient = amino.SubClient(comId='41242618', profile=client.profile);

id_chat_test = "8c6d96a2-58a0-4bae-a499-0efc2b75c98c";

@client.callbacks.event("on_text_message")
def on_text_message(message):
    data_sms = message.message;
    if (str(data_sms.chatId) == "8c6d96a2-58a0-4bae-a499-0efc2b75c98c") :
        print(f"{data_sms.author.nickname}: {data_sms.content}");
        us_id = [];
        #us_id.append(str(data_sms.author.userId));
        us_id.append(data_sms.author.userId);
        #print("mentionUserIds: "+str(data_sms.mentionUserIds))
        if str(data_sms.author.nickname) != "Karapass" :
            subclient.send_message(data_sms.chatId, "@добрий день", replyTo = data_sms.messageId, mentionUserIds=[us_id]);

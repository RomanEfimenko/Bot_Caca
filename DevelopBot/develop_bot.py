import amino
#import random

#random.seed(); # my code

client = amino.Client()

client.login(email='karapass@bk.ru', password='xxxxxxxx');

code = client.sub_clients
print(code)

MY_ID = client.profile.userId;

subclient = amino.SubClient(comId='41242618', profile=client.profile);

print("Begin work...\n\n");

#--------------------------------------------------------------------------

id_chat_test = "8c6d96a2-58a0-4bae-a499-0efc2b75c98c";

@client.callbacks.event("on_text_message")
def on_text_message(message):
    data_sms = message.message;
    if (str(data_sms.chatId) == "8c6d96a2-58a0-4bae-a499-0efc2b75c98c") :
        reply_sms_id = data_sms.clientRefId;
        print("isHidden: "+str(data_sms.isHidden));
        print("clientRefId: "+str(reply_sms_id));

        #if()

        if(data_sms.author.nickname == "добрий день") :
            print(f"{data_sms.author.nickname}: {data_sms.content}");
            if str(data_sms.author.userId) != MY_ID :
                subclient.send_message(data_sms.chatId, "check message", replyTo = data_sms.messageId);

#client.login(email='karapass@bk.ru', password='123456789karapas');

import amino

client = amino.Client()

client.login(email='xxxxxx@mail.ru', password='xxxxxxxx');

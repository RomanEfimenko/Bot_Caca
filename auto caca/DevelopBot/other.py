import amino
import random

random.seed(); # my code


client = amino.Client()

client.login(email='karapass@bk.ru', password='123456789karapas');

subclient = amino.SubClient(comId='41242618', profile=client.profile);

id_chat_test = "8c6d96a2-58a0-4bae-a499-0efc2b75c98c";

@client.callbacks.event("on_text_message")

def on_text_message(message):
    if (str(message.chatId) == id_chat_test) :
        print(f"{message.author.nickname}: {message.content}");
        subclient.send_message(message.chatId, "print message", replyTo = message.messageId);









chatId

oldMessages = []

with open("oldMessagesDevelop.txt", "r") as oldFile:
    for messageId in oldFile.read().split("\n")[:-1]:
        oldMessages.append(messageId)

while True:
    readChats = subclient.get_chat_threads().chatId

    for chatId in readChats:
        msg = subclient.get_chat_messages(chatId=chatId, size=25)
        for message, messageId, author in zip(msg.content, msg.messageId, msg.author.nickname):
            if not messageId in oldMessages:
                print(chatId, author, message)

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
                #---------------------------------------------------

                oldMessages.append(messageId)
                with open("oldMessages.txt", "a") as oldFile:
                    oldFile.write(messageId + "\n")
                    oldFile.close()

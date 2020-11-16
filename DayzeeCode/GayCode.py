print("start")
import amino
import os
import time

clear = lambda: os.system('clear')

packs = "/storage/emulated/0/Send audio file" # директория со звуками # "/storage/emulated/0/Send audio file"

class bcolors:
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[31m'
    blud = '\033[1m'
    undline = '\033[4m'
    end = "\033[0m"

bc = bcolors

client = amino.Client()
client.login(email='@', password='')
print(f"{bc.blue} Вошёл в аккаунт")

subclient = amino.SubClient(comId='156542274', profile=client.profile)

print(f" {bc.yellow}Как вы хотите получить chatId? Вписать вручную или вставить ссылку?\n {bc.cyan}Вписать вручную (В)\n {bc.green}Вставить ссылку (С)\n {bc.red}Стандартное значение (S)")

tid = str(input(f"{bc.blud}{bc.undline}{bc.blue} Ваш ответ: {bc.end}")).lower()

if tid.find('b') != -1 or tid.find('в') != -1 :
    print(f"{bc.green} Сейчас я покажу вам всем, chatId.")
    long = input(f" {bc.yellow}Сколько сообщений брать, с кажого чата: ")
    shh = input(f" {bc.blue}Каким будет ваше скрытное сообщения?: ")
    readChats = subclient.get_chat_threads().chatId

    for chat_id in readChats:
        msg = subclient.get_chat_messages(chatId=chat_id, size=long)

        for message, messageId, author in zip(msg.content, msg.messageId, msg.author.nickname):

            print(f'{bc.green}{author}: {bc.blue}{message} : {bc.yellow}{chat_id}{bc.end}')
            if message == shh:
            	print(f"{bc.cyan} Поздравляем, ваше скрытые сообщения нашли, chatId скопирован")
            	time.sleep(5)
            	clear()
            	print(bc.yellow + str(chat_id))
            	time.sleep(10)
            	break

    chid = input(f"{bc.green} Введите пожалуйста chatId: ")

if tid.find('с') != -1 or tid.find('c') != -1:

	link = input(f"{bc.green} Введите пожалуйста ссылку: ")
	chid = client.get_from_code(link).objectId

if tid.find('s') != -1 :
    # Стандартное значение. Форсированно выбираем чат
    chid = '8c6d96a2-58a0-4bae-a499-0efc2b75c98c'

del tid

print(f"{bc.yellow} Сейчас, будем выбирать пак. Вывожу список папок")

for name in os.listdir(packs):
	if os.path.isdir(os.path.join(packs, name)):
		print(bc.yellow + name)


which_pack = input(f"{bc.cyan} Какой пак, будете использовать?: ")

print("which_pack: "+str(which_pack))

nx = input(f"{bc.blue} Хотите выбрать папку в папке?(Д/Н): ").lower()

if nx.find('д') != -1 or nx.find('y') != -1 :
    print(f"{bc.green} Вывожу, список папок в этой папке.")
    for name in os.listdir(packs):
        if os.path.isdir(os.path.join(packs +'\\' + which_pack, name)):
            print(bc.yellow + name);
            pack1 = input(f"{bc.green} Какую папку, хотите использовать?: ");
    which_pack = which_pack + '\\' + pack1
    del pack1
    del nx



print(f'{bc.yellow} Подсказка, чтобы поменять пак введите: "Change" ')
time.sleep(3)
while True:
    try:
        print(f"{bc.blud}{bc.cyan} Вывожу название всех аудио")
        folder = []
        for i in os.walk(packs + '\\' + which_pack):
            folder.append(i)
        for address, dirs, files in folder:
            for file in files:
                print(address+'\\'+file)
        gh = input(f"{bc.end}{bc.green} Введите название ГС, без .mp3: ")

        with open(packs+'\\'+which_pack+'\\'+gh+".mp3","rb") as file:
            print(f"{bc.yellow}ChatID: "+str(chid)+"\nSend audio: "+str(file));
            subclient.send_message(chatId=chid, file=file, fileType="audio")
        if gh.find('change') != -1 :
            for name in os.listdir(packs):
                if os.path.isdir(os.path.join(packs, name)):
                    print(bc.yellow + name)

            which_pack = input(f"{bc.cyan} какой пак, будете использовать?: ")
    except:
        pass

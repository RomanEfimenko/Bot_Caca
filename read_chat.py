import amino

client = amino.Client()
client.login(email='efimenko@ucoz-team.net', password='123456789')
subclient = amino.SubClient(comId='131410019', profile=client.profile)

f = open('log.txt', 'w'); #my code

chats = subclient.get_chat_threads()
for name, id in zip(chats.title, chats.chatId):
    print(name, id);
    f.write(str(name)+' : '+str(id)+'\n'); #my code

f.close(); #my code

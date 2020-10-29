import amino

client = amino.Client()
client.login(email='karapass@bk.ru', password='123456789karapas')

f = open('log.txt', 'w'); #my code

subclients = client.sub_clients()
for name, id in zip(subclients.name, subclients.comId):
    print(name, id);
    f.write(str(name)+' : '+str(id)+'\n'); #my code

f.close(); #my code

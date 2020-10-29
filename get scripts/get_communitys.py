import amino

client = amino.Client()
client.login(email='karapass@bk.ru', password='123456789karapas')

f = open('log.txt', 'wb'); #my code

subclients = client.sub_clients()
for name, id in zip(subclients.name, subclients.comId):
    print(name, id);
    write_text = str(name)+' : '+str(id)+'\n';
    f.write(write_text.encode('utf8')); #my code

f.close(); #my code

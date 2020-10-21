import amino

client = amino.Client()
client.login(email='efimenko@ucoz-team.net', password='123456789')

f = open('log.txt', 'w'); #my code

subclients = client.sub_clients()
for name, id in zip(subclients.name, subclients.comId):
    print(name, id);
    f.write(str(name)+' : '+str(id)+'\n'); #my code

f.close(); #my code

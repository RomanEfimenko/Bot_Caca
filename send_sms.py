import amino

client = amino.Client()
client.login(email='efimenko@ucoz-team.net', password='123456789')
subclient = amino.SubClient(comId='131410019', profile=client.profile)

subclient.send_message(message='Сосітє хуй фашисти праклятиє', chatId='ec7f1dc8-d418-4873-905b-e1544401dd28')

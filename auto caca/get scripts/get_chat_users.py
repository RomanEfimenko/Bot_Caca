import amino

client = amino.Client()
client.login(email='efimenko@ucoz-team.net', password='123456789')
subclient = amino.SubClient(comId='131410019', profile=client.profile)
id_need_chat = "ec7f1dc8-d418-4873-905b-e1544401dd28"; # Чат 18+

if 1<2 :
    f = open('user_chat_list.txt', 'wb'); #my code
    count_i = 0;
    print("Участники чата:\n\n");
    f.write("Участники чата:\n".encode('utf8'));
    for one_user_nickname in subclient.get_chat_users(id_need_chat,start=0,size=30).profile.nickname:
        count_i = count_i+1;
        str_raz = str(count_i)+'. '+one_user_nickname+'\n';
        print(str_raz);
        f.write(str_raz.encode('utf8'));

#userId
#aminoId
    print("\n\n");
    count_i = 0;
    print("Участники чата Id:\n\n");
    for one_user_nickname in subclient.get_chat_users(type=id_need_chat,start=0,size=30).profile.userId:
        count_i = count_i+1;
        str_raz = str(count_i)+'. '+str(one_user_nickname)+'\n';
        print(str_raz);
        f.write(str_raz.encode('utf8'));
    f.close(); #my code

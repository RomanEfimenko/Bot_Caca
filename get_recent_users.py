import amino

client = amino.Client()
client.login(email='karapass@bk.ru', password='123456789karapas')
subclient = amino.SubClient(comId='131410019', profile=client.profile)

if 1<2 :
    f = open('user_recent_list.txt', 'wb'); #my code
    count_i = 0;
    print("Вступили недавно:\n\n");
    f.write("Вступили недавно:\n".encode('utf8'));
    for one_user_nickname in subclient.get_all_users(type='recent',start=0,size=20).profile.nickname:
        count_i = count_i+1;
        str_raz = str(count_i)+'. '+one_user_nickname+'\n';
        print(str_raz);
        f.write(str_raz.encode('utf8'));

#userId
#aminoId
    print("\n\n");
    count_i = 0;
    print("Вступили недавно Id:\n\n");
    for one_user_nickname in subclient.get_all_users(type='recent',start=0,size=20).profile.userId:
        count_i = count_i+1;
        str_raz = str(count_i)+'. '+str(one_user_nickname)+'\n';
        print(str_raz);
        f.write(str_raz.encode('utf8'));
    f.close(); #my code

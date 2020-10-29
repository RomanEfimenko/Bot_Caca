import amino

client = amino.Client()
client.login(email='efimenko@ucoz-team.net', password='123456789')
subclient = amino.SubClient(comId='131410019', profile=client.profile)

id_need_user = "1a18bf18-4af6-4989-8b48-cd6e0854be4c"; # добрий день
#id_need_user = "a0820c69-7d48-4b26-9e20-32c0f0b83d40"; # HiMark

info_user = subclient.get_user_info(id_need_user);
subclient.visit(id_need_user);

print("nickname: \n"+str(info_user.nickname)+'\n');
print("level: \n"+str(info_user.level)+'\n');
print("onlineStatus: \n"+str(info_user.onlineStatus)+'\n'); # 1 - true 2 - false
print("postsCount: \n"+str(info_user.postsCount)+'\n');
print("avatarFrame: \n"+str(info_user.avatarFrame)+'\n'); # none
print("avatarFrameId: \n"+str(info_user.avatarFrameId)+'\n'); # none
print("membershipStatus: \n"+str(info_user.membershipStatus)+'\n'); # hz
print("role: \n"+str(info_user.role)+'\n'); # 0 - just_user
print("createdTime: \n"+str(info_user.createdTime)+'\n'); # create profile in comunity
print("customTitles: \n"+str(info_user.customTitles)+'\n'); # Роли
print("content: \n"+str(info_user.content)+'\n'); # profile description
print("icon: \n"+str(info_user.icon)+'\n'); # avatar url

print("backgroundImage: \n"+str(info_user.extensions.bm[1])+'\n')



#print("backgroundImage: \n"+str(info_user.backgroundImage)+'\n');
#    try: self.backgroundImage = self.json["extensions"]["bm"][1]

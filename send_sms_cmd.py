while True:

    print("Write message: ");
    inp = input();
    if(str(inp)=="!!!1") :
        text_file_bot = open("testbot_config.txt", "w");
        text_file_bot.write(inp);
        text_file_bot.close();
        print("Change chat...\n--------------------------\n\n");
        continue;
    else :
        if (str(inp) != "") :
            text_file = open("send_message_cmd.txt", "w");
            text_file.write(inp);
            text_file.close();
            print("Complete...\n--------------------------\n\n");

while True :
    inp = input();
    text_file = open("input_console.txt", "w");
    #print("You write: "+inp);
    text_file.write("!"+str(inp)+"\n");
    text_file.close();

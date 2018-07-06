import webbrowser
def chatBot(text):
    if(text == "hi"):
        print("hello")
    elif(text == "hello"):
        print("hi")
    elif(text.split()[:2] == ["count", "to"]):
        try: 
            for count in range(1,int(text.split()[2])+1):
                print(str(count))
        except ValueError:
            print("I can't count to that ya dingus.")
    elif(text == "obunga"):
        print("obunga")
        webbrowser.open('https://cdn.discordapp.com/attachments/441183518588928029/464634625524760577/obunga.jpg')
    elif(text.split()[0] == "add"):
        print(text.split()[1]+" + "+ text.split()[3]+" = " + str(int(text.split()[1])+int(text.split()[3])))
    else:
        print("I can't do that")
print("Type \"exit\" to exit")
chat = ""
while(chat != "exit"):
    chat = input("> ")
    chatBot(chat)
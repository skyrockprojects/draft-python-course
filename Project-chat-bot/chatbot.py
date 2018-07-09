import webbrowser

class ChatBot:
    def __init__(self, chats):
        self.chats = chats
    def start(self):
        self.input = ""
        print("Type \"exit\" to exit.")
        while(self.input != "exit"):
            self.input = input("> ")
            for chat in self.chats:
                chat.input(self.input)

class SimpleChat:
    def __init__(self, aliases, response):
        self.aliases = aliases
        self.response = response
    def input(self, input):
        if input in self.aliases:
            print(self.response)

class AdvancedChat:
    def __init__(self, inputCheck, response):
        self.response = response
        self.inputCheck = inputCheck
    def input(self, input):
        if self.inputCheck(input):
            self.response(input)

hi = SimpleChat(["hi","hello","hey"],"hi")
def hiResponse(self, input):
    print(input)
def hiCheck(self, input):
    if input in ["hi","hello","hey"]:
        return true
    return false
hi = AdvancedChat(hiCheck, hiResponse)
chatList = [hi]
chatBot = ChatBot(chatList)
chatBot.start()
# def chatBot(text):
#     if(text == "hi"):
#         print("hello")
#     elif(text == "hello"):
#         print("hi")
#     elif(text.split()[:2] == ["count", "to"]):
#         try: 
#             for count in range(1,int(text.split()[2])+1):
#                 print(str(count))
#         except ValueError:
#             print("I can't count to that ya dingus.")
#     elif(text == "obunga"):
#         print("obunga")
#         webbrowser.open('https://cdn.discordapp.com/attachments/441183518588928029/464634625524760577/obunga.jpg')
#     elif(text.split()[0] == "add"):
#         print(text.split()[1]+" + "+ text.split()[3]+" = " + str(int(text.split()[1])+int(text.split()[3])))
#     else:
#         print("I can't do that")
# print("Type \"exit\" to exit")
# chat = ""
# while(chat != "exit"):
#     chat = input("> ")
#     chatBot(chat)
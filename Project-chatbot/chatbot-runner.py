# A simple class to run the Chatbot class.
from chatbot import ChatBot
#Create a ChatBot, give it user input, and print its replies.
cb = ChatBot()

print(cb.getGreeting())
statement = input("")

while(statement != "Bye"):
    print(cb.getResponse(statement))
    statement = input("")

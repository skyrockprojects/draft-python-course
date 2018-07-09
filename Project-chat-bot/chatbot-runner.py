# A simple class to run the Chatbot class.
# @author Laurie White
#  @version April 2012
from chatbot import ChatBot
#Create a Magpie, give it user input, and print its replies.
cb = ChatBot()

print(cb.getGreeting())
statement = input("")

while(statement != "Bye"):
    print(cb.getResponse(statement))
    statement = input("")

#Functions take inputs and either do something with it or return a modified verison

#you use the def statement to define a function

#this function adds a and b and returns that value
def add(a,b):
    return a + b

#you can use a function by calling it's name with parentheses surrounding the inputs
onePlusTwo = add(1,2)
print(onePlusTwo)

#functions don't have to return anything

#this function takes a quote and it's author and prints it out

def printQuote(quote, author):
    print(quote,"\n",author)

#functions can accept anything as an imput, but usually you use variables

quoteAuthor = "Declan"

quoteContent = "Yeet"

printQuote(quoteAuthor,quoteContent)
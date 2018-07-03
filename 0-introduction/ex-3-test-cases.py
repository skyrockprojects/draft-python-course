# Test cases are a series of inputs you try to see if the program is funtioning correctly

# Here are my implimentations of the printTwice and subtraction funtions you wrote last lesson

def printTwice(input):
    print(input)
    print(input)

def subtract(a,b):
    return a - b

#Here we test to see that they are working with a variety of things

printTwice("word")
printTwice("twice")
printTwice(123)
printTwice("HELLO!")

#while testing functions that take numbers as inputs it is a good idea to use a variety of large, small, 0, and negative numbers to test all the possible inputs
print(subtract(0,0))
print(subtract(1,0))
print(subtract(23,-1))
print(subtract(2000,-100000))
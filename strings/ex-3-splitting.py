#the .split() function is very useful
#it allows you to take a string and turn it into a list of strings based on what you split by
#if you were to split by the word " by "
exampleString = "Day by day"
#                 1 ---- 2
#you would get a list of ["Day", "day"]
print(exampleString.split(" by "))

#this is very useful if you want to turn a sentence into words
exampleSentence = "It is half past eleven."
#in that case you split by the space character: split(" ")
print(exampleSentence.split(" "))

exampleMultipleSpaces = "Hi     there ."
#if there are multiple of the string you are splitting by it will add empty strings in the list (one less than the amount of spaces)
print(exampleMultipleSpaces.split(" "))

#Instead of typing the space character you can just leave the arguments blank to save times
print(exampleSentence.split())
#Example 1 - Basics

#Strings are a very useful type, they can be added together, or "concatenated"
exampleConcatenation = "first" + "second"
# this turns two strings into one string put together end to end
print(exampleConcatenation)

# Strings have a lot of built in methods, 
# a very useful one is str() which turns anything into a string
# which allows you to print it

#you can turn integers into strings,
print(str(45))
#lists of integers too!
print(str([1,2,3,4,5]))
#you can also print lists of strings
print(str(["a","b","c","d"]))

#another useful method is len() which returns the length of an inputted string
#like lists it returns the amount of things in the string, but this time it is the amount of characters in the string
numberedString = "12345" # 5 characters

print("numberedString length = "+str(len(numberedString)))

#there are two more useful methods that will be useful in a couple situations
#.upper() makes the string UPPERCASE
#and .lower() makes the string lowsercase

exampleWord = "Word"
#original
print(exampleWord.lower())

#all lowercase
print(exampleWord.lower())

#all uppercase
print(exampleWord.upper())

#escape characters are things that you can't actually type with your keyboard
#so they made "codes" for them

#the most common one is: \n which adds a new line
print("firstline\nsecondline")

#you can also add a tab
print("\ttabbed")

#and if you want to have a blackslash in a string you have to escape it to

print("\\ <--single backslash")
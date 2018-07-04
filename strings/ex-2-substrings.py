#strings are kind of like lists of single letters, you can pick and choose any single charachter and use it

exampleString = "Example"
                #0123456
#gets the char number 3, or "m"
print(exampleString[3])

#you can also extract any series of characters

#a the number after the colon tells where to end the new string

# the below string method gets characters 0 thhrough 2
# Example
# 0123456
# +++
print(exampleString[0:2])

# the number before the colon chooses the last character
# the below string method gets characters 0 through 2
# Example
# 0123456
#    ++++
print(exampleString[3:6])

# if you want to take the first part of the string (starting from 0)
# or the last part (the end of the string) there is a very simple way to do this a little bit faster

#instead of putting 0 to take the first part, you can just leave the place empty
#this
print(exampleString[:2])
#is the same as this
print(exampleString[0:2])

#you can also do the same thing with the end of the string

print(exampleString[3:6])
print(exampleString[3:])

#there is also a way to remove charcters from strings if you need to get rid of them

exampleSentence = "Hello world!"
print(exampleSentence)
#if you want to remove one, or a couple characters you can use a negative number

#if you want to remove a single character from the end, you would do this
print(exampleSentence[0:-1])
# Hello world!
#            -

#If you wanted to take more away, just make the number bigger
print(exampleSentence[0:-7])
# Hello world!
#      -------

# you can do the same thing from the beginning
print(exampleSentence[-6:12])
# Hello world!
# ------
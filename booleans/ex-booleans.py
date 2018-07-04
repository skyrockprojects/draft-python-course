# booleans (bool) are a very simple data type they can be True or False
# True and False have to be capitalized
exampleTrue = True
exampleFalse = False

#the if statement will only run its code if its input is true

if exampleTrue:
    print("This prints because exampleTrue, the argument (input), is True")

if exampleFalse:
    print("This doesn't print because exampleFalse is False")

#the else statement runs its code if the if statement's argument is false

if exampleFalse:
    print("This doesn't print because exampleFalse is False")
else:
    print("This runs instead.")

if exampleTrue:
    print("This prints because exampleTrue is True")
else:
    print("This does not run")

#you can put another if,else statement inside the first else statement
alsoFalse = exampleFalse

if exampleFalse:
    print("This doesn't run")
else:
    if alsoFalse:
        print("This also doesn't run")
    else:
        print("This runs")

# in python there is a shorter way to do it called elif (else, if)

#this is the same thing as the previous if, else if, else
if exampleFalse:
    print("This doesn't run")
#elif = else if
elif alsoFalse:
    print("This also doesn't run")
else:
    print("This runs")

#you can do this as much as you want
if exampleFalse:
    print("This doesn't run")
elif alsoFalse:
    print("This also doesn't run")
elif alsoFalse:
    print("This also doesn't run")
elif alsoFalse:
    print("This also doesn't run")
elif alsoFalse:
    print("This also doesn't run")
elif alsoFalse:
    print("This also doesn't run")
else:
    print("This runs")

#else if else is very useful for different specified outputs for inputs

#like this

#takes an integer representing the day of the week and a boolean of whether it is a vacation day
#monday = 1, sunday = 7
def isThereSchool(day,vacation):
    #  >= is greaterthan or equal to, so if it is later in the week than saturday (6)
    # it will set school to false because it is the weekend 
    if(day >= 6):
        return False
    #if it is vacation there will be no school
    elif(vacation):
        return False
    else:
        return True

print("Saturday on Vacation, is there School? " + isThereSchool(6,True))
print("Monday not on Vacation, is there School? " + isThereSchool(1,False))

#the "or" operator returns true if any of its surrounding arguments are true
#and it returns false if both of the arguments are false



#you can simplify the noschool function using the "or operator"

def simpleSchool(day,vacation):
    #if it is the weekend or vacation it will return false because there is no school
    if(day >= 6 or vacation):
        return False
    else:
        return True

print("Saturday on Vacation, is there School? " + simpleSchool(6,True))
print("Monday not on Vacation, is there School? " + simpleSchool(1,False))

#you can simplify it even futher by only writing the if statement
def superSimpleSchool(day,vacation):
    #if it is the weekend or vacation it will return false because there is no school
    if(day >= 6 or vacation):
        #once the function returns, it doesn't run anything after so it's ok to do this
        return False
    return True

# the "and" operator checks if both the surrounding arguments are true, and if they are, it returns true

alsoTrue = exampleTrue

if exampleTrue and alsoTrue:
    print("This prints")
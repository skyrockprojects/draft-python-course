# write your own function that takes two numbers and subtracs them

# WRITE YOUR SUBTRACTION FUNCTION HERE (call it subtract)

# also write a function that prints out it's input twice

# WRITE YOUR FUNTION THAT PRINTS TWICE HERE (call it printTwice)

#you can also put a function as one of the inputs, try putting values into the subtract function and use it as an input for printTwice











# These are test cases we will learn about them next lesson
#DO NOT EDIT THIS
def checkOutput(index, value):
    if(output[index] == value):
        return "CORRECT!"
    return "WRONG, try again"

firstInput = [1,2,3,4,5]
secondInput = [-1,0,14,22,3]
output = [2,2,-11,-18,2]
for i in range(5):
    print(firstInput[i]," + ",secondInput[i]," = ",subtract(firstInput[i],secondInput[i])," ",checkOutput(i,subtract(firstInput[i],secondInput[i])))
for i in firstInput:
    printTwice(i)


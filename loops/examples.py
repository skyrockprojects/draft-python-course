#Basic for loop; Prints out the numbers from 0 to 10
for x in range(0,10):
    print(x, end=" ")
print("")
#Basic while loop; Stops when variable y reaches 10
y=0
while(y<10):
    print(y, end=" ")
    y+=1
print("")
#Basic foreach loop; Prints out what is inside a list
list = ["a","b","c",1,2,3]
for z in list:
    print(z, end=" ")
print("")
#Basic nested loop; Prints what is inse a 2D list
list_of_lists = [["a",'b','c'],[1,2,3]]
for l in list_of_lists:
    for a in l:
        print(a, end=" ")
    print("")


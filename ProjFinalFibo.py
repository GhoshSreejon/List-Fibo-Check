
print("\nHello! Welcome to my project. \n\n"+"The user needs to enter a list of numbers and this program \nwill find out whether they belong to the fibonacci series or not and \nsort and display two rows of elements which are valid and invalid respectively.")

# here the ( \n ) is known as the newline character, used to create a new line

l1=[]           #initialising list to store fibonacci series
a=0             #initialising the first member of fibonacci series
b=1             #initialising the second member of fibonacci series
l1.append(a)    #appending the first element of the fibonacci series
l1.append(b)    #appending the first element of the fibonacci series


for i in range(2,10**3,1):      #initialising a list of fibonacci series
    c=a+b
    a=b
    b=c
    l1.append(c)                #appending the rest of the elements of the fibonacci series


print()
print("Enter the numbers to be checked, separated by ',': ",end="")
l2=list(map(int,input().split(","))) #using map function to input elements in a list that are to be checked
n=len(l2)
l3=[]           #initialising list to store the elements that are valid
l4=[]           #initialising list to store the elements that are invalid


vld=0           #counter variable for the valid elements
invld=0         #counter variable for the invalid elements


for i in range(0,n,1):
    if(l2[i] in l1):
        l3.append(l2[i])
        vld+=1
    else:
        l4.append(l2[i])
        invld+=1
        

l3.sort()
l4.sort()       


print()
for i in range(0,vld,1):
    print(l3[i],end=" ")
if(vld>1):
    print("are valid")
elif(vld==1):
    print("is valid")


print()
for i in range(0,invld,1):
    print(l4[i],end=" ")
if(invld>1):
    print("are invalid")
elif(invld==1):
    print("is invalid")

print()
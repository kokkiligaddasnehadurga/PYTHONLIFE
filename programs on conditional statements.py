#programs based control statements
#control statments are of four types
#if 
#else
#elif
#nested if

n=int(input("enter a number:"))
age=n
if age>=18:
    print("you can vote")
else:
    print("wait")



#using elif:    
n=int(input("enter a number:"))
age=n
if age>18:
    print("you can vote")
elif age==18:
    print("you can vote")
else:
    print("wait")

    
#using nested if:
#nested if:it is used to write the condition in already existing condition
n=int(input("enter a number:"))
n1=int(input("enter a number:"))
a=n+n1
print(a)
if True:
    print("outer if")
    if True:
        print("if")
    else:
        print("i")
else:
    print("i")
    

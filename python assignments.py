

# To write a tables by using for loops concept 

# to writing a 9th table 


number=int(input())

for table in range(1,11):
    print(number," X ",table,"=",table*number)

print("----------------------------------------------------------")

# to write 11 table by using for loop

number_11=int(input())

for table_11th in range(1,11):
    print(number_11," X ",table_11th,"=",table_11th*number_11)

print("-------------------------------------------------------------------------")

# To write a 5 th table by using while loop 

loop_number=int(input("select a number: "))
counter=0
while counter <=10:
    print(loop_number," X ",counter , "=" , counter*loop_number)
    counter=counter+1


#conditional and relational operators 

gents=int(input())
ladies=int(input())

#by using if elif and else statement we can write code

if gents==ladies:
    print("Belongs to co-education college")
elif gents>ladies:
    print("Gents college")
elif gents<ladies:
    print("ladies college")
else:
    print("no colleges fro gents and ladies")


# To write a simple code based on no of workers in a shift

workers=(10,20,30,40,50,60,70,80,90,100)

for no_of_workers in workers:

    if no_of_workers>70:
        print("Workers belongd to afternoon shift")

    elif ((no_of_workers<=70) and (no_of_workers>30)):
        print("workers belongs to morning shift")

    else:
        print("workers belongs to night shift")


print("--------------------------------------------------------------------")

expression=input("enter the expression of +,-,*,/:")

number1=int(input("enter first number"))
number2=int(input("enter second number"))

if expression == "+":
    print(number1,expression,number2,"=",number1+number2)
elif expression == "-":
    print(number1,expression,number2,"=",number1-number2)

elif expression == "*":
    print(number1,expression,number2,"=",number1*number2)

elif expression == "/":
    print(number1,expression,number2,"=",number1/number2)

else:
    print("valid number")
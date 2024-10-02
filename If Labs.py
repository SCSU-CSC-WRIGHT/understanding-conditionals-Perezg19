# This is temperature check
temp_check = int(input("What is the current temperature in Celsius: "))
if (temp_check)>30:
    print("It's a hot day!")
else:
    print("The weather is cool.")

# This is number comparison
x = int(input("Please type in a number: "))
y = int(input("Please type in another number: "))
if (x>y):
    print(f"{x} is greater.")
elif (y>x):
    print(f"{y} is lower.")
else:
    print("These numbers are equal.")

# This is password checker
pword = "abc"
password = input("Please enter your password: ")
if (password==pword):
    print("Access granted.")
else:
    print("Access denied.")

# This is the simple calculator
x = int(input("Please type in a number: "))
y = int(input("Please type in another number: "))
op = input("Enter your operation: ")
if (op=='+'):
    print(x+y)
if (op=='-'):
    print(x-y)
if (op=='*'):
    print(x*y)
if (op=='/'):
    print(x/y)

# This is positive, negative, or zero
rand_num = float(input("Please enter a number: "))
if (rand_num==0):
    print("This number is zero.")
if (rand_num>0):
    print("This number is positive.")
if (rand_num<0):
    print("This number is negative.")

# This is day of the week
day = input("Please enter a number between 1 and 7: ")
if (day==1):
    print("It is Monday.")
elif (day==2):
    print("It is Tuesday.")
elif (day==3):
    print("It is Wednesday.")
elif (day==4):
    print("It is Thursday.")
elif (day==5):
    print("It is Friday.")
elif (day==6):
    print("It is Saturday.")
else:
    print("It is Sunday.")
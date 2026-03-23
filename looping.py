looping
for i in range(1,5,1):
    print("hello")
n=int(input("enter range from 1 to :"))
for i in range(1,n+1):
    print(i)
for i in range(1,11):
    print(i*7)
num=7
for i in range(1,11):
    print(i*num)
num=int(input("enter a number:"))
for i in range(1,11):
    print(num*i)
wap to print factors of number
12=> 1,2,3,4,6,12
count=0
num=int(input("enter number:"))
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count = count+1
        print("total factors:",count)
        
count=0
num=int(input("enter number:"))
for i in range(1,num+1):
    if num%i==0:
        print(i)
        count = count+1
        print("total factors:",count)
        if count==2:
            print("prime")
        else:
             print("not prime")
               
for i in range(1,6):
    if i==4:
        break
    print(i) output 1,2,3
    for i in range(1,6,2):
    print(i)
    if i==4:
        break output1,2,3,4
    for i in range(1,6):
    print(i)
    if i==4:
        continue#1,2,3,4,5
    for i in range(1,6):
    print(i)
    if i==4:
        pass
    for i in range(1,6):
    print(i)
    if i==6:
        break
else:
    print(0)
    
    Q51. Calculate INCOME TAX

sal = float( input("Enter Salary : ") )
if sal<500000:
    print("No Tax Liablity")
elif sal<700000:
    print("Tax :",sal*0.05)
elif sal<1000000:
    print("Tax :",sal*0.10)
else:
    print("Tax :",sal*0.15)
Q52. ATM withdrawl Program

balance = 32000
w = float(input("Enter Amount Withdrawl : "))
if w<=balance:
    print("Collect The Money")
    balance=balance-w
    print("Current Balance :",balance)
else:
    print("Insufficient Balance")
    print("Current Balance :",balance)
# WAP to find sum of all natural numbers.
    1 to N

n = int(input("Enter Range From 1 to : "))
add = 0
for i in range(1,n+1):
    add=add+i

print(add)

n = int(input("Enter Range From 1 to : "))

print( "Total :", n*(n+1)/2 )
Find Factorial
    !5  =>  5*4*3*2*1  => 120

add = 1
num = int(input("Enter A Number : "))
for i in range(1,num+1):
    add = add*i

print("factorial :",add)




        

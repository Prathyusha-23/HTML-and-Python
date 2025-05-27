a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
#Arithmetic operations
print("Addition",a+b)
print("subtraction",a-b)
print("Multiplication",a*b)
print("Division",a/b)
print("Modulo division",a%b)
#Relational or comparison
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
#Logical operators
print(a and b)
print(a or b)
print(not b)
print(not a)
#Bitwise operators
print(a & b)
print( a|b)
print(a^b)#XOR
print(~a)#not
print(a>>b)#right shift
print(a<<1)#left shift
#Identity operators
c=a
print(a is b)
print(a is not b)
#Membership operators
d=[10,20,30]
e=[56,30,23]
print( d in e)
print(d not in e)
print(10 in d)
#The rectangle
print("Area of rectangle:",a*b)
print("Perimeter of rectangle:",(2*(a+b)))
#power of a number
print(a**b)
#conditional statements
year=int(input("enter the year:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print(year,"leap year")
else:
    print(year,"not leap year")

#Marks grading
a=int(input("Enter your marks:"))
if(a in range(91,100)):
    print("Grade O")
elif(a in range(81,90)):
    print("Grade A")
elif(a in range(71,80)):
    print("Grade B")
elif(a in range(61,70)):
    print("Grade C")
elif(a in range(46,60)):
    print("Grade D")
elif(a in range(34,45)):
    print("Grade E")
else:
    print("FAILED")

#Biggest of three numbers
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:")) 
if(a>b and a>c):
      print(a,"is largest")
elif(b>c):
    print(b,"is largest")
elif(a==b and a==c):
    print("all are equal")
elif(a==b or a==c):
    print("both are equal,highest is",c)
else:
    print(c,"is largest")

#Electricty bill
a=int(input("enter the no.of units:"))
b=120
if(a<=50):
    print(120)
elif(a>50 and a<=100):
    print(((a-50)*2.89)+b)
elif(a>100 and a<=150):
    print(120+(100-50)*2.89+(a-100)*3.83)
elif(a>150 and a<=200):
    print(120+(100-50)*2.89+(150-100)*3.83+(a-150)*4.56)
elif(a>200 and a<=300):
    print(120+(100-50)*2.89+(150-100)*3.83+(200-150)*4.56+(a-200)*5.34)
elif(a>300 and a<=400):
    print(120+(100-50)*2.89+(150-100)*3.83+(200-150)*4.56+(300-200)*5.34+(a-300)*5.99)
elif(a>400 and a<=500):
    print(120+(100-50)*2.89+(150-100)*3.83+(200-150)*4.56+(300-200)*5.34+(400-300)*5.99+(a-400)*6.89)
elif(a>500 and a<=750):
    print(120+(100-50)*2.89+(150-100)*3.83+(200-150)*4.56+(300-200)*5.34+(400-300)*5.99+(500-400)*6.89+(a-500)*7.56)
else:
    print(120+(100-50)*2.89+(150-100)*3.83+(200-150)*4.56+(300-200)*5.34+(400-300)*5.99+(500-400)*6.89+(750-500)*7.56+(u-750)*8.73)

a=float(input("Enter the number:"))
b=float(input("Enter the number:"))
c=input("please select +,-,*,/,%:")
if(c=='+'):
    print("addition:",a+b)
elif(c=='-'):
    print("subtraction:",a-b)
elif(c=='*'):
    print("multiplication:",a*b)
elif(c=='/'):
    if b!=0:
      print("division:",a/b)
    else:
        print("Division not possible")
elif(c=='%'):
    print("Modulo division:",a%b)
else:
    print("Invalid operator")


#Triangles
a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))
if((a+b)>c and (a+c)>b and (b+c)>a):
    print("This is triangle")
    if(a==b and a==c):
        print("This is Equilateral")
    elif(a==b or a==c or b==c):
        print("This is Isoseleus")
    else:
        print("scalen")
else:
    print("Not a triangle")


#vote eligibility
a=int(input("enter your age correctly:"))
if(a<18):
    print("you are a kid go and play")
else:
    print("you are eligible for vote")


#ATM withdraw
amount=int(input("enter the amount you want:"))
balance=8000
if(amount<balance):
    print("Amount remain:",balance-amount)
else:
    print("Insufficient balance")
   

#Ternnary operators
a=10
b=20
value=a if a>b else b
print("Max value",value)

#basics
a='welcome to qis wollege'
print(a.find('z'))
print(a.rfind('e'))#printing the highest value
print(a.index('c'))
print(a.rindex('q'))
print(a.count('e'))
print(a.count('come'))#check whether the series is present in the same order
b=a.replace('wel','')
print(b)
print(a.replace('wel',''))#only that particular statement
print(a.replace('w','t',1))#1 is count
print(a.split())
print(a.split(':'))
c='battula@gmail.com'
d=c.split('@')
print(d[1])
s1="abc"
s2="123"
print(s1.join(s2))
#password checker"
n=input("enter password:")
a=False
b=False
c=False
if len(n)<=8:
    print("password invalid")
else:
    for i in (n):
       if  i.islower():
           a=True
       if i.isupper():
           b=True
       if i.isdigit():
            c=True
    if a and b and c:
            print("strong")
    else:
        print("weak")
for i in range(1,11,1):
    print("prathyusha")


n=int(input("enter number"))
for i in range(10,1,-1):
    print(i)

#even numbers
n=int(input("enter number"))
for i in range(2,n+1,2):
    print(i)

#odd numbers
n=int(input("enter number"))
for i in range(1,n,2):
    print(i)

#sum of even numbers
n=int(input("enter number"))
for i in range(1,n,2):
    print(i)

#sum of odd numbers
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    if i%2!=0:
        sum+=i
print(sum)

#sum of squares
n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    if i%2!=0:
        sum+=(i*i)
print(sum)

#Right angle triangle using *
n=int(input("enter the number:"))
for i in range(1,n+1):
     print('*'*i)

#reverse the triangle
n=int(input("enter the number:"))
for i in range(n,0,-1):
     print('*'*i)

#triangle form
n=int(input("enter the number:"))
for i in range(n):
     print(' '*(n-i-1)+'*'*(2*i+1))

#square pattern
n=int(input("enter the number:"))
for i in range(n):
     print('*'*(n-i)+'*'*(1*i))

#square with spaces(hallow square)
n=int(input("enter the number:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#triangle using  nested for loops
n=int(input("enter the number:"))
for i in range(n):
     print(' '*(n-i-1)+'*'*(2*i+1))

#reverse a pyramid using nested for loop
n=int(input("enter the number:"))
for i in range(n):
    for j in range(i):
         print(' ',end=' ')
    for k in range(2*(n-i)-1):
         print('*',end=' ')
    print()

#triangle with numbers
n=int(input("enter the number:"))
num=1
for i in range(n+1):
    for j in range(i):
       print(num,end=' ')
       num=num+1
    print()

#numbers using while loop
n=int(input("enter the number:"))
i=1
while(i<n):
    i+=1
    print(i)

#sum of each number in a number
n=int(input("enter the number:"))
sum=0
while n>0:
    r=n%10
    sum+=r
    n=n//10
print(sum)
    
#power of number
n=int(input("enter the number:"))
p=int(input("enter the power value:"))
if n>0:
    print(n**p)
    
#power without using power method
base=int(input("enter the number:"))
expo=int(input("enter the power value:"))
k=1
p=1
while k<=expo:
    p=p*base
    k+=1
print(p)

#reverse the given number
n=int(input("Enter the string:"))
sum=0
while n>0:
    digit=n%10
    sum=(sum*10)+digit
    n//=10
print(sum)

#count the digits in a given string
n=int(input("Enter the string:"))
count=0
while n>0:
    count+=1
    n//=10
print(count) 
#name
a=input("start")
b=input("end")
c=a.capitalize()
d=b.capitalize()
print(c," ",d)

c=['soda','chintu','hari']
c.append('m1')
print(c) 
c.extend(['1','2','3']    )
print(c)
for i  in range(1,7):
    n=input("enter:")
    c.append(n)
print(c)
print(c[9])
#remove function is used to eliminate a specific value present in the list
#del function is used to eliminate a value at a specified index position
x=[1,2,3,4,5]
x.extend([6,7,8,9])
print(x)
x.sort()
print(x)
print(sorted(x))
print(x.count('3'))
print(max(x))
print(min(x))
print(sum(x))
#extend() is used to add a list of values to the already existing list
#sort() is used to sort the elements in ascending order
#sorted() is same as sort() but we use print statement directly here
#count() is used to find the value repeated in the list
#min() is used to find the minimum value in the list
#max() is used to find the maximum value in the list
#sum() is used to find the sum of all elements in the list
x.insert(4,10)
print(x)
#list comprehensions
l=[f"{i}-even" if i%2==0  else f"{i}-odd" for i  in range(1,50)]
print(l)
l=[f"{i}-{i*i}" for i  in range(1,50)]
print(l)
l=[sum((i*i) for i  in range(1,50))]
print(l)
fib=[0,1]
l=[fib.append(fib[-1]+fib[-2] ) for i in range(2,50)]
print(fib)

#write a python program which prints the factorial of a given number using function
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
#method2 for factorial
def factorial(n):
    r=1
    for i in range(1,n+1):
        r*=i
    return r
print(factorial(5))
#memory management in python: stack-variables are stored,heap-values are stored . The values are not assigned to variables .
#stack will be maintained by python interpreter and heap is maintained by garbage collector.
#default parameter of method is self
#doc string: .__doc__(It is used for multi line comment lines)
#userdefined functions:anonomus,recursive,doc functions
#python program to define a particular function with the following rules
def sub(a,b):
    print(a-b)
print(sub(10,20))
def add(a,b):
    return a+b
print(add(10,20))
def mul():
    return a*b
a=int(input())
b=int(input())
print(mul())
def mul():
    print(a*b)
a=int(input())
b=int(input())
print(mul())
#counting lower and uppercase in string
s=input("enter:")
l=0
u=0
for i in s:
    if i.islower():
        l+=1
    if i.isupper():
        u+=1
print(l,u)'''
#list
'''l=list(map(int,input().split(" ")))
v=[]
s=[]
for i in l:
    a=1
    b=0
    for j in range(len(l)):
        if l[j]==i:
            continue
        else:
            a*=l[j]
            b+=l[j]
    v.append(a)
    s.append(b)
print(v)
print(s)

c=65
for i in range(1,6):
    for j in range(1,i+1):
        print(chr(c),end=" ")
    c+=1
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    i+=1
    print()
def prime(n):
    count=0
    if n>1:
        for i in range(1,n+1):
            if n%i==0:
                count+=1
            if count==2:
                return True
            else:
                return False
for i in range(51):
    if prime(i):print(i,end=",")
#with return and without parameters
def add():
    a=int(input())
    b=int(input())
    c=a+b
    return c
print(add())
#with return with parameters
def add(a,b):
    return a+b
a=int(input())
b=int(input())
print(add(a,b))
#without return and without parameters
def add():
    a,b=10,20
    print(a+b)
add()
#without return and with parameters
def add(a,b):
    print(a+b)
add(10,20)
#memory management in python
#There are 4 segments:1.code segment 2.static segment 3.stack 4.Heap
#In code there are 2:code editor
#identifiers are stored in stack,values stored in heap
#docstring is used to print comments which are present inside function
def add(a,b):
    '''This is a function'''
    return a+b
print(add(10,20))
print(add.__doc__)
#Types of arguments: required,keyword,default,variable length,keyword length
#required or positional-no.of parameters equal to no.of arguments
#keyword-The values which are passed to parameters in function calling
#keword argument example
def add(a,b):
    print(a+b)
add(b=10,a=20)
#default-the values which are passed the parameters in function definition
def add(a=10,b=30):
    print(a+b)
add()
#variable length-multiple arguments for a single parameter
def add(b,*a):
    print(b)
    print(a)
add("prathyusha")
add(10,20,30)
add(90)
#keyword length-we will pass multiple key-value pairs
def add(**a):
    for i in a:
        print(i)
add(a=10,b=20,c=30)
def add(a,b=10,*c,**d):
    print(a)
    print(b,c,d)
#add("QIS")
#add(10)
#add(1,2,3,4)
add(a=10,b=20,c=89,d=45)
a=int(input())
sum=0
while a>0:
    r=a%10
    sum+=r
    a//=10
    if len(sum)==1:
        print(sum)
    else:
        continue
#sum of numbers in list
#multiply all in list
#reverse a string
#factorial
#number falls in given range
#There are total 6 types of functions: predefined,userdefined,lambda,fruitful,void,recursive
#fruitful-These are some of the builtin functions which returns a value to a variable
import math
x=math.sqrt(8)
print(x)
#void-A function which doesn't return anything-types(with and without parameters)
def fun():
    print("Hello world")
fun()
def fun(a):
    a="Hello world"
    print(a)
fun(" ")
#lamdba-also known as anonymous functions,it is a function without predefined name
#syntax:lambda parameters:expression
x=lambda a:a
print(x("hello"))
x=lambda a,b:a+b
print(x(10,20))
x=lambda *a:a
print(x(10,20,30))
#FILTER METHOD
x=[i for i in range(1,101)]
print(list(filter(lambda i:i%2==0,x)))
#map
x=[i for i in range(1,101)]
print(list(map(lambda i:i**2,x)))
#local and global
x=10
def a():
    global a
    a=20
    print(a)
a()
print(a)
#when base case is not there in recursion then it goes to infinite loop
#recursion
def sum(a,b):
    if b==0:
        return a
    else:
        return sum(a+1,b-1)
print(sum(10,20))
#palindrome
n=121
t=n
rev=0
while n>0:
    rev=rev*10+n%10
    n//=10
print(rev)
if rev==t: print("p")
else: print("n")
#sum of n natural numbers using recursion
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n+fact(n-1)
print(fact(5))
#recursive or nested iteration functions
#advantages-time,space complexity,backtracking
#factorial4
n=int(input())
fact=0
if n==0 or n==1:
    print( "1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
#compound interest
compound_interest=principal_amount*(1+interest_rate/100)**number_of_years-principal_amount
#armstrong number
n=int(input())
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if n==sum:
    print("armstrong")
else:
    print("not armstrong")
#prime number in an interval
n=int(input())
flag=False10 
if n>1:
    for i in range(2,n):
        if n%i==0:
            flag=True
            break
if flag:
    print("not prime")
else:
    print("prime")
#prime within range
l=2
u=100
count=0
for n in range(l,u+1):
    if n>1:
        for i in r1ange(2,n):
            if n%i==0:
                break
        else:
            print(n)
            count+=1
print(count)
#sum of the numbers in the givn number 1234=10
n=int(input("enter the number:"))
sum=0
while n>0:
    r=n%10
    sum+=r
if(sum==n):
    print(sum)
#Palindrome number
n=int(input("Enter the string:"))
a=n
sum=0
while a>0:
    digit=a%10
    sum=(sum*10)+digit
    a//=10
if(n==sum):
   print("palindrome")
else:
   print("Not palindrome")
#fibonacci
n = 4
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
a=int(input())
while a>=10:
    sum=0
    while a>0:
        r=a%10
        sum+=r
        a//=10
    a=sum
print(sum)
a=input().split(" ")
sum=1
for i in a:
    sum*=int(i)
print(sum)
#reverse a string
s="prathyusha"
b=' '
for i in s:
    b=i+b
print(b)
n=int(input())
fact=1
if n==0 or n==1:
    print("1") 
else:
    for i in range(2,n+1):
        fact=fact*i
    print(fact)
n=int(input())
if n//2*2==n:
    print("even")
else:
    print("odd")
for i in range(1,51):
    print(i**3)
a=input()
b=ord(a)
print(b)
a=[1,2,3,4]
max=a[0]
for i in range(1,len(a)):
    if a[i]>max:
        max=a[i]
print(max)
a=[1,2,3]
temp = a[0]
a[0] = a[2]
a[2] = temp
print(a)
#transpose of a matrix
m=[[1,2],[3,4],[5,6]]
for k in m:
    print(k)
l=[[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
for k in l:
    print(k)
n=4
l=[[0 for i in range(n)] for j in range(n)]
print(l)
import phonenumbers
from phonenumbers import geocoder
p1=phonenumbers.parse("+917702407377")
p2=phonenumbers.parse("+919515023599")
p3=phonenumbers.parse("+919573677977")
print(geocoder.description_for_number(p1,"en"));
print(geocoder.description_for_number(p2,"en"));
print(geocoder.description_for_number(p3,"en"));
#patterns-square pattern
a=int(input())
for i in range(a):
    print('*'*a)
a=int(input())
for i in range(a):
    print('*'*(i+1))
a=int(input())
for i in range(a):
    b=a-i
    print('*'*b)
n=4
a=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(a,end=" ")
    a+=1
    print()
#prime number
import math
start=int(input("enter start:"))
end=int(input("enter end:"))
for i in range(start,end):
    if i<=1:
        print("Not prime")
    else:
        a=(math.factorial(i-1)+1)%i==0
        if a:
            print(i," is Prime")
        else:
            print(i," is Not prime")

#prime method-2
import math
start=2
end=100
count=0
for num in range(start,end+1):
    if(num>1):
        prime=True
    for i in range(2,int(math.sqrt(num)+1)):
        if num%i==0:
            prime=False
            break
    if prime:
        count+=1
        print(num,"prime number")
print("count",count)


#stings nearly 21 functions
str="qiscet"
print(len(str))
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.casefold())
print(str.count('q'))
print(str.isalpha())
a="i am going to college"
print(a.title())
print(a.replace('going','went'))
print(a.startswith('i'))
print(a.endswith('i'))
print(a.find('g'))
print(a.index('c'))
b="python"
#nythop
print(b[::1])
print(b[-1],b[:-1],b[0])
print(a.lstrip())#used to remove space in left side
print(a.rstrip())#used to remove space in right side
print(a.isspace())#return boolean whether space is there or not in the starting
c="123"
print(c.isdigit())#boolean value
print(c.isalpha())
print(c.isnumeric())
print(c.isalnum())
#Bitwise AND-only 1 when both are 1's
#Bitwise OR-only 0 when both are 0's
#Bitwise XOR-same then 0 different then 1
#Bitwise NOT-opposite to XOR operation
f=5
print(~f)
print(f<<2)
print(f>>2)

#Types of algorithms
1.sorting
2.searching
3.Recursive
4.Graph
5.Dynamic
6.greedy
7.backtracking

#strong number-The sum of factorials of digits are equal to the original number is called strong number
n=int(input("Enter the number:"))
sum=0
a=n
while n>0:
     digit=n%10
     fact=1
     for i in range(1,digit+1):
        fact=fact*i
     sum+=fact
     n=n//10
if sum==a:
    print("strong number")
else:
    print("not strong")


#count no.of letters in a given string
a=input("enter the string:")
l1=[]
print(a.lower())
for i in a:
     if i in a:
          if i not in l1:
            print(i,a.count(i))
            l1.append(i)    


#Remove a character based on index
a=input("Enter the string:")
b=int(input("Enter index value:"))
l=len(a)
if b>=0 and b<1:
     print(a[:b]+a[b+1:])
     #print(a.replace(a[b],""))
else:
     print("num should be positive")

List: Collection of different datatypes/items
mutable 
ordered 
indexed 
duplicates are allowed

operations basic:
1.index...slicing
3.concat...repetition
5.updated...comparision
7.membership


#l=["monday","list",80,4.9]
s=input("enter").split()
print(s)
l1=[]
for i in range(len(s):
     s[i]=int(s[i])
print(s)

s=int(input("enter"))
l1=[]
for i in range(s):
     a=int(input("enter:"))
     l1.append(a)
print(l1)

#comprehension 4 steps
#variable=[expression loop condition]
l1=[int(input()) for i in range(1,4)]
print(l1)

n=int(input("enter:"))
l1=[int(input()) for i in range(1,n)]
print(l1)
s="123456"
l1=[int(i) for i in s]
print(l1)

l1=[int(i) for i in input("enter:").split(" ")]
print(l1)

l1=[i for i in range(1,10) if i%2==0]
print(l1)

l1=["positive" if int(i)>0 else "negative" for i in input("enter:").split(" ")]
print(l1)

l1=list(map(int,input('enter:').split(" ")))
print(l1)

l1,l2=list(map(int,input('enter:').split(" ")))
print(l1,l2)

l1=[int(i) for i in input("enter:").split(" ")]
l2=[int(i) for i in input("enter:").split(" ")]
print(l1+l2)
print(l1 in l2)
print(l1*4)
print(l1*len(l2))
print(l1 ==l2)

l1=["goodmorning",["python","c"]]
l1[1][0]="c"
l1[1][1]="python"
print(l1)

#Built in methods of list():
len(),append(), extend(),sum(),max(),min(),copy(),sort(),find(),index(),count()
remove->It uses values
pop->Default it removes last value or we can pop by index

l1=[i for i in input("enter:").split(" ")]
l1.sort(key=None,reverse=True)
print(l1)

l1=[i for i in input("enter:").split(" ")]
l2=[i for i in input("enter:").split(" ")]
l3=[]
if len(l1)==len(l2):
    for i in range(len(l1)):
       a=abs(l1[i]-l2[i])
       l3.append(a)
        
    print(l3)
else:
    print("Tke the list as same siz")

#Function-A block of organized,reusable code designed to perform a specific task.
def sub():
   print("hello")
   print("good morning")
sub()
def soda():
    'return the statement'
    return "prathyusha"
print(soda())
#only one return statement
#comments are called as doc strings(.__doc__)
print(soda.__doc__)
#parameters->function starting
#arguments->function ending
#arguments may not be equal to parameters and position is important

def sub(d,c):
    print(d-c)
a=int(input())
b=int(input())
sub(d=a,c=b)
sub(c=a,d=b)
#Default Arguments
def sub(d,c=100):
    print(d-c)
a=int(input())
b=int(input())
sub(a)
#Anonymous functions(nameless or lambda functions)
#arguments no limit,expression should be 1
#variable=lambda arguments:expression
 #print(variable(arguments))
def sum():
    a=n*(n+1)
    print(a)
n=int(input("enter number:"))
sum()

def fact():
    f=1
    if n==0 or n==1:
        return 1
    else:
        for i in range(1,n+1):
            f=f*i
        print(f)
n=int(input("enter number:"))
fact()

s=lambda a,b,c:a+b
a,b,c=1,2,3
print(s(a,b,c))
print(s(10,20,30))

s=input("enter:")
c=input("enter:")
s2=""
if c in s:
    for i in s:
        if i!=c:
            s2=s2+i
    print(s2)

#Tuples
operations:index,slicing,concat,repetition,membership,comparision,del()
#Dictionaries
d={1:10,2:20,3:30}
print(d.keys())
d1={"a":100,500:200,"c":300}
print(d1.values())
print(sorted(d.items()))
for i,j in sorted(d.items()):
    print(i,j)
#methods: get(),pop(),update(),clear(),len(),copy()
a=input("keys:").split(" ")
b=input("values:").split(" ")
d=dict(zip(a,b))
print(d)
print(sorted(d.items()))
for i,j in sorted(d.items()):
      print(i,j)

a=input("keys:").split(" ")
b=input("values:").split(" ")
d={}
for i in range(len(b)):
    d[a[i]]=b[i]
    print(sorted(d.items()))
print(d)

#set:unique,unordered(no index,no slicing) collection of same items,no duplicates
It wont take list,tuple,dict datatypes as elements in it
methods:add()-for single elements
update-for group of elements by creaing a list
discard-no changes in set ,remove-raise an error
#Mathematical operations
Union-combines all elements and remove duplicates-'|' or .union()
Intersection-used to take common elements from set-'&' or .intersection(),s1&=s2
Difference-returns new set that contains elements from set1- '-' or .difference()or .difference_update() or-=
Symmetric difference-.symmetric_difference() or '^' or .symmetric_difference_update(),^=
Functions:len(),copy(),clear(),isdisjoint(),issubset()
#Recursion-2 criteria:base case and recursive case
#factorial using recursion
def s(n):
    if n==1:
        return 1
    else:
        return n*s(n-1)
n=int(input("enter"))
print(s(n))
#palindrome using recursion
def s(n):
    k=len(n)
    if k<=1:
        return 1
    else:
        if n[0]==n[-1]:
            return s(n[1:-1])
        else:
            return 0
n=input("enter")
r=s(n)
if r==0:
    print("not palindrome")
else:
    print("palindrome")

OOPS:
keyword classname:
  constructor (optional)
     statements
  ----------
  methods or functions:(input)
     statements
     -----
  method 2:(output)
    statements
    ----------
object creation()---->instance of the class
calling input methods using object
calling output methods using object
#OOPS with constructor
class Employee:
    def __init__(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def output(self):
        print("name:",self.name,"id:",self.id,"salary:",self.salary)
x=Employee("rani",306,57000)
x.output()
y=Employee("harika",67,56000)
y.output()
a=input("name:")
b=int(input("id:"))
c=int(input("salary:"))
z=Employee(a,b,c)
z.output()

#OOPS without constructor
class Employee:
    def details(self,name,id,salary):
        self.name=name
        self.id=id
        self.salary=salary
    def output(self):
        print("name:",self.name,"id:",self.id,"salary:",self.salary)
x=Employee()
x.details("rani",306,57000)
print("details:",x.output())

class Employee:
    pass
y=Employee()
y.b=200
print(y.b)
#Inheritence:
1.base class
2.child(derived class)
Types of inheritance:single,multiple,multilevel,hierarchical
#single inheritance
class parent:
    def f1(self):
        print("hi")
    def f2(self):
        print("hello")
class child(parent):
    def f3(self):
        print("good morning")
v=child()
v.f3()
v.f2()
v.f1()
#Method overriding-having same method names in the different classes.
#polymorphism
class shape:
    def area(self):
        print("you cn find the area of different shapes")
class square(shape):
    def __init__(self,a):
        self.a=a
    def area(self):
        print("square",self.a*self.a)
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("rectangle:",self.l*self.b)
class circle(shape):
    def __init__(self,r):
        self.r=r
    def area(self):
        print("circle:",3.14*self.r*self.r)
v=[shape(),square(4),rectangle(10,20),circle(5)]
for i in v:
    i.area()
l=input("enter").split(" ")
a=list(map(int,l))
a.sort()
print(a)
a.reverse()
print(a)
s=input("enter:").split(" ")
l1=[int(i) for i in s]
for i in l1:
    if i==0:
        a=l1.remove(i)
        l1.append(a)
print(l1)
matrix:directly getting from the user
l1=[[1,2,3],[4,5,6],[7,8,9]]
for i in l1:
    print(i)
n=int(input("size of the matrix"))
r,c=list(map(int,input("enter:").split(" ")))
l1=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(1)
    l1.append(a)
print(l1)
for i in r:
    for j in c:
        print(l1[j][i],end=" ")
    print(i)
r,c=list(map(int,input("enter:").split(" ")))
l1=[[i+j for j in range(c)] for i in range(r)]
print(l1)
r,c=list(map(int,input("enter:").split(" ")))
l1=[]
for i in range(r):
    a=[]
    for j in range(c):
        if i==j:
            a.append(1)
        else:
            a.append(0)
        
    l1.append(a)
for i in range(r):
    for j in range(c):
        print(l1[i][j],end=" ")
    print()
r,c=list(map(int,input("enter:").split(" ")))
m1=[]
for i in range(r):
    v=[]
    a=list(map(int,input("enter:").split(" ")))
    if len(a)==c:
        v.append(a)
        m1.append(v)
print(m1)
n=int(input("enter:"))
if n%2!=0:
    l1=[[1 if i==2 or j==n-i else 0 for j in range(n)]for i in range(n)]
for i in range(n):
    for j in range(n):
        print(l1[i][j],end=" ")
    print()
s=input("enter")
a=s.find('@')
b=s.find('.')
print(s[a+1:b])
s=input("enter:")
s.islower()
if s.isalpha():
    print("panagram")
else:
    print("not panagram")

s=input("enter:")
c=0
a="abcdeghijklmnopqrstuvwxyz"
for i in s:
    for j in s:
        if s in a:
            c=c+1
if c==26:
    print("anagram")
else:
    print("not anagram")
a=input("enter:")
b=input("enter:")
if sorted(a)==sorted(b):
        print("anagram")
else:
    print("not anagram")
a=input("enter:")
b=a.count('-')
s=""
for i in a:
    if i!='-':
       s=s+i
print(b*'-'+s)
#password locker
a=input("enter:")
b=a[0]
d=0
c=0
sp=0
if len(a)>=4 and not a.isalpha():
    for i in range(len(a)):
        if a[i].isdigit():
            d=d+1
        if a[i].isupper():
            c=c+1
        if a[i]=="/" or a[i]==" ":
            sp=sp+1
        if c>=1 and d>=1 and sp==0:
            print("valid")
    else:
        print("not valid")
#pattern-structure or format which differentiate shapes
#types-alphabetical,mathematical shapes patterns(pyramid,floyds,pascal,hollow..)
#structure of pattern
j=  0 1 2 3
i=0 * * * *(0,0)(0,1)(0,2)(0,3)
  1 * * * *(1,0)(1,1)....
  2 * * * *
  3 * * * *
#i is for horizontal lines(rows), j is for vertical lines(columns)
n=5
for i in range(1,n+1):
    print('A'*n)
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or j==0 or j==n-1:
            print("A",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("D",end=" ")
        else:
            print(' ',end=" ")
    print()
for i in range(1,n+1):
    print('A'*n)
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n//2 or j==0 or j==n-1 or i==n-1:
            print("B",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0:
            print("C",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or i==n//2:
            print("E",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0  or j==0 or i==n//2:
            print("F",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (j==n-1 and i>=n//2) or (i==n//2 and j>=n//2):
            print("G",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if j==n-1  or j==0 or i==n//2:
            print("H",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if i==n-1  or j==n//2 or i==0:
            print("I",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if j==n//2 or i==0 or (j==0 and i>=n//2) or (i==n-1 and j<=n//2):
            print("J",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or i==n-1 :
            print("L",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==0 or j==n//2:
            print("M",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==j:
            print("N",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n//2 or (j==n-1 and i<=n//2):
            print("P",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n-1 or j==n-1 or (i>=n//2 and i==j):
            print("Q",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i==n//2 or (j==n-1 and i<=n//2) or (i==j and i>=n//2):
            print("R",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if i==n-1 or i==0 or i==n//2 or (i<=n//2 and j==0) or (j==n-1 and i>=n//2) :
            print("S",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2  :
            print("T",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n-1  :
            print("U",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n-1 or j==n//2 :
            print("W",end=" ")
        else:
            print(' ',end=" ")
    print()
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or (i==n-1 and i==j) :
            print("W",end=" ")
        else:
            print(' ',end=" ")
    print()

from turtle import *
from colorsys import *
speed(0)
bgcolor("black")
h=0
for i in range(75):
    color(hsv_to_rgb(h,1,1))
    h+=0.014
    left(1)
    forward(1)
    for j in range(2):
        left(2)
        circle(140)
    hideturtle()
done()
n=5
for i in range(n):
    for j in range(n):
        if i==j or j==n-i-1:
            print("X",end=" ")
        else:print(" ",end=" ")
    print()
#if we want to decrease the j values then use n-i-1
#H.W- madam using hour
n=5
for i in range(n):
    for j in range(n):
        if (i==j and i<=n//2) or (j==n-i-1 and i<=n//2) or (j==n//2 and i>=n//2):
            print("Y",end=" ")
        else:print(" ",end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):
        if j==0 or j==n-i-1:
            print("V",end=" ")
        else:print(" ",end=" ")
    print()
n=5
for i in range(n):
    for j in range(n):
        if j==(n//2-1) or (j==n-i-1 and i<=n//2) or (i==j and j>=n//2):
            print("X",end=" ")
        else:print(" ",end=" ")
    print()
#ord-prints the ASCII value of character, chr-prints character when ASCII is give 
n=5
c=0
for i in range(n):
    for j in range(n):
        if j==(n//2-1) or (j==n-i-1 and i<=n//2) or (i==j and j>=n//2):
            print(c,end=" ")
            c+=1
        else:print(" ",end=" ")
    print()
n=5
c=0
for i in range(n):
    for j in range(n):
        if j==(n//2-1) or (j==n-i-1 and i<=n//2) or (i==j and j>=n//2):
            print(chr(c),end=" ")
            c+=1
        else:print(" ",end=" ")
    print()
#mathematical patterns
n=5
c=1
for i in range(n):
    for j in range(n):
            print(c,end=" ")
            c+=1
    print()
n=5
c=1
for i in range(n):
    for j in range(n):
            print(j,end=" ")
            c+=1
    print()
n=5
c=1
for i in range(n):
    for j in range(n):
            print(i,end=" ")
            c+=1
    print()
n=5
c=1
for i in range(n):
    for j in range(n):
            print(i+j,end=" ")
            c+=1
    print()
n=5
c=65
for i in range(n):
    c=65
    for j in range(n):
            print(chr(c),end=" ")
            c+=1
    print()
n=5
c='A'
for i in range(n):
    for j in range(n):
        print(ord(c),end=" ")
        c=chr(ord(c)+1)
    print()
n=5
s="MADAM"
for i in range(n):
    for j in range(n):
            if i==0 or i==n-1 or i==j or i==n-j-1:
                print(s[j],end=" ")
            else:print(" ",end=" ")
    print()
n=5
c=0
for i in range(n):
    c=0
    for j in range(n):
            print(i,end=" ")
            c+=1
    print()
n = 5
s = "IAMASTUDENTOFQISCAVE"
index = 0

for i in range(n):
    for j in range(n):
        # First row: print first 5 letters of string s
        if i == 0 and j <= 4:
            print(s[index], end=" ")
            index += 1
        # First diagonal: print next 5 letters of string s
        elif i == j and j <= 4:
            print(s[index], end=" ")
            index += 1
        # Second diagonal: print next 5 letters of string s
        elif i + j == n - 1 and j <= 4:
            print(s[index], end=" ")
            index += 1
        else:
            print(" ", end=" ")
    print()
n=9
for i in range(n):
    for j in range(n):
        if j==n//2 or i==n-1 or (i<=n//2 and j==n-i-(n//2) and i!=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#mathematical shapes problem
n=5
for i in range(n):
    for j in range(n):
        print(n*j*i,end=" ")
    print()
n=5
for i in range(n):
    c=6
    for j in range(n):
        print(c,end=" ")
        c+=1
    print()
n=5
c=6
for i in range(n):
    for j in range(n):
        print(c,end=" ")
    c+=1
    print()
n=5
for i in range(n):
    c=65
    for j in range(n):
        print(chr(c),end=" ")
        c+=1
    print()
#Left side right angled triangle
n=10
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
n=5
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()

n=5
for i in range(n):
    for j in range(n-i):
        print("*"*j,end=" ")
    print("/")
#right side right angled triangle
n=5
c=97
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for k in range(i+1):
        print(chr(c),end=" ")
        c+=1
    print()
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for k in range(n-i):
        print(chr(c),end=" ")
        c+=1
    print()
#Butterfly triangle
n=10
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    for k in range(i+1):
        print(" ",end=" ")
    for j in range(i+2):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    for j in range(n-i-1):
        print(' ',end=" ")
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(n-i-1):
        print("*",end=" ")
    for j in range(i+1):
        print(' ',end=" ")
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(n-i-1):
        print("*",end=" ")
    print()
#Triangle
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
#inverse triangle
n=5
for i in range(n):
    for j in range(i):
        print(" ",end="")
    for j in range(n-i):
        print("* ",end="")
    print()
  #rhombus
  #Triangle
n=5
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("* ",end="")
    print()
#inverse triangle
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(n-i-1):
        print("* ",end="")
    print()
#advanced patterns
n=5
for i in range(n):
    print("*"*(i+1))
n=5
for i in range(n):
    print("*"*(n-i))
n=5
for i in range(n):
    print(" "*(n-i-1)+"*"*(i+1))
n=5
for i in range(n):
    print(" "*(i)+"*"*(n-i))
#rhombus
n=5
for i in range(n):
    print(" "*(n-i-1)+"*"*(i+1))
for i in range(n):
    print(" "*(i+1)+"*"*(n-i-1))
#butterfly
n=5
for i in range(n):
    print("*"*(i+1)+"  "*(n-i-1)+"*"*(i+1))
for i in range(n):
    print("*"*(n-i-1)+"  "*(i+1)+"*"*(n-i-1))
#Decorators in python-the function can be passed as the parameter of main function
def my_decorator(fune):
    def sub():
        print("soda")
        fune()
        print("priya")
    return sub
def say():
    print("hello")
d=my_decorator(say)
d()
#modules-A module in a python is a single file or files that is intended to be imported and used in python programs
#types-1.buit-in module-these are pre-installed with python ,such as math,os,sys...
import math
def area(r):
    print(math.pi)
    print(math.sqrt(r))
area(7)
import os
print(os.name)
#2.user-defined or custom modules-these are user-defined created to organise and reuse code across different projects
def greet(name):
    return f"hello,{name}"
pi=3.14
#this should be in one file
import filename
print(filename.name('prathyusha'))
print(filename.pi)
#3.standard module-pre installed but they are updated everytime and are not installed by default,but use them by default
import datetime
print(datetime.datetime.now())
import random
print(random.randint(1,10))
#4.third party modules-these are developed by community and can be installed using python packages on package managers like pip. eg:numpy,pandas,sklearn
import numpy as np
x=np.array([1,2,3])
print(x)
import pandas as pd
data=pd.DataFrame({'a':[1,2],'b':[2,4]})
print(data)
#oops
class ipl:
    def rcb(self):
        print("esala cup namde")
    def csk(self):
        print("thala for a reason")
a=ipl()
a.rcb()
a.csk()
class ipl:
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def csk(self):
        print(self.name)
        print(self.score)
        print("thala for a reason")
a=ipl('dhoni',200)
a.csk()
#oops(object oriented programming structure)-It is a programming paradigm that is used to structure a program so that properties and behaviours are bundled into individual objects
#class-It is a blueprint of an object
#syntax:class classname:
#   attributes and methods
class daily:
    print("welcome to QIS")
class cse:
    def p(self):
        print("welcome")
        print("to")
        print("QIS")
a=cse()
a.p()
class ipl:
    def __init__(self,captain,captain1):
        self.captain=captain
        self.captain1=captain1
    def csk(self):
        print(self.captain)
    def mi(self):
        print(self.captain1)
a=ipl("dhoni","hardik")
a.csk()
a.mi()
#Abstraction-hiding the unwanted area
from abc import ABC,abstractmethod
class Ipl(ABC):#abstract base class
    @abstractmethod
    def trophy(self):
        pass
class rcb(Ipl):
    def trophy(self):
        print("esala cup namde")
class csk(Ipl):
    def trophy(self):
        print("Thala for a reason")
o=csk()
o.trophy()
p=rcb()
p.trophy()
#Encapsulation-wrapping up of data into a single unit
class public:
    def __init__(self,name):
        self.name=name
o=public("prathyusha")
print(o.name)
class protected:
    def __init__(self,age):
        self._age=age
o=protected("19")
print(o._age)
class private:
    def __init__(self,name):
        self.__name=name
o=private("praveen")
print(o._private__name)
#polymorphism-many forms
#method overloading-same method but different parameters using variable length argumen
class cse:
    def pichollu(self,*args):
        print(args)
o=cse()
o.pichollu(1,2,3)
o.pichollu(4,5,6)
#method overriding
class parent:
    def work(self):
        print("i have no work")
class child(parent):
    def work(self):
        super().work()
        print("priya")
o=child()
o.work()
#merge+insertion =hybrid alogrithm which is tim sort alogrithm used in sort() method
#bubble sort-adjacent comparisions upto n-1 iterations in each stage
'''l=[5,3,4,2,1]
n=len(l)
for i in range(n-1):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)'''
#selection sort-by comparing index
l=[5,3,4,2,1]
n=len(l)
for i in range(n):
    m=i
    for j in range(i,n):
        if l[j]<l[m]:
            m=j
    l[i],l[m]=l[m],l[i]
print(l)
#practice
n = 5
s = "IAMASTUDENTOFQISCAVE"
index = 0

for i in range(n):
    for j in range(n):
        # First row: print first 5 letters of string s
        if i == 0 and j <= 4:
            print(s[index], end=" ")
            index += 1
        # First diagonal: print next 5 letters of string s
        elif i == j and j <= 4:
            print(s[index], end=" ")
            index += 1
        # Second diagonal: print next 5 letters of string s
        elif i + j == n - 1 and j <= 4:
            print(s[index], end=" ")
            index += 1
        else:
            print(" ", end=" ")
    print()

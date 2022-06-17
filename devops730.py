# Variable & data types
"""
a = -108765432345678987654
b = 88876.5456789
c = 1j
d = "Hello world 1234 !@#$%^&"
e = False

# print() - it is a function
print(a)
print('a')
print(b)
print(c)
print(d)
print(e)
print(a,b,c,d,e,100,'hello')
"""

# variable = value/data, data type, memory address 
"""
x = False
print(x)        # data of x
print(type(x))  # data type of x
print(id(x))    # memory address of x
"""

# type casting
"""
a = float(10)
print(a,type(a))

b = int(20.99876567)
print(b,type(b))

c = str(100)        # c = "100" 
print(c,type(c))

d = int("12345")
print(d,type(d))

e = bool("hello123")
print(e, type(e))
"""

# input()  - function
"""
print("Enter a number")
a = input()
x = int(a)
print("The user given value x =", x, type(x))

print("Enter a number")
b = int(input())
print("The user given value =", b, type(b))

c = x + b
print("The sum =", c, type(c))
"""

# pep8 
"""
a = 10
b=20
c                 =               23456
print(a,b,c)
"""

# Operators
# arithmetic Operator
"""
print(10 + 3)   # 13
print(10 - 3)   # 7
print(10 * 3)   # 30
print(10 ** 3)  # 10 power of 3 = 10*10*10 = 1000
print(10 / 3)   # 3.33333333
print(10 // 2)  # Quotient
print(10 % 2)   # Remainder
"""

# assignment operator (while loop)
"""
a = 10
print(a)    # 10

a += 5      # a = a + 5
print(a)    # a = 15

a *= 2      # a = 15 * 2
print(a)    # a = 30

a *= a      # a = a * a
print(a)    # a = 900
"""

# comparision operator, return T/F (bool)
# if else, while loop
"""
print(10 == 10)     # T
print(10 != 10)     # F
print(10 >= 10)     # T
print(10 > 10)      # F
print(10 <= 10)     # T
print(10 < 10)      # F
"""

# logical operator - and or not
# if else, while loop
"""
print(10==10 and 4<6)   # T and T = T
print(10==10 and 4>6)   # T and F = F
print(10==10 or 4>6)    # T or F  = T
print(not 10==10)       # not T   = F
"""

# operator Precedence
# 26, 16
# BODMAS - Bracket of Div Mul Add Sub
"""
print(10 + 3 * 2)
print((10 + 3) * 2)
"""

# Collection
# List  - collection of data types
# array - collection of similar data types

# List - []
#    0   1       2          3    4   5 - indexes
"""
a = [1,2.66,"hello world",False,5j,6.77,1,1,1,1,1,1]    # duplicate memebers
print(a, type(a))

print(a[2])     # ordered

a[2] = "orange" # changeable
print(a)
"""

# tuple - ()
"""
a = (1,2.66,"hello world",False,5j,6.77,1,1,1,1,1,1)    # duplicate memebers
print(a, type(a))

print(a[2])     # ordered

a[2] = "orange" # unchangeable
"""

# set - {}
"""
a = {'a','a','a','b','b','c'}    # no duplicate memebers
print(a, type(a))
"""

# if else
  
# syntax
"""
if <condition T/F>:
elif <condition T/F>:
else:
"""

# if 
"""
a = 100
if a>10:
    print("a is bigger than 10")
"""

# if + Indentation
"""
a = 10
if a>10:
    print("a is bigger than 10")
    print("code inside if condition")
print("end of if condition")
print("program over")
"""

# if + else
"""
a = 10
if a>10:
    print("a is bigger than 10")
    print("code inside if condition")
    print("end of if condition")
else:
    print("a is smaller than 10")
    print("code inside else condition")
print("program over")
"""

# if + elif + else
"""
a = 10
if a>10:
    print("a is bigger than 10")
    print("code inside if condition")
    print("end of if condition")
elif a==10:
    print("a is 10")
else:
    print("a is smaller than 10")
    print("code inside else condition")
print("program over")
"""

# Rules
"""
if <condition T/F>:
elif <condition T/F>: (optional) (as many as you want)
else:                 (optional)
"""

# example 
"""
a = 10
if a>10:
    print("a is bigger than 10")
elif a<10:
    print("a is smaller than 10")
"""

# 
"""
if False:
    print("a is bigger than 10")
else:
    print("a is smaller than 10")
"""

# 
"""
a = 20
if a==20:
    print("a")
elif a==20:
    print("b")
else:
    print("c")
"""

# multiple elif
"""
a = 40
if a==20:
    print("a")
elif a==20:
    print("b")
elif a==30:
    print("c")
elif a==40:
    print('d')
"""

"""
a = 101
if a>10 and a>100:
    print("a is a biggest number")
else:
    print("hi")
"""

# loop

# while loop - numbers
# for loop - string/list/tuple/set

# while loop
# syntax
"""
while <condition T/F>:
"""

# while loop
"""
a = 1
while a<=5:
    print(a)
    a = a + 1
print("loop over")
"""

# example
"""
a = 70           # Intilization, Start
while a<=100:    # condition, Stop
    print(a)
    a = a + 2    # Incrementation, jump
print("loop over")
"""

# KeyboardInterrupt = Ctrl + C
"""
a = 1
while a>0:
    print(a)
    a = a + 1
print("loop over")
"""

# for loop syntax
"""
for <variable> in <string/list/tuple>:
"""

# fetches letter by letter
"""
for i in "hello":
    print(i)
"""

# fetch element by element
"""
for i in [1,2.33,"hello",False]:
    print(i)
"""

# 
"""
for i in "hello":
    print(i,end='')
"""

# python standard functions/method
"""
print()
input()
id()
type()
int()
float()
bool()
str()
"""

# user def functions
"""
def func_name():
"""
# 1. func creation
"""
def mithran():      # func create
    print("hello world")
    print("code inside myfun")
    print("end of mithran fun")

def myfun():
    print("hello mars")
    print("code inside myfun")

myfun()
mithran()
myfun()
"""

# 2. func + arguments
"""
def myfun(a,b):         # a & b are arguments
    print("hello mars")
    print("the values passed are",a,b)

myfun(20,40)
myfun('hello',88.99)
"""

# 3. func + default argument
"""
def myfun(a=0,b=0):         # a & b are default arguments
    print("hello mars")
    print("the values passed are",a,b)

myfun()
myfun(14)
myfun(b=14)
myfun(14,'hi')
"""

# 4. func + arbitrary argument 
"""
def myfun(*x):   # x is an arbitrary argument
    print("the values are", x)
    y = list(x)
    print(y)

myfun()
myfun(2,3)
myfun(1,2,3,4,5,6,7,46,8,8,8,8,8)
"""

# 5. func + return

"""
def myfun():
    print("hello world")
    return 100

def newfun():
    print("hello mars")
    return 500

z = myfun() + newfun() + myfun()
print(z)
"""

# Library
"""
import math
x = math.sqrt(24)
print(x)
"""

# 
"""
import myownlib
print(myownlib.a)
print(myownlib.b)
myownlib.myfun()
"""

"""
import boto3
x = boto3.resource('ec2')
x.create_key_pair(KeyName='python1704')
"""

"""
import boto3
x = boto3.resource('ec2')
x.create_instances(ImageId='ami-0bcf5425cdc1d8a85',InstanceType='t2.micro',KeyName='python1704',MaxCount=3,MinCount=1)
"""
    
"""
import os
import time

os.mkdir("C:/Users/mithr/Documents/hi")
time.sleep(7)
os.rmdir("C:/Users/mithr/Documents/hi")
"""
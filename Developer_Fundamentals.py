#Code must be readable and easily understandable
#Lines should be commented
#The code being predictable and easy to read is more important than hard big code
#do not repeat yourself in code.Use For and while loops

#u can make functions as well like this:
def Say_hello(name,emoji):
    print(f"HELLO000000000000000000000000 {name}{emoji}")

#parameters are given the bracket
#def say_hello(name,emoji):
Say_hello("Ishan",'😀')
Say_hello("Aaryan",'😀')
Say_hello("Anvay",'😀')

#arguments are the actual values while the parameters are the space

#return is an important keyword which is especially needed when u make functions

# def sum(num1, num2):
#     return num1 + num2
# print(sum(2,3))
# print(sum(10,5))

#u can also simply replace return with print()

#rule of function
#A function should do One thing PERFECTLY(does not mean that doing multiple things is bad)
#It should return a valid and useful output

#some built in functions are 
#list()
#print()
#max(arg1, arg2)
#min(arg1, arg2)
#input()
#def

#you can also make your own functions
#def say hello(line 7.) is an example of it.

#methods are the ones with which u use .
#examples are:
my_list = [1,2,3,4,5,6,7]
print(my_list.index(3))
#the methods come to the left of the dots

def test(a):
    'info: this is literally just print...with a new name tho.'
    print(a)

test('PRINT THIS NOW')
print(test.__doc__)

#clean code.
#code should be minimal but readability is the priority over minimalism.
#clean code is helpful as well since its smaller and takes less time to read if its commented and written well
def is_even(num):
    if num % 2 == 0:
        return True
    return False

print(is_even(11))

#operators
#!= is for "not equal to"
# % is for checking the remainder" 
# == is for "is equal to"

#args and kwargs
#args = arguments
#kwards = keyword arguments
#*args **kwargs

def super_func(*args):
    print(*args)
    return sum(args)

print(super_func(1,2,3,4,5))

#*args makes it so that u can put infinite arguments 
#**kwargs makes it so that u can put infinite keywords

#rule: params, *args,default params, **kwargs

#scope- something present in many languages
#what variables keywords etc, do i have access to?

#print(Name) gives an error since Name isnt a variable
#total = 100 is called a global scope
#def whatev():
#   total = 100
#here total is a indented in a function so it isnt in the global scope
#therefore its unuseable out of the indent 

#There is the global keyword
#global
#it makes local variables to global variables
#there is the nonlocal keyword which makes it possible to use a variable in a local scope without making it local
#nonlocal
"""
A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.

"""

"""
In Python a function is defined using the def keyword:

ExampleGet your own Python Server:

def my_function():
    print("Hello from a function")

"""

"""
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

"""

"""
This function expects 2 arguments, and gets 2 arguments:

def my_function(fname, lname):
    print(fname + " " + lname)

my_function("Emil", "Refsnes")

"""

"""
If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

"""

"""
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

"""

"""
If the number of keyword arguments is unknown, add a double ** before the parameter name:

def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

"""

"""
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

"""

"""
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

"""

"""
def my_function(x):
    return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

"""

"""
function definitions cannot be empty, but if you for some reason have a function definition with no content,
put in the pass statement to avoid getting an error.

Example:

def myfunction():
    pass
    
"""

"""
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.

To specify that a function can have only positional arguments, add , / after the arguments:

Example:

def my_function(x, /):
    print(x)

my_function(3)
"""

"""
Without the , / you are actually allowed to use keyword arguments even if the function expects positional arguments:

Example:

def my_function(x):
    print(x)

my_function(x = 3)

"""

"""
But when adding the , / you will get an error if you try to send a keyword argument:

Example:

def my_function(x, /):
    print(x)

my_function(x = 3)

"""

"""
To specify that a function can have only keyword arguments, add *, before the arguments:

Example:

def my_function(*, x):
    print(x)

my_function(x = 3)

"""

"""
Without the *, you are allowed to use positionale arguments even if the function expects keyword arguments:

Example:
    
def my_function(x):
    print(x)

my_function(3)

But when adding the *, / you will get an error if you try to send a positional argument:

Example:

def my_function(*, x):
  print(x)

my_function(3)

"""

"""
You can combine the two argument types in the same function.

Any argument before the / , are positional-only, and any argument after the *, are keyword-only.

Example
def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

"""

"""
Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. 
This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, 
or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. 
The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

"""

"""
Recursion Example:

def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
"""

"""
    Exercises:

"""

"""
def my_function():
    print("Hello from a function")

"""

"""
Execute a function named my_function

def my_function():
    print("Hello from a function")

my_function()

"""

"""
Inside a function with two parameters, print the first parameter.


def my_function(fname, lname):
    print(fname)

"""

"""
Let the function return the x parameter + 5.


def my_function(x):
    return x + 5

"""

"""
If you do not know the number of arguments that will be passed into your function, 
there is a prefix you can add in the function definition, which prefix?

def my_function(*kids):
    print("The youngest child is " + kids[2])

"""

"""
If you do not know the number of keyword arguments that will be passed into your function, 
there is a prefix you can add in the function definition, which prefix?


def my_function(**kid):
    print("His last name is " + kid["lname"])

"""

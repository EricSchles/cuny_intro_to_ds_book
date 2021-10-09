#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# In this last section of chapter one we will be going over functions, a cornerstone of programming and one of the most important concepts you'll learn in this class.
# 
# We'll cover:
# * why
# * scoping, parameters, return
# * functions and flow of control
# * functions and iteration
# * multiple returns
# * some basic algorithms
# 
# Before we go through the sections, let's just see some examples of functions:

# In[1]:


def greeting(name):
    print("Hello "+name)
    
greeting("Eric")


# This is the general syntax of a function in Python, it's pretty similar to a function in almost any language you'll learn.  The basic style of Python functions are:
# 
# ```
# def FUNCTION_NAME(PARAMETER_1, PARAMETER_2,..PARAMETER_N):
#     FUNCTION BODY GOES HERE
#     [OPTIONAL] return SOME_VALUES
# ```
# 
# As you can see the important keyword is `def` before the function name, the `:` just like we used in if/elif/else statements and then a tabbed in body, just like in if/elif/else statements.  
# 
# The difference between these two programming concepts will become clear in a moment and what this concept tries to express.
# 
# # Why
# 
# Functions in general, from a programmatic standpoint, serve the process of storing code for reuse.  This is not dis-similiar from what you've seen thus far in this chapter with respect to iterations.  Recall our simple for loop:

# In[2]:


summation = 0
for i in range(10):
    summation += i
print(summation)


# Technically this above code is the same as:

# In[3]:


summation = 0
summation += 1
summation += 2
summation += 3
summation += 4
summation += 5
summation += 6
summation += 7
summation += 8
summation += 9

summation


# So why is the former prefered to the latter?  The answer, from a superficial standpoint is, simplicity, we just have to type less.  But there is additional benefit - _expressiveness_.  When something is sorter and cleaner, it is hopefully clearer.  That's _why_ we use iteration.  The same is true from a superficial standpoint with functions.
# 
# Suppose you had the following code:

# In[4]:


names = [
    "eric", "susan",
    "Phil", "barbara",
    "jim", "carmen",
    "chadwick"
]
for name in names:
    greeting_string = "Hello "
    if name.islower():
        name = name.capitalize()
    print(greeting_string + name)


# The code inside the for loop isn't that messy, but it's not the most readable.  If we added a function and removed some of the code inside the loop then it would be easier to read:

# In[5]:


def create_greeting(name):
    if name.islower():
        name = name.capitalize()
    return "Hello " + name

names = [
    "eric", "susan",
    "Phil", "barbara",
    "jim", "carmen",
    "chadwick"
]
for name in names:
    print(create_greeting(name))


# Notice, now it's clearer what's happening in the for loop, because we simplified it by abstracting the details out to functions.  This was perhaps a contrieved example, however the general point should stand out: functions allow us to easily reuse pieces of code.
# 
# We've already seen this several times.  Recall from earlier sections, the `math` module:

# In[6]:


import math

math.pow(2, 7)


# The above piece of code uses a function.  It just happens that someone _else_ defined the function for us.  And then we get to just _use_ it.  This is another core use of functions - it allows us to easily use someone elses code.  
# 
# # Scoping, Parameters, and Return
# 
# ## Scope
# 
# One of the important features of a function is it is self contained.  That means the only way for it to be _aware_ of any variables is to pass them in explicitly.  That said, functions will be _aware_ of the other functions in the program.  So to summarize, functions can't see the other variables in a script, but can see the other functions in the script.  
# 
# So where and how does this _awareness_ work?
# 
# Consider the following example:

# In[12]:


def adder(y):
    x = 14
    return y + x

x = 7
y = 12
print("return value of the function:", adder(y))
print("value of x:", x)


# The above example shows us how function scoping works -
# 
# The variable `y` is passed into the function, so it goes from the global scope of the program, to the local scope of the function `adder`.  
# 
# Next let's look at the variable `x` - notice that we define it twice:
# 
# * once in the global scope
# * once in the local scope of the function `adder`
# 
# In this second scope, local to the function, the value of x is used in the sum: `x + y`, however in the global scope, the variable x is _never used_.
# 
# That's why the value of x _stays_ `7` when we print it out in the end, in general, this implies that the scope local to the function can't see and therefore cannot manipulate those in global scope.
# 
# ## Parameters
# 
# So far we've dealt with functions of one parameter, however as we saw from the general definition of functions, we can have 'N' many parameters, where 'N' is just some arbitrary number.  Here is an example of a function with two parameters:

# In[14]:


def adder(x, y):
    return x + y

w = 5
z = 6
print(adder(w, z))


# As you can see, this function takes in two variabls from global scope instead of one, and then adds them.  Inside the scope of the function, these variables are called `x` and `y`.  And at the global scope, they are called `w` and `z`.
# 
# Now let's look at how we pass a list, instead of a variable:

# In[15]:


def sum_numbers(listing):
    summation = 0
    for elem in listing:
        summation += elem
    return summation

list_of = [1,23,4,5,66,1,23,41,2]
sum_numbers(list_of)


# As you can see - functions parameters work the same way variables do, with respect to syntax - to pass a list, we simply pass the name of the list and Python does the rest.
# 
# However!  There is an important difference - Python passes list by reference, rather than by value.  This means rather than creating a _new_ list and then passing that into the function, Python actually passes what's called the _references_ of the list.  We'll get into this more in chapter 2, but basically, this means there are no scoping rules on lists.
# 
# Let's look at an example:

# In[16]:


def mutate_list_elements(listing):
    listing[0] = 7
    
listing = [1,2,3,4,5]
mutate_list_elements(listing)
print(listing)


# See!  Even though we never set the new list to the old list, or _even_ returned the new list, the old list was _still_ mutated.  Some people see this as a very bad thing, because it can lead to very subtle bugs, but the performance gain of passing by reference versus by value is just too attractive to ignore.  So we live with this consequence.
# 
# ## Returns
# 
# So we've talked naively about returns thus far, sort of _implicitly_.  Now we make explicit what was implicit - a return is _how_ a function goes from local to global scope.  It's what we _pass back up_ to global scope.
# 
# Since the above example sort of feels like a counter example to this, because of the weirdness of pass by reference, let's look at a quick example to see how this works:

# In[17]:


def adder(x, y):
    return x + y

w = 9
z = 10
summation = adder(w, z)
print(f"the sum of {w} + {z} = {summation}")


# So how this worked is - we took our variables from _global_ scope and then stuck them in variables x and y, once we entered into the function - that's because that's the name of the parameters once we enter the function.  Then we do the addition, and the _return_ is what comes back from the function.
# 
# So when we do:
# 
# `summation = adder(w, z)`
# 
# The value of there result: x + y, aka the piece of code that gets _returned_ is what ends up in the variable `summation`.  
# 
# So returns will _typically_ be the last line of a function, because after that we _tend_ to leave the local scope.  One of the neat things about Python though, is we can return _multiple_ things at once!
# 
# For instance:

# In[20]:


def some_formula(x, y):
    z = x / y
    return x + z - y, z

w = 9
q = 10
result, ratio = some_formula(w, q)
print(f"the result of {w}, {q} for some formula = {result} with a ratio factor of {ratio}")


# As you can see, this random formula returns two things:
# 
# * The result of the formula: `x + z - y`
# * The implicit ratio used within the formula: `z = x / y`
# 
# This way we know _what_ happened inside the function.  
# 
# Notice the general syntax:
# 
# ```
# def FUNCTION_NAME(PARAMETER1, PARAMETER2, .., PARAMETERN):
#     some code goes here
#     return result_one, result_two, .., result_n
# ```
# 
# This means we could return as many things as we wanted.  Notice also, that when we set the return equal we needed the same number of commas _between_ variables:
# 
# `result, ratio = some_formula(w, q)`
# 
# Because our return was:
# 
# `return x + z - y, z`
# 
# That's how we got our variables to match up.  We could also store all the results in something called a tuple.  Let's look at an example and then we'll dive a little deeper into tuples:

# In[22]:


def identity(x, y):
    return x, y

w = 10
z = 12

result = identity(w, z)
print("The result is:", result)
print(type(result))


# as you can see, we pass back a tuple because of the use of the comma in the return.  If we check the type for a function with just one return, we'll see that the type is just that of the returned variable:

# In[23]:


def some_function(x):
    return x + 2

x = 7
result = some_function(x)
print("the result is", result)
print(type(result))


# Next let's provide a little understanding of tools:
# 
# A tuple is like a list, but you can't make it bigger or smaller.
# 
# This might make you think tuples don't have much value, but they are great!  They just aren't good for the _same_ things as lists.
# 
# Let's look at an example of a tuple:

# In[24]:


t = tuple([1,2,3])

print("things tuples can do:")
[elem for elem in dir(t) if "__" not in elem]


# As you can see, all you can do is get the index of a specific element:

# In[29]:


index_of_two = t.index(2)

print(f"index of {t[index_of_two]} is {index_of_two}")


# Or count the number of occurrences of a given element:

# In[31]:


count_2 = t.count(2)
print(f"number of times 2 appears in t: {count_2}")


# As you saw above we can also index into tuples, like you can with lists.  And you can iterate over tuples:

# In[32]:


for elem in t:
    print(elem)


# But that _is_ the power of tuples.  Because you have guarantees on how many elements you can expect, and because your tuples are iterable like lists, that means you can do make assumptions about your data.  Which is why its used for the multiple value return amongst other things.  Admittedly, there aren't infinite uses for tuples, but they have their uses.
# 
# The biggest reason we use them for multiple value returns is once functions are defined, they should have _fixed_ behavior.  That means if a function returns a certain amount of data, it should return it consistently.  This means you can think intelligently about your program.
# 
# # Functions and Flow of Control
# 
# In addition to being able to make use of simple statements inside of functions like addition or basic string manipulation, we can also do more advanced things like flow of control:

# In[33]:


def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
print("is 7 even?", is_even(7))


# Notice - because this function could take one of two paths - it has _two_ return statements, one for each branch.  Of course we could rewrite this to have one return:

# In[34]:


def is_even(x):
    result = None
    if x % 2 == 0:
        result = True
    else:
        result = False
    return result

print("is 7 even?", is_even(7))


# But the first way just _feels_ cleaner.  In addition to being able to bring flow of control into a function - we can take a complicated boolean statement, and _stick it into a function_:

# In[35]:


def complicated_boolean(x, y, z, w):
    return not ((x and y) or z) and w

x = True
y = False
z = True
w = True
if complicated_boolean(x, y, z, w):
    print("got here")
else:
    print("didn't get here")


# Next let's see how a function can make our code cleaner:

# In[1]:


def power(a, b):
    product = 1
    for _ in range(b):
        product *= a
    return product

powers_of_2 = {}
for i in range(30):
    powers_of_2[i] = power(2, i)
    
powers_of_2[14], powers_of_2[0]


# Next let's implement a logarithm and check that it inverts the exponentiation:

# In[2]:


def log(base, result):
    counter = 0
    while result > 1:
        result /= base
        counter += 1
    return counter

for i in range(1,30):
    if log(2, powers_of_2[i]) != i:
        print("failed")
        break


# In general functions are how we implement mathematics, which is what we'll need to do mathematics.  Now let's learn a little combinatorics.
# 
# One of the fundamental functions in combinatorics is the factorial, $n!$ which gets used in the choose function:
# 
# $$ {n \choose k} = \frac{n!}{k!(n - k)!} $$
# 
# Let's implement the factorial first:

# In[3]:


def factorial(n):
    result = 1
    for num in range(n, 1, -1):
        result *= num
    return result

factorial(3)


# Now we can implement the choose:

# In[4]:


def choose(n, k):
    denominator = factorial(k) * factorial(n - k)
    return factorial(n)/denominator

choose(10, 4)


# Now that we have the `choose` function we can use it for some things!
# 
# For one we can implement:
# 
# $$ (x + y)^{n} = \sum_{k=0}^{n}{n \choose k}x^{n-k}y^{k} $$

# In[5]:


def binomial_formula(x, y, n):
    summation = 0
    for k in range(n):
        summation += choose(n, k) * power(x, n-k) * power(y, k)
    return summation

binomial_formula(4, 5, 4)


# We can also use the choose function to calculate a probability:
# 
# Problem:
# 
# I choose 3 cards from the standard deck of cards.  What is the probability that these cards contain at least one ace?
# 
# Here the sample space contains all possible ways to choose 3 cards from 52 cards, thus
# 
# $$ |S| = {52 \choose 3} $$
# 
# There are 52 - 4 = 48 non-ace cards so we have:
# 
# $$ |A^{c}| = {48 \choose 3} $$
# 
# Thus,
# 
# $$ P(A) = 1 - \frac{{48 \choose 3}}{{52 \choose 3}} $$
# 
# We can implement the solution:

# In[6]:


1 - choose(48, 3)/choose(52, 3)


# Next let's go over some type hinting.  Type hinting lets you give hints in your code for what parameters are expected by the program.  Let's look at an example:

# In[8]:


def adder(x: int, y: int) -> int:
    return x + y

adder(5, 6)


# In general, the way the syntax works is:
# 
# ```
# def FUNCTION_NAME(param1: type1, param2: type2, .. paramN: typeN) -> return type:
#     code body
#     return some_data
# ```
# 
# As you can see from the example and the generalization we specify the variables like before, but then also specify the types.  Some basic types include:
# 
# * int 
# * float
# * str
# * bool
# 
# There is also a builtin `typing` library that has many more types.  You can read more about those [here](https://docs.python.org/3/library/typing.html).

# In[ ]:





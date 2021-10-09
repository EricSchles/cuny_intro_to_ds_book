#!/usr/bin/env python
# coding: utf-8

# # Functions
# 
# We've informally seen functions throughout this book so far, but now we'll give them a formal introduction.  Let's look at an example:

# In[1]:


def greeting(name):
    return "Hello " + name

greeting("Eric")


# Let's look at the syntax around functions:
# 
# ```
# def FUNCTION_NAME(PARAMETER_1, PARAMETER_2, ..., PARAMETER_N):
#     code block..
#     return (PARAMETER_1, PARAMETER_2, ..., PARAMETER_N)
# ```  
# 
# a function is a block of code that runs in a local context, separate from the global scope of the program.  Next let's see how a function can make our code cleaner:

# In[4]:


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

# In[11]:


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

# In[12]:


def factorial(n):
    result = 1
    for num in range(n, 1, -1):
        result *= num
    return result

factorial(3)


# Now we can implement the choose:

# In[20]:


def choose(n, k):
    denominator = factorial(k) * factorial(n - k)
    return factorial(n)/denominator

choose(10, 4)


# Now that we have the `choose` function we can use it for some things!
# 
# For one we can implement:
# 
# $$ (x + y)^{n} = \sum_{k=0}^{n}{n \choose k}x^{n-k}y^{k} $$

# In[23]:


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

# In[24]:


1 - choose(48, 3)/choose(52, 3)


# Next let's go over some type hinting.  Type hinting lets you give hints in your code for what parameters are expected by the program.  Let's look at an example:

# In[25]:


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

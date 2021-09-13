#!/usr/bin/env python
# coding: utf-8

# # Flow of Control
# 
# * Flow of control
#     * indenting in Python
#     * if/elif/else
#     * fizzbuzz
#     * evens and odds
#     
# ## Flow Of Control
# 
# Now that we've looked at libraries and basic python types, it's time to start learning the power of computer science!  Basically everything we've done up until this point is just using a programming language as a _very_ fancy calculator, that is automating mathematics.  
# 
# But now we'll explore the first thing we can't _really_ do with a calculator - flow of control. Flow of control centers around one basic notion - that if we can tell whether or not something is True, then we can draw conclusions from the truth of that statement.  
# 
# Let's look at an example:
# 
# Suppose you want to make sure, that no matter what random number you pick, it's always even.  How might you ensure that?
# 
# Well, we can observe that all odd numbers are of the form: 
# 
# $$ 2k + 1 \text{ s.t. } k \in \mathbb{N} $$
# 
# If you aren't used to the above notation, the $ \in $ stands for 'in' and the s.t. stands for 'such that'.
# 
# So, knowing that all odd numbers are just an even number $+1$, we can simply add or subtract `1` to get another even number.
# 
# There is one more piece of syntax before we can create our code - the modulo operator: `%`.
# 
# The modulo operator gets the remainder from integer division instead of the quotient.  The way this works is by observing this fact:
# 
# $$m = aq + r \text{ s.t. } m,a,q,r \in \mathbb{N}$$
# 
# That is - for any numbers, m and a such that:
# 
# $m$ is divided by $a$ we get the above formula.
# 
# Let's look at some examples to verify this:

# In[5]:


m = 17
a = 12

print(f"Quotient of {m}/{a} is", m//a)
print(f"Remainder of {m}/{a} is", m % a)


# What this says is: 
# 
# $$ 17 = (12*1) + 5 $$
# 
# That seems right.  Will this always work?!  Yes!  Let's pick some random numbers:

# In[7]:


import random

m = random.randint(101, 1000000)
a = random.randint(0, 100)

print(f"Quotient of {m}/{a} is", m//a)
print(f"Remainder of {m}/{a} is", m % a)


# You can verify this works yourself by running the above code a bunch of times (it will always work).

# Now we are ready for our flow of control example:

# In[8]:


import random

random_number = random.randint(0, 1000000)

if random_number % 2 == 1:
    random_number += 1

random_number    


# As you can see, we always get an even number.  You can verify this too by running the above code as many times as you want.  It will always produce an even number.
# 
# Now let's go over the flow of control syntax in a bit more detail:
# 
# ```
# if [STATEMENT THAT RESOLVES TO TRUE OR FALSE]:
#     [SOME CODE GOES HERE]
# ``` 
# 
# First let's talk about the statement that resolves to true or false - this is just a variable of type boolean, as we've seen in previous sections.  That is, any statement that goes into the `if` statement just needs to resolve to one of the binary values `True` or `False`.
# 
# Notice there is _some_ new syntax here:
# 
# First, the `if` keyword - we always state any flow of control with an `if`, specifically this is saying "if this statement is `True` then do the following.
# 
# Next we have a `:` at the end of the boolean statement.  This indicates that we are about to go into what's called a new scope - that's code that may not _always_ run in every version of the program.  It's code that might only run sometimes.  
# 
# Finally, our code is indented to indicate a change in scope.  This means it goes on a new line and is either tabbed in or whitespaced in.
# 
# This final point can feel very conceptual, but once you get used to reading code this way, it appears elegant and useful.
# 
# Intuitively the way I think of scoping rules is as the same as a to do list.  Let's look at an example for context:
# 
# Things I need to do today:
# * brush my teeth
# * study a lot
# * learn some statistics
# * eat breakfast
# * eat lunch
# * eat dinner
#     
# As you can see the above list, the individual items are _tabbed_ in, so each item is implied to be within the _scope_ of the list, things I need to do today.
# 
# Now let's talk about some consequences of changing scope - optionally created variables.  Best to look at an example for this:

# In[2]:


x = 7

if x == 7:
    y = 9
    x += y
else:
    z = 29
    x += z
    
print(x)


# The above code introduces two new pieces of syntax - the first being the `else` statement, which works with the 'if' statement above - specifically the joint statement is:
# 
# if x equals 7, create a variable y and add it to x, otherwise, create a variable z and it to x.
# 
# We can sort of think of the else as the opposite of the if statement.  So if x equals anything _but_ 7 then do that.
# 
# The next thing that's new is variables created in _local scope_.  So if x equals 7, then we create y, _but_ if it doesn't then y never get's created.  Likewise, if x equals 7, then z is _never_ created.  Let's verify this by trying to add `x + z`:

# In[3]:


x + z


# As you can see, the scope for z was never entered, so the variable is number created.  That's why we get a `NameError`.  Before we move onto another topic there was one last piece of syntax we need to cover:
# 
# `elif`
# 
# The `elif` statement stands for else if, and executes only if the `if` statement is false.  Additionally the boolean in the `elif` statement needs to be true.  Let's look at an example using `elif`:

# In[5]:


x = 14

if x == 12:
    w = 1
    x += w
elif x == 14:
    q = 2
    x -= q

print(x)


# As you can see, the elif statement executes because the if statement was false.  But what happens if both statements are true?

# In[6]:


string = "Hello there friends!"

if "e" in string:
    print("there are vowels here!")
elif "!" in string:
    print("this string has no alphabet characters")
else:
    print("no e or ! here")


# As you can see, because the first condition was true, it executed, this happened _even though_ the condition in the `elif` was true.
# 
# Also note, we introduced an `else` condition here - in this case, the code in the `else` block will only execute if neither the `if`, nor the `elif` statement happen to be true.
# 
# Before we leave this topic, let's look at one more bit of functionality - multiple `elif`'s:

# In[8]:


string = "Hello there"

if "z" in string:
    print("there is a 'z' here!")
elif "!" in string:
    print("this string has no alphabet characters")
elif "the" in string:
    print("there is a substring that spells 'the'")
else:
    print("no e or ! here")


# In this example there are _two_ elif statements. We execute the second one because the `if` _and_ the first `elif` are both `False`.  As an aside, in some cases, where you might have many `elif` statements, it might make more sense to combine some of these using boolean operators like `and` or `or`.  It all depends!
# 
# Finally, let's look at a problem that is often asked on computer science interviews for junior developers - fizzbuzz.
# 
# The fizzbuzz problem is written as follows:
# 
# For a random integer, but print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5, otherwise print the integer.
# 
# Before you see the answer - try implementing this yourself on a `.py` file.  It's good practice and likely to come up again on an interview.  
# 
# Answer:

# In[16]:


import random

integer = random.randint(0, 10000000)

if integer % 3 == 0 and integer % 5 == 0:
    print("FizzBuzz")
elif integer % 3 == 0:
    print("Fizz")
elif integer % 5 == 0:
    print("Buzz")
else:
    print(integer)


# We check if the integer is divisible by 3 and by 5 first, because of the order of execution of the control statements -
# 
# If we checked for divisability of 3 or 5 alone first, if the number was in fact divisible by both, we would never know.  So we _need_ to check for 3 and 5 first.  After that, the ordering doesn't matter.  Finally, we enter the else condition - simply printing the integer assuming it is neither divisible by 3 or 5.
# 
# Before we leave this section - a note on divisability - can you figure out why if a number % 3 == 0 implies it's divisible by that number?
# 
# Simply recall our division algorithm from earlier:
# 
# $$ m = aq + r $$
# 
# If $r=0$ this implies there is no remainder when we divide $\frac{m}{a}$ this is why if $r=0$ then that's the same thing as _divisability_.

# In[ ]:





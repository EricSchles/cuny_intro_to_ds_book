#!/usr/bin/env python
# coding: utf-8

# # Iteration, The True Power Of Programming
# 
# In general, when programming, the main thing we are concerned about is something called efficiency.  This specifically refers to how 'fast' in general our code is.  
# 
# Well the reason why programs efficiency matters, is because we are going to do things a bunch of times. And when I say a bunch of times, I some times mean trillions of times.
# 
# In order to do this, we use a technique called "iteration". This allows us to carry out an activity many, many times.
# 
# Let's look at an example:

# In[1]:


index = 0

while index < 10:
    print(index)
    index += 1


# The above simple example accomplishes a fairly trival task, it enumerates all the numbers between 0 and 9.  This is the basis for interation.  Iteration is _always_ indexed by the natural numbers.  That's why we name the variable we are "iterating over" the index.  As the index increases, we get closer and closer to the terminal statement.
# 
# Here the terminal statement is inside a "while" loop.
# 
# A while statement works somewhat like an if statement.  In an if statement, we check a condition and if the condition is True, then we execute a set of steps.  In a while loop, we check if a condition is True, the same way as before.  The difference being, we keep executing the statement, _until_ the statement is False.  This means any while loop has the potential to go on forever, without stopping.  
# 
# The way we get around this generally is with something called a for loop, which will get to in a little while.
# 
# Now that we have a means of iterating, let's go back to some of the examples we've looked at and add some iteration _spice_!
# 
# First let's look at some stuff with random numbers.  Specifically, we'll see how often a random number is even or odd:

# In[13]:


import random

evens = 0
odds = 0
num_samples = 5
i = 0
while i < num_samples:
    random_number = random.randint(0, 1000000)
    if random_number % 2 == 0:
        evens += 1
    else:
        odds += 1
    i += 1
        
print("Evens percentage:", evens/num_samples)
print("Odds percentage:", odds/num_samples)


# Let's see what happens if we increase the sample size?  Do we get closer to 50/50 or further away?

# In[14]:


import random

evens = 0
odds = 0
num_samples = 500
i = 0
while i < num_samples:
    random_number = random.randint(0, 1000000)
    if random_number % 2 == 0:
        evens += 1
    else:
        odds += 1
    i += 1
        
print("Evens percentage:", evens/num_samples)
print("Odds percentage:", odds/num_samples)


# Looks like we are getting closer, how many do we need to get to pretty much exactly 50/50?

# In[15]:


import random

evens = 0
odds = 0
num_samples = 50000
i = 0
while i < num_samples:
    random_number = random.randint(0, 1000000)
    if random_number % 2 == 0:
        evens += 1
    else:
        odds += 1
    i += 1
        
print("Evens percentage:", evens/num_samples)
print("Odds percentage:", odds/num_samples)


# Looks like we've gotten pretty close!  Let's do one more:

# In[16]:


import random

evens = 0
odds = 0
num_samples = 500000
i = 0
while i < num_samples:
    random_number = random.randint(0, 1000000)
    if random_number % 2 == 0:
        evens += 1
    else:
        odds += 1
    i += 1
        
print("Evens percentage:", evens/num_samples)
print("Odds percentage:", odds/num_samples)


# Looks like we got super close!  In general, the above example illustrates something called _asymptotic_ behavior.  This is the behavior that a system exhibits in the long run.  
# 
# In this case - we know that the probability that a given natural number is even or odd is 50%.  However, getting to this experimentally isn't always obvious.  Important questions include:
# 
# * How many samples do we need to draw before we get close to our theoretical value?
# * How do we define close?
# * Are we sure we are capturing the entire space of possible samples?  In otherwords, are there any 'rare' cases we need to look out for?

# Next let's look at a modification of FizzBuzz:
# 
# For integers 1 to N, print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5, otherwise print the integer.
# 
# Notice the difference - now we'll iterate through a bunch of numbers, rather than some random number:

# In[19]:


integer = 0
while integer < 20:
    if integer % 3 == 0 and integer % 5 == 0:
        print("FizzBuzz")
    elif integer % 3 == 0:
        print("Fizz")
    elif integer % 5 == 0:
        print("Buzz")
    else:
        print(integer)
    integer += 1


# ## Lists
# 
# Now that we've gotten through how to represent data and iteration, the next thing to do is learn to represent "collections" of variables.  For this will need something called a list:

# In[2]:


listing = [1,2,3,4,5]

print(listing)


# Lists are different than the other variables we've seen thus far, in that in addition to being able to print the _entire_ collection, we can also print specific elements:

# In[3]:


print(listing[0])
print(listing[4])


# Notice that lists are "zero-indexed", so if there are "N" elements in our list, then the last number is in the "N"-1st position.  That's why, when we access the fourth index, we are actually getting the 5th element.
# 
# Let's look at how to iterate over a list using a while loop:

# In[4]:


listing = [1,2,3,4,5]

index = 0
while index < len(listing):
    print(listing[index])
    index += 1


# There is actually a short hand for above, the for loop that we talked about earlier:

# In[5]:


listing = [2,3,4,5,6]

for element in listing:
    print(element)


# I started this list at 2 just to make it clear that we iterate _over the elements_ of the list, not an index.
# 
# And if we'd like to print the index _and_ the elements we can do so as follows:

# In[6]:


listing = [1,2,3,4,5]

for index, element in enumerate(listing):
    print("The element is",element,"at index",index)


# Notice that we concatenated the element, index variables with the string by using `,`'s.  This will only work inside of a print statement.  If python sees a string and an integer then this won't work in general, so we cannot do the following:

# In[7]:


"thing " + 5


# In[ ]:





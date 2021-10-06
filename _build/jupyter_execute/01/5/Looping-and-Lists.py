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
# In addition to being able to store elements of the same type, we can also have lists with _multiple_ element types:

# In[2]:


x = 42 + 6
listing = [1, 5.07, "hello", True, x]
listing


# As the above example shows, we can store all of the basic types that we've seen so far in a list.  We can even store _variables_ in a list.  In addition to being able to store basic types, we can also store _functions_:

# In[3]:


import random

list_of_functions = [min, max, random.random, random.randint]

list_of_functions[0](25, 40)


# While the above example doesn't get used that often programmatically, it's still _possible_.  So far, we've only added elements to a list at assignment to a variable name.  But what if we wanted to start with an empty list and then _add_ elements, how would that work?
# 
# There are a few ways to do this:
# 
# * append - using this method we add elements to the end of the list
# * insert - using this method we can add elements to any position of the list, however this requires us to specify the index we would like to add our element to.
# 
# Let's see some examples:

# In[6]:


listing = []
listing.append(5)
print(listing)
listing.append(6)
print(listing)
listing.append(7)

listing


# As you can see, we first instantiate our list by assigning an empty list to the variable `listing`.  Then we add elements to the end of the list, one by one.  As stated above, using the append, 'appends' the elements to the end of our list.  This is a good typical practice, because it creates a notion of sequencing via operation.  In other words, the first element added to the list appears in the 1st position of the list, the 2nd in the second position and so on.  So we know where the element we added ended up based on it's index.  This isn't _always_ the right thing to do.  For those cases, we have the `insert` function associated with the list.
# 
# Let's look at an example using insert now:

# In[8]:


listing = []

listing.append(5)
listing.append(6)
listing.append(7)
print(listing)
listing.insert(0, 4)

print(listing)


# Here we add the `4` in position zero, aka the first position, so that we can keep our list in order.  Note: lists need not be ordered, although it is a nice property to have from time to time.  
# 
# We can also insert elements in any _available_ position in the list.  Let's look at an example of this:

# In[9]:


listing = []

listing.append(5)
listing.append(6)
listing.append(7)
print(listing)
listing.insert(1, 17)
print(listing)


# What would happen if we tried to insert in position 18 in the above list?  Note, the list only has 4 elements:

# In[11]:


listing.insert(18, 27)
listing


# In Python, since we don't have an 18th position, Python lists do the intelligent thing and just add the element to the end of the list.

# Now let's combine what we've learned so far - this is how to iterate over a list using a while loop:

# In[4]:


listing = [1,2,3,4,5]

index = 0
while index < len(listing):
    print(listing[index])
    index += 1


# Now that we can add a bunch of elements to a list at once, we can also do a few more things with lists - that is we can calculate information over the elements of the list.  For instance, suppose we had a list of random elements and wanted to know the value of the minimum element:

# In[13]:


import random

listing = []
size = 1000
index = 0

while index < size:
    listing.append(random.randint(0, 10000))
    index += 1
    
min(listing)


# The `min` function gives us the ability to _describe_ some sense of the information within the list, without having to look at _every_ element.  There are a bunch of functions for describing data, another one is `max`:

# In[14]:


import random

listing = []
size = 1000
index = 0

while index < size:
    listing.append(random.randint(0, 10000))
    index += 1
    
max(listing)


# If we were interested in the boundaries of our list, we would get both of these descriptives at once:

# In[15]:


import random

listing = []
size = 1000
index = 0

while index < size:
    listing.append(random.randint(0, 10000))
    index += 1
    
min(listing), max(listing)


# This gives us a sense of the _range_ of our random data, how big the difference is between the smallest and largest elements.
# 
# Within while loops there is a lot of syntax you need to account for, the extra required pieces do mean you have more flexability, but often you don't need that much flexability.  And the extra syntax can often lead to errors.  For instance, suppose we had the following while loop:
# 
# ```python
# listing = []
# size = 1000
# index = 0
# 
# while index < size:
#     listing.append(1)
#     index += 1
#     
# summa = 0
# while index <= size:
#     summa += listing[index]
#     index += 1
# ```
# 
# Would this work?  We'll try it now just to see:

# In[17]:


listing = []
size = 1000
index = 0

while index < size:
    listing.append(1)
    index += 1
    
summa = 0
while index <= size:
    summa += listing[index]
    index += 1


# This is one of the most common errors in computer programming, and not always easy to catch - an index out of bounds error.  This error happens when we try to index into the array at a position that is _larger_ than the array.  Since the computer doesn't have any data in that position, the computer doesn't know what to return and therefore raises an error.

# That's why computer scientists developed a short hand for the while loop, called a for loop:

# In[5]:


listing = [2,3,4,5,6]

for element in listing:
    print(element)


# I started this list at 2 just to make it clear that we iterate _over the elements_ of the list, not an index.  The for loop continues to iterate until the list is out of elements.  That means we can never end up with out of bounds errors.  
# 
# And if we'd like to print the index _and_ the elements we can do so as follows:

# In[6]:


listing = [1,2,3,4,5]

for index, element in enumerate(listing):
    print("The element is",element,"at index",index)


# Notice that we concatenated the element, index variables with the string by using `,`'s.  This will only work inside of a print statement.  If python sees a string and an integer then this won't work in general, so we cannot do the following:

# In[7]:


"thing " + 5


# Notice from the above that with a while loop we can specify _multiple_ exit conditions, and we technically don't need something we can iterate over, like a list.  This means that while loops are capable of being _much_ cheaper from a memory standpoint and much more flexible than for loops.  That said, often times you don't need the extra flexability, and memory is pretty cheap these days, so it's unlikely a list is going to cost you much in terms of performance.
# 
# Let's look at two examples of pieces of code and their running times, in terms of CPU time:

# In[19]:


import random
import time

start = time.time()
summa = 0
index = 0
size = 1000
while index < size:
    summa += random.randint(0, 1000)
    index += 1
    
print(time.time() - start, "seconds")
print(summa/size)


# This code takes the arithmetic mean, defined as:
# 
# $$ \frac{1}{n}  \sum_{i=0}^{n} i $$
# 
# We can also do this with a for loop:

# In[20]:


import random
import time

start = time.time()
summa = 0
index = 0
size = 1000
listing = []
while index < size:
    listing.append(random.randint(0, 1000))
    index += 1

for elem in listing:
    summa += elem
print(time.time() - start, "seconds")
print(summa/size)


# Because we often need to populate a list with elements in a for loop, one of the things Python comes equiped with is the `range` function that iterates over an index _very_ fast.  This more or less makes up for the fact that you need to iterate over a list to use a for loop:

# In[21]:


import random
import time

start = time.time()
summa = 0
for elem in range(1000):
    summa += random.randint(0, 1000)
print(time.time() - start, "seconds")
print(summa/size)


# As you can see, the while loop is still a little bit faster, but the syntax is _so much_ simplier using the for loop.  That difference in complexity can be _very_ important.  Especially because expressing ideas programatically is often hard enough.  Typically there is no need for extra complicated syntax to save a few miliseconds.

# In[ ]:





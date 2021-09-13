#!/usr/bin/env python
# coding: utf-8

# # Computer Science Basics
#    
# Computer Science is the study of computation.  Often times that computation is expressed through hardware and 'software' called a programming language.  Programming languages can take on a number of flavors and styles.
#    
# ## Computation
# 
# You can think of computation sort of like a super set of mathematics.  Anything you can do with mathematics you can do with computation, with a notable exception.  In mathematics you have sets like the real numbers, the complex numbers and even larger more dense infinite sets.  Because everything in a computer is by definition finite, there is a limit on how precise you can make your mathematical computation.  That said, any discrete mathematics will be exactly equivalent to it's counter part computationally.  
# 
# If this sounds vague or confusing, we'll look at a motivating example in Python.
# 
# ## Python Programming Language
# 
# The Python Programming Language is a high level, white spaced language.  Here is an example program:

# In[1]:


print("Hello World")


# The above 'program' is the reason that Python is the programming language for this course.  Python explicit, minimalistic and dynamically typed.  That means writing Python programs is as straight forward as possible.
# 
# Now let's look at an example of what I meant above:

# In[4]:


result = 3 + 7
print(f"The result of 3 + 7 = {result}")


# As you can see, the result of `3 + 7`, as expected is 10.  This is because 3 and 7 both belong to the infinite set called the Natural Numbers, denoted **N**.  Any mathematical operation on **N** will always be exactly the same as if you did the math by hand.  This means we can use Python or almost any programming language, _as_ a calculator.  
# 
# In addition to being able to express any discrete computation, like a calculator or a human would, Python or any computer can express something called the computables.  An example of a computable number we haven't see before in this chapter is `3.15`.  This number is a real number, sometimes denoted by **R**.  However it's important to recognize that there are certain members of **R** a computer cannot accurately represent, at least not completely.  Here's an example of such a number:

# In[5]:


def calculate_digits_of_pi(num_iter=100000):
    k = 1
    summation = 0
    for i in range(num_iter):
        if i % 2 == 0:
            summation += 4/k
        else:
            summation -= 4/k
        k += 2
    return summation

approximation_of_pi = calculate_digits_of_pi()
approximation_of_pi


# As you can see from the above 'algorithm', we calculate an approximation of the digits of pi.  However, the above number is _not_ pi.  The number pi is _infinite_ in it's length.  Since computers are inherently finite, they cannot express all the digits of pi and store them in memory.  Thus pi, a member of **R** is not expressable in the space of computables.  In fact, _any_ irrational number is not expressable in the space of the computables.However, we can work with the computables most of the time.  
# 
# It's all a question of how precise we need to make our calculation.  
# 
# ## Precision In Detail
# 
# The idea of precision is incredibly important in Computer Science.  But it's a concept that also holds a great deal of importance in all of the Sciences and Engineering fields.  You've probably heard the terms is [significant figures](https://en.wikipedia.org/wiki/Significant_figures).  
# 
# **Definition** Significant Figures := The number of significant figures refers to precision.  The more precise the calculation needs to be, the greater the number of significant figures.
# 
# Example:
# 
# Suppose you were looking at the gross domestic product of the united states for 2020 - turns out it's approximately 20.93 trillion according to [statista](https://www.statista.com/statistics/263591/gross-domestic-product-gdp-of-the-united-states/).  
# 
# In this case there are 4 significant digits 20.93.  Of course this isn't an exact measure, but it's _good enough_.  In general the question of precision is _incredibly_ context specific.  What you need varies within and between applications, often times for the _same_ measurement.  
# 
# Your choice of units and significant figures matters a great deal.  For instance, let's say you were a doctor and prescribed a medicine in grams, when the typical dose is in _milligrams_ (1000 milligram == 1 gram).  That might be enough for a _leathal_ dose.  But I digress.
# 
# The point is, sometimes the number of significant digits means, even for irrational numbers, you can get away with _reduced_ precision.  In other words, a computable equivalent to a number that is infinitely long _might_ be okay.  It really all depends.  But most of the time, for science and engineering, you can accept a certain level of being imprecise.  The challenge is making sure you are precise enough.  
# 
# ## Floats
# 
# In general anything with a decimal point is called a floating point number or float for short.  Let's look at some examples of floats and integers, often called ints for short.  

# In[1]:


print(5 + 3)
print(7.14 + 9)
print(9.13 + 10.5)


# As you can see, you can add ints to ints, floats to ints or floats to floats.  
# 
# The third example is probably worth spending a little extra time on.  Does that issue happe every time we add `9.13 + 10.5`?

# In[2]:


9.13 + 10.5


# Looks like it's repeatable.  Is this a mistake?  `9.13 + 10.5` ought to be `19.63`, so where did the `0.000000000000003` come from?
# 
# Well, it turns out that floating point numbers do some _funny_ things sometimes.  If you need 4 signficant digits, with 2 of them after the decimal point, then this is no big deal.  But what if you _need_ all 18 significant digits (there are 18 digits in the above number)?  Then this is certainly a problem because you never know when Python will 'decide' to add a random 3 in your least significant digit.  If you really need all that precision, then this means you _can't_ trust the mathematics you are doing sometimes with the standard float.  
# 
# Not to worry!  There are other versions of the floating point numbers with more precision.  So if we really need that much precision, we are okay.  But why don't we just _automatically_ use that 'better' floating point system _all the time_?
# 
# The answer is because it's expensive.  In the world of computation, everything is about trade offs.  If you want your mathematical systems to be fast, then you _have_ to give up precision.  In some cases, not much precision, in some cases, not much speed, but you are always making that trade off.
# 
# If you had to care about all 18 places all the time, all of the mathematics you did on the computer would be slower.  And that might matter for your system.  
# 
# ## Trading System Example
# 
# Let's say you are running a trading system for the stock market.  In this trading system, you only look at prices.  You don't care about any digits after 3 decimal places (3 places to the right of the decimal point).  And you only care about 3 because of rounding errors which happen some times.  
# 
# Let's do an experiment to see how fast two floating point number systems would be.  We'll see two versions of the add operator to see how fast each version of floating point is.
# 
# First we'll look at `fsum` which is a precise version of sum:

# In[3]:


import math

get_ipython().run_line_magic('timeit', 'math.fsum')


# Next we'll look at regular old sum, which doesn't care as much about precision:

# In[4]:


get_ipython().run_line_magic('timeit', 'sum')


# As you can see, the typical `sum` is about `twice` as fast as the precise sum.  Because the number of loops is the same, they ran about the same number of times.  But it took `sum` _half_ as long to finish.  Also, there was a greater variance in how long it took `fsum` to finish.  With any algorithm, the better one is typically the one that runs faster and more accurately.  So, if we go back to our example -
# 
# What do you think would happen if with the two trading systems?  Consider this:
# 
# If adding takes twice as long and adding is a _fundamental_ operation in trading, then you should assume that all the trades on the slower system will take _at least_ twice as long.  That means traders on the fast system will be able to see the results of their trades, perhaps minutes faster than their counter parts at the firm using the slower system.  That means they can literally watch the other trading firm executing a strategy in real time and _steal it_.  
# 
# This may feel _dishonorable_ but it's 100% legal.  You are seeing all the information that everyone else is seeing.  You just happen to be seeing it first.  But I digress.

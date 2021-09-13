#!/usr/bin/env python
# coding: utf-8

# # Variables and Types
# 
# 
# * Variables and Types
#     * ints
#     * floats
#     * strings
#     * booleans
#     * converting between types
#     * operators
#         
# ## Variables In Python
# 
# The python language allows us to store data in named variables.  These variables hold data, which can either be mutated or not mutated.  Let's take a look at the main examples:
# 
# * int - these are the generic integers
# * float - these are sort of like the "real" numbers from math, but they aren't as dense and they aren't infinite.  We call these the "computables" or the floating point numbers.
# * bool - this type of variable can only be `True` or `False`.
# * string - this type of variable contains "characters" that are strung together.  Strings are different than integers and floats in that they don't represent numbers.
# 
# Examples in code:

# In[1]:


# Integer

x = 0
print(x)

x = x + 7
print(x)

x * 4
print(x)

x /= 5
print(x)


# Here we have a simple program that creates a variable `x` and stores the value `0` in `x`.  This is done through the use of `=`.  Which in a program is not equality, but _assignment_.  Notice that if we want to mutate the stored value of `x` we need to first update the original value by another value and then store the result in the original variable.
# 
# This is captured with the line:
# 
# `x = x + 7`.
# 
# As a counter example, if we simply multiple `x * 4`, but do not update it's value with an assignment statement, the value of x is not updated.  This is because programs are pedantic.  They will only do what you tell them, nothing more and nothing less.  And they will do it _exactly_.  
# 
# Finally, having to write `x = x + whatever` is annoying, so programmers came up with the `operater=` short hand.
# 
# We see that here with `/`, which stands for division.  Specifically, `/=`.  But this will work with _any_ of the mathematical operators we've seen so far.  So:
# 
# * `+=` works
# * `-=` works
# * `*=` works
# * `/=` works
# 
# Now then, we can carry out the same exercise with floating point numbers, we'll use `y` this time, instead of `x` just to keep things fresh:
# 
# 

# In[2]:


# Floats

y = 0.7
print(y)

y = y + 7.1
print(y)

y * 4.8
print(y)

y /= 5.7
print(y)


# As you can see, everything we can do with the integers we can do with the floats!  The only real difference is that floats have a decimal point.  This is how you can tell the difference between the two.  There is nothing new here (very much on purpose), so we'll move onto bools:

# In[3]:


# Booleans

x = True
y = False

print(x and y)
print(x or y)
print(not x)


# Since booleans can only take on one of two values, we just capture both of them above.  The `and`, `or`, and `not` operator may be new to you.  But they should be pretty straight forward.
# 
# As you saw above, plus some additions:
# 
# * True and False = False
# * True and True = True
# * False and False = False
# * True or False = True
# * True or True = True
# * False or False = False
# * not True = False
# * not False = True
# 
# Boolean variables may not seem useful, but they are of _huge_ importance for programming in Python.  In fact, they allow us to do things like this:

# In[4]:


x = True
if x == True:
    print("woah it worked")
else:
    print("something has gone wrong here")


# We'll look more in detail at flow of control in the next section, but for now, keep this in the back of your mind.  Now let's talk about some stuff related to types.
# 
# Finally, let's look at strings:
# 
# A string is a sequence of characters.  Let's look at an example:

# In[46]:


x = "5"

y = "7"

x + y


# The difference between the string `+` and the number `+` is that addition with numbers will lead to addition in the typical way.  When we add strings together, we do something called _concatenation_.  Let's look at a more typical example:

# In[48]:


# Strings

greeting = "Hello there"

greeting += " new friend,"
print(greeting)


# As you can see in the above we can make use of the `+=` operator as well.  In addition to being able to concatenate strings, we can also select substrings with something called an index operator:

# In[49]:


greeting[0]


# The above code selects the index at position zero, otherwise known as the first character of the string.  We can also select substrings with start and stop indices:

# In[51]:


greeting[0:11]


# In the above code we specify the start index, a `:` and the stop index like:
# 
# `string[START INDEX GOES HERE : END INDEX GOES HERE]`.
# 
# Because strings in Python are zero indexed, the end of the index will be a little odd, at first.  So if we want the 5th character, we need to get index 4:

# In[52]:


"abcdefhijklmnopqrstuvwxyz"[4]


# In general, we need the n-1st index if we want the nth character in a string, because of the zero indexing.

# Moving on, suppose you are debugging some code, or you've written something and you aren't sure what it's type is, you can always figure it out with the `type` function.
# 
# Let's look at some examples:

# In[5]:


x = 7

type(x)


# Here we see what the `type` function does - it tells you what type the variable is.  We can also see what `type` returns with:

# In[6]:


type(type(x))


# You might have thought it returns a string, but in fact it returns a type of type 'type'.  This is important because the type, type can have extra information associated with it.  To see that, we are going to introduce another function -  `isinstance`:

# In[7]:


isinstance(x, int)


# The first argument of isinstance is a variable of any type, but the second input _needs_ to be of type, 'type', so you can be sure you are checking for a type.  
# 
# Let's do some experiments now - suppose you did the following:

# In[9]:


y = 7 + 12.8


# What do you think the type of y ought to be?  We can figure this out by calling `type`:

# In[10]:


type(y)


# Okay - what about this code?

# In[11]:


z = "Hello" * 3


# What do we think the type will be now?

# In[12]:


type(z)


# Surprising!  Let's look at the value of z, just to see what's in it:

# In[13]:


z


# Ah!  So multiplication repeats a string `n` times.  Very interesting!  Does `+` work?

# In[14]:


w = 8 + "something"


# Nope!  Python throws an error, showing us that it doesn't work.  So far we've talked about a bunch of stuff, but there is one very special primitive type we haven't talked about yet - `None`.
# 
# The `None` type is a singleton - in that it only has one value, `None`.  So if something is of type `None` then it's just that value.  Different programming languages express this concept differently.  But it generally means the same thing - a lack of value.  
# 
# In particular `None` comes up a lot when we get to functions.  But it also comes up when we get to data analysis - specifically in that context, `None` means missing data.  This can happen when experimental data is either lost, wasn't recorded, or was just never captured.
# 
# Imagine that you are gathering survey data.  And some of the participants don't get to the end of the survey.  In that case, do you throw out the partially filled out surveys?  Probably not!  Survey collection is expensive and difficult.  So the better thing to do is fillin a `None` value for any questions they didn't answer.  
# 
# Let's see an example of a function that returns `None` that you've seen already:

# In[15]:


output = print("hello")


# In[17]:


type(output)


# As you can see, this is the `None` we've been talking about. If we want to check this, we can't use the isinstance we've been talking about already:

# In[20]:


isinstance(output, None)


# That's because `NoneType` isn't a recognized type like `int`.  So we'll need a different technique for this:

# In[21]:


output is None


# Here we've used the `is` operator to figure out that this is `None`.  The reason we make use of the `is` operator because it checks for _true_ equality.  Let me show you what I mean!

# In[23]:


x = 5.0
y = 3 + 2

x is y


# Last time I checked 5.0 _equals_ 3+2, we can even check that it's the case with the double equals:

# In[24]:


x == y


# So what's going on here?!  Well, the `is` operator is _stronger_ than `==`.  It specifically asks, are these two things _exactly_ the same.  Do they have the same type?  Do they have the same value?  The answer is no in the case of `x` and `y`.  But it is in the case of `output` and `None`.
# 
# Before we leave this section, there is one more topic we need to cover:
# 
# Converting between types - sometimes this is called type casting.  With the Python basic types, we'll do this via the types themselves:

# In[26]:


x = 5.0
print(type(x))
x = int(x)
print("Type of x after casting", type(x))


# As you can see, we can type cast explicitly by using the type as a function, with a variable as input.  This works for all the basic types, when the conversion is defined:

# In[27]:


x = 5.0
print(int(x))
print(str(x))
print(bool(x))


# Here we've shown how the value `5.0` get's cast.  Next let's look at a special value `0`:

# In[28]:


x = 0.0
print(int(x))
print(str(x))
print(bool(x))


# Notice that `0` gets cast to `False`, which is only true for that value:

# In[29]:


x = 19.5
print(int(x))
print(str(x))
print(bool(x))


# As you can see, any other value will be cast to True.  Even values less than 1.

# In[30]:


x = 0.5
print(int(x))
print(str(x))
print(bool(x))


# Notice in the above example, since 0.5 is less than one, it gets cast to zero.  Does this hold for all values less than one but great than zero?

# In[31]:


x = 0.7
print(int(x))
print(str(x))
print(bool(x))


# Let's look at one more example:

# In[32]:


x = 0.99999
print(int(x))
print(str(x))
print(bool(x))


# As you can see, when casting between `floats` and `ints`, Python rounds down.  Now let's try converting an int to it's other respective types:

# In[33]:


x = 1
print(float(x))
print(str(x))
print(bool(x))


# As you can see, things happen as expected, based on the above examples.  Let's see what happens at zero, for consistency:

# In[34]:


x = 0
print(float(x))
print(str(x))
print(bool(x))


# As expected!  And let's try some big negative number:

# In[35]:


x = -12391759182731
print(float(x))
print(str(x))
print(bool(x))


# Looks consistent! Alright, let's move onto strings:

# In[36]:


x = "hello"
print(int(x))
print(float(x))
print(bool(x))


# As you can see here, strings with characters don't convert to numbers.  Because how would that even work?  Let's look at bool, just to see what happens there:

# In[37]:


x = "hello"
print(bool(x))


# Looks like strings resolve to `True`, however this isn't true for one special string - the empty string, denoted by `''`.  This is the string of _length_ zero.  It has no characters.  Since zero is false, a _zero_ character string also ends up this way:

# In[38]:


x = ''
print(bool(x))


# Before we leave strings, let's see what happens if we try to convert strings of numbers into numbers:

# In[39]:


x = '5'
print(int(x))
print(float(x))
print(bool(x))


# This, perhaps surprisingly, works.  That's because the operations `int` and `float` _undo_ the conversion to string, as we saw in the first couple of examples, when we converted numbers _to_ strings.  Finally, let's look at a floating point number captured in a string:

# In[40]:


x = '5.12387'
print(int(x))
print(float(x))
print(bool(x))


# Interestingly, the conversion to an `int` fails!  That's because Python is not smart enough to figure out this is a float wrapped in a string.  Let's see if the others work:

# In[41]:


x = '5.12387'
print(float(x))
print(bool(x))


# Yup!  They do.  What if we really wanted to see the above code run with no errors?  We could convert to float first and then to a int:

# In[42]:


x = '5.12387'
print(int(float(x)))
print(float(x))
print(bool(x))


# Last but not least, let's look at booleans:

# In[43]:


x = True
print(int(x))
print(float(x))
print(str(x))


# In[44]:


x = False
print(int(x))
print(float(x))
print(str(x))


#!/usr/bin/env python
# coding: utf-8

# # Numpy Basics
# 
# Probably the biggest shift when getting started with data science is the syntax of numpy and pandas because it differs so much from other programming paradigms.  In this section we will walk through some numpy basics:
# 
# * why numpy?
# * introduction to tensors
# * numpy shapes
# * numpy slicing
# * numpy querying
# * linear algebra in numpy

# ## Why Numpy?

# Technically, anything you can do in numpy you can do in plain old python.  And arguably the syntax will be easier to understand, that is, unless you use numpy as it is intended.  Numpy _can_ be used for all the basic stuff that you'll find most of the examples for on the internet.  But it's really _intended_ to be used for a new paradigm of programming.  One that's caught on in the statistical and deep learning communities (which have at least some overlap).  
# 
# Numpy's api and computation is optimized for the manipulation of algebraic structures.  You can use it to do most of the computation that you can do with vanilla Python, or any other programming lanugage.  But you probably shouldn't.  We can think of the numpy api as sort of a directed language.  It's not quiet that, because numpy is mostly "about" syntax change.  You are thinking about the world from a difference lense.  But I digress.
# 

# 
# * incredible speed - numpy is _much_ faster than vanilla python (it can even outperform Java sometimes)
# * a beautiful and well organized api
# * tons of utility functions
# * amazing documentation
# * it's completely free (whaaaaat)

# To really understand numpy and the power it brings, we need to understand tensors.  Because without them, numpy honestly doesn't make much sense, at least at first.  And even once you start to get used to the syntax, without the mental model of a tensor, you'll completely miss the point of using it.

# ## Tensors

# Tensors are some of the most powerful objects around.  In fact, this book is basically just a "how do I use tensors" most of the time.  The chapter on linear regression?  That's just about tensors.  The chapter on classification?  More applications of tensors.  Much of machine learning is built on tensors.  Specifically, on matrices.  Because I define the matrix in another chapter, I won't go into a ton of detail about what they are, or how to use them.

# * scalars
# * vectors
# * matrices
# * order-3 tensors and higher

# A scalar is an order zero tensor - because it's just a single number, like say the number `5`.  A vector is a one dimensional collection of numbers representing data or an equation, like: 
# 
# $$ \begin{pmatrix}
# 1  \\
# 4  \\
# 7 
# \end{pmatrix}
# $$
# 

# A matrix is a two dimensional collect of numbers representing a system of equations, like:
# 
# $$
# \begin{pmatrix}
# 1 & 2 & 3 \\
# 4 & 5 & 6 \\
# 7 & 8 & 9
# \end{pmatrix}
# $$
# 

# An order three tensor looks like a data cube.  There is no easy way to show such a cube in latex, so you'll have to imagine this to some extent:
# 
# $$ A_{1} = 
# \begin{pmatrix}
# 1 & 2 & 3 \\
# 4 & 5 & 6 \\
# 7 & 8 & 9
# \end{pmatrix}
# $$
# 
# $$ A_{2} = 
# \begin{pmatrix}
# 3 & 2 & 3 \\
# 7 & 6 & 6 \\
# 7 & 2 & 9
# \end{pmatrix}
# $$
# 
# $$ A_{3} = 
# \begin{pmatrix}
# 1 & 2 & 3 \\
# 7 & 6 & 4 \\
# 6 & 2 & 19
# \end{pmatrix}
# $$
# 

# Now imagine $A_{1}, A_{2}, A_{3}$ as one object.  This is an order three tensor.  It has three axes - $(i,j,k)$ and you can specify elements across these three axes.  So $(0,0,0) = 1$, $(1,0,0) = 4$, and $(3,0,3) = 6$.  Here the i is the row index, j is the column index and k is the matrix index.  You can also do this for order 4 and up to n, where n is any finite natural number you like.  

# ## Numpy Shapes

# Now that you know what a tensor is, the syntax of numpy will seem obvious and straight forward.  Let's start by showing how to represent each of the tensors we've discussed thus far:

# In[2]:


# order 0 tensor
import numpy as np

scalar = np.array([1])
print(scalar)


# You may think we've done nothing new here.  But actually we have!  For starters, numpy attaches types to anything passed into it.  And it does this _implicitly_.  You never have to name the types.  That by itself would be a feat of engineering prowess.  Let's see what I'm talking about:

# In[3]:


scalar.dtype


# The `dtype` property tells us what kind of data is in our tensor.  Since there are mathematical consequences to what's in our tensor, it's best to define one type per tensor.  Usually floats are the most flexible.  Of course, you can define a tensor with multiple types.  But for any serious mathematical computation, this is discouraged.  However, there are lots of programming instances when defining multiple types in a data structure is useful and important, which is why this paradigm is supported:

# In[4]:


np.array(["hello", 1])


# Now that we have seen an order 0 tensor and an order 1 tensor, by accident, let's define another order 1 tensor, called a vector:

# In[5]:


vector = np.array([1, 4, 7])
print(vector)


# There are a few things to note here:
# 
# 1. a vector is a collection of scalars.
# 2. a vector represents a mathematical object, not just an array.
# 
# Because this is a mathematical object, we can do things like this:

# In[6]:


vector_one = np.array([1, 4, 7])
vector_two = np.array([2, 4, 6])

np.matmul(vector_one, vector_two.T)


# If you've ever taken a linear algebra course the answer that's produced will seem surprising.  That's because technically numpy defaults to an array of scalars for a one dimensional array passed to the `np.array` method, rather than a vector.  The difference here is important.
# 
# Because algebraic objects are defined in part by the algebraic operators attached to them, this detail matters.  Specifically, here the "multiplication" attached to our vectors is the inner product in this case.  If we want the outer product, which is what most folks who have taken linear algebra would expect, then we need to tell numpy that we are working with tensors or order 1 aka vectors and not a collection of scalars.
# 
# We do that by using the `reshape` method a powerful tool that will allow us to represent tensors of any order we like.  But first let's start with the basics of turning a collection of scalars into an order 1 tensor, aka a vector:

# In[7]:


vector_one = np.array([1, 4, 7])
vector_two = np.array([2, 4, 6])

vector_one = vector_one.reshape(3, 1)
vector_two = vector_two.reshape(1, 3)
print("vector one:")
print(vector_one)
print("vector two:", vector_two)
print("result:")
np.matmul(vector_one, vector_two)


# By reshaping our vectors to the appropriate shapes, we were able to produce a matrix!  This is a general fact of linear algebra - you can get a matrix by applying a matrix multiplication (`matmul`), also known as the outer product, to two vectors.  This "trick" of taking two lower dimensional tensors to create a higher order one will actually work for _any_ tensor we like.  If we want to recover an order 3 tensor we simply need to multiply a matrix by a vector.  That's because the order is additive, by tensor product!  Let's see an example:

# In[8]:


a = np.array([[ 5, 1 ,3], 
              [ 1, 1 ,1], 
              [ 1, 2 ,1]])
b = np.array([1, 2, 3])
print(np.tensordot(a, b, axes=0))


# Here `a` is a matrix, `b` is a tensor.  And by taking the tensor product of the two of them, we recover an order 3 tensor!  Notice we have to provide an axes or the `tensorproduct` method.  This is because a tensor product can be defined on any order.  We've already seen an order 1 tensor product, the inner product.  And we've seen an order 2 tensor product, the outer product.  In higher spaces, we generally refer to the product as simply the tensor product where the order comes from context.  However, please take care to be clear about the shapes of your tensors, otherwise you'll end up doing the _wrong multiplication_.  
# 
# I'll leave as an exercise creating tensors of order 4, 5, and 6.  Happy multiplying!

# ## Numpy Slicing

# Now that we've seen how to create our tensors the next step is to be able to index into them.  The number of axes that you specify will determine how deep a slice you get back.  For instance, if you are working with an order 3 tensor and you specify one axes, you'll get back a matrix.  If you specify two, you'll get back a vector.  And if you specify all three you'll get back a scalar.  Let's see some examples:

# In[9]:


# Getting back a matrix
a = np.array([[ 5, 1 ,3], 
              [ 1, 1 ,1], 
              [ 1, 2 ,1]])
b = np.array([1, 2, 3])
order_3_tensor = np.tensordot(a, b, axes=0)

order_3_tensor[:, :, 0]


# The numpy syntax for slicing may seem somewhat familar, but maybe not.  In vanilla Python you can choose a number of elements by slicing:

# In[10]:


listing = list(range(20))

print(listing[:])


# The `[:]` just gives back a "slice" that's equal to the whole array, because we didn't specify any start an end.  But if say we just wanted the last 3 elements we can do this:

# In[11]:


listing = list(range(20))

print(listing[-3:])


# Of course, we can fully specify the start and end as well:

# In[12]:


listing = list(range(20))

print(listing[5:9])


# Of course, that's only for a one dimensional array.  In numpy, we are dealing with _many_ dimensions, which is why the syntax looks different.  In the example above we had:
# 
# `order_3_tensor[:, :, 0]`

# The first axis is selected completely so like with vanilla Python lists, we simply do `[:` for the whole thing.  Next we get the entire second axis so we have: `[:, :`.  And finally, we just want the first "element" along the third axis: `[:, :, 0]`.  At first, this syntax seems confusing to everyone.  But once it clicks, by understanding numpy arrays as tensors, then everything in the syntax becomes _obvious_.
# 
# Let's move onto our second example.  This time we'll get back just a vector:

# In[13]:


# Getting back a vector
a = np.array([[ 5, 1 ,3], 
              [ 1, 1 ,1], 
              [ 1, 2 ,1]])
b = np.array([1, 2, 3])
order_3_tensor = np.tensordot(a, b, axes=0)

order_3_tensor[:, 0, 0]


# As you can see, we've specified _two_ axes and therefore, we get back an order 1 tensor.  Now, let's move onto the final example and get back just a scalar:

# In[14]:


# Getting back a scalar
a = np.array([[ 5, 1 ,3], 
              [ 1, 1 ,1], 
              [ 1, 2 ,1]])
b = np.array([1, 2, 3])
order_3_tensor = np.tensordot(a, b, axes=0)

order_3_tensor[0, 0, 0]


# Something to notice, the first order 2 slice of our order 3 tensor is just the matrix `a`.  This is because the first element in our vector `b` is a 1.  I'll leave as an exercise, to see if you can write a slice that recovers the first row of matrix a.  Your answer should look like this:
# 
# `[5, 1, 3]`
# 
# Here is the starter code:

# In[15]:


a = np.array([[ 5, 1 ,3], 
              [ 1, 1 ,1], 
              [ 1, 2 ,1]])
b = np.array([1, 2, 3])
order_3_tensor = np.tensordot(a, b, axes=0)

# put in your slices here
#order_3_tensor[, , ]


# Note: there is more than one way to recover the row in question.
# 
# ## Numpy Querying
# 
# So far we've looked at the mathematical advantages of numpy.  There was another claim I made, that numpy is blazing fast.  And I wasn't kidding.  Compare numpy with vanilla python on _many_ operations and you'll see it's power.  That's because numpy is written in C with it's api specified in Python.  This means it can take advantage of the high level-ness of Python, while keeping the performance of C.  Truly, numpy is a modern marvel.
# 
# Let's see some examples of numpy's performance in action:

# In[16]:


get_ipython().run_line_magic('timeit', 'array = np.random.normal(0, 1, size=10000)')


# In[18]:


import random

get_ipython().run_line_magic('timeit', '[random.gauss(0, 1) for _ in range(10000)]')


# As you can see, numpy is an _order_ of magnitude faster.  There are a lot of examples similar to this.  We'll look at just a few more:

# In[19]:


array_one = np.random.normal(0, 1, size=10000)
array_two = np.random.normal(0, 1, size=10000)


# In[20]:


get_ipython().run_line_magic('timeit', 'array_one + array_two')


# In[22]:


array_one = [random.gauss(0, 1) for _ in range(10000)]
array_two = [random.gauss(0, 1) for _ in range(10000)]


# In[24]:


get_ipython().run_line_magic('timeit', '[array_one[index] + array_two[index] for index in range(len(array_one))]')


# This time numpy is _2 orders_ of magnitude faster.  And the syntax was _much_ clearer.  Granted, it is less clear what we are doing, unless you know the numpy api.  Whenever you add two vectors in numpy, this adds each element together.  So beware!  You can also do multiplication just as easily:

# In[25]:


array_one = np.random.normal(0, 1, size=10000)
array_two = np.random.normal(0, 1, size=10000)


# In[26]:


get_ipython().run_line_magic('timeit', 'array_one * array_two')


# In[27]:


array_one = np.random.normal(0, 1, size=10000)
array_two = np.random.normal(0, 1, size=10000)


# In[28]:


get_ipython().run_line_magic('timeit', '[array_one[index] * array_two[index] for index in range(len(array_one))]')


# As you can see the orders of magnitude are similar for multiplication as they were for addition.  This is actually a _much_ bigger deal than may be obvious from these two examples.  All of linear algebra relies on these two operations.  That means linear regression, logistic regression, neural networks are all around 100 times faster implemented with numpy as compared to vanilla Python.  Of course, that is a blanket statement.  There are things you can do to make vanilla Python move faster.  And you can implement numpy poorly.  So this is a statement that needs to be taken with a grain of salt.  But still, numpy is faster for the things that matter to folks working in statistics and machine learning.  And that's just a fact.
# 
# Since numpy is _so fast_.  It can actually be used as a minimal in memory database.  Here we'll go over some of the basics for querying data in numpy.  Some of the syntax here will be confusing at first, but with time and practice it will become clear.
# 
# Let's look at a simple example of selecting a specific section of elements:

# In[29]:


array = np.random.normal(0, 1, size=10000)

len(array[array > 0.5])/len(array)


# I did a little stylizing here returning the percentage of the array over 0.5.  But basically this shows us the querying syntax.  This syntax is definitely _not_ obvious on first blush.  That said, once you get used to it, it's pretty powerful.  What's going on here is the following:
# 
# the inner bit of syntax: `array > 0.5` is a boolean statement.  That is, implicitly every element of the array is checked for the condition, element of array greater than 0.5.  If the element meets the condition `True` is returned, otherwise False is returned.  
# 
# 

# Then a boolean array is passed to the array as a slice:
# 
# `array[boolean statement goes here]`.

# Then indices where the index in question is `True` is returned.  Any indices that return `False` are ommited.  In this way, you can "semantically slice" your array.  To make this concrete, let's look at just the result of `array > 05`:

# In[30]:


array > 0.5


# As you can see, this is just an array of boolean values.  And if we counted up the number of times that resultant array has the value `True` it would equal the size of the semantically sliced array: `array[array > 0.5]`:

# In[31]:


print((array > 0.5).astype(int).sum())
print(len(array[array > 0.5]))


# The way I counted the number of `True`'s may be confusing, so let's look at that: 
# 
# By casting the `True`'s and `False`'s as type `int` we turn the `True`'s into `1`'s and the `False`'s into `0`'s. 
# 
# We've show a simple example of how to query with numpy, but these examples can be as sophisticated as they are in any SQL dialect.  Next let's look at a complex querying statement - one with two statements:
# 
# Here we will select all the elements between 0.5 and 0.7 only

# In[33]:


array = np.random.normal(0, 1, size=10000)

result = array[
    (array > 0.5) &
    (array < 0.7)
]
len(result)/len(array)


# Notice here the use of the `&` symbol.  This stands for 'and' when dealing with boolean statements.  Specifically those where both numbers are represented as binary.  Therefore we refer to `&` as `binary and`.  
# 
# The way this operator works is as follows:
# 
# 1 `&` 1 = 1
# 
# 1 `&` 0 = 0
# 
# 0 `&` 1 = 0
# 
# If we have longer binary numbers, then we simply apply the `&` element wise across the "string" of binary numbers:
# 
# 10 `&` 01 = 00
# 
# There are other "binary" operators:
# 
# * OR = `|`
# * NOT = `~`
# 
# With these three operators we can create very sophisticated queries into our numpy arrays.  For instance, let's get all the numbers between 0.5 and 0.7 or the numbers less than 0.1:

# In[34]:


result = array[
    ((array > 0.5) &
    (array < 0.7)) |
    (array < 0.1)
]
len(result)/len(array)


# Often times the `~` operator may seem unnecessary, but if you're querying from a variable it can make life very easy:

# In[35]:


original_query = ((array > 0.5) & (array < 0.7)) | (array < 0.1)
result = array[~original_query]
len(result)/len(array)


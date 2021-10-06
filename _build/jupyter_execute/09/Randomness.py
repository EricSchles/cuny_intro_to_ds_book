#!/usr/bin/env python
# coding: utf-8

# In[2]:


path_data = '../../../assets/data/'
import numpy as np

import matplotlib
matplotlib.use('Agg')
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')


# # Randomness
# 
# In the previous chapters we developed skills needed to make insightful descriptions of data. Data scientists also have to be able to understand randomness. For example, they have to be able to assign individuals to treatment and control groups at random, and then try to say whether any observed differences in the outcomes of the two groups are simply due to the random assignment or genuinely due to the treatment.
# 
# In this chapter, we begin our analysis of randomness. To start off, we will use Python to make choices at random. In `numpy` there is a sub-module called `random` that contains many functions that involve random selection. One of these functions is called `choice`. It picks one item at random from an array, and it is equally likely to pick any of the items. The function call is `np.random.choice(array_name)`, where `array_name` is the name of the array from which to make the choice.
# 
# Thus the following code evaluates to `treatment` with chance 50%, and `control` with chance 50%.

# In[3]:


two_groups = np.array(['treatment', 'control'])
np.random.choice(two_groups)


# The big difference between the code above and all the other code we have run thus far is that the code above doesn't always return the same value. It can return either `treatment` or `control`, and we don't know ahead of time which one it will pick. We can repeat the process by providing a second argument, the number of times to repeat the process.

# In[4]:


np.random.choice(two_groups, 10)


# A fundamental question about random events is whether or not they occur. For example:
# 
# - Did an individual get assigned to the treatment group, or not?
# - Is a gambler going to win money, or not?
# - Has a poll made an accurate prediction, or not?
# 
# Once the event has occurred, you can answer "yes" or "no" to all these questions. In programming, it is conventional to do this by labeling statements as True or False. For example, if an individual did get assigned to the treatment group, then the statement, "The individual was assigned to the treatment group" would be `True`. If not, it would be `False`.

# <h2>Booleans and Comparison</h2>
# 
# In Python, Boolean values, named for the logician [George Boole](https://en.wikipedia.org/wiki/George_Boole), represent truth and take only two possible values: `True` and `False`. Whether problems involve randomness or not, Boolean values most often arise from comparison operators. Python includes a variety of operators that compare values. For example, `3` is larger than `1 + 1`.

# In[4]:


3 > 1 + 1


# The value `True` indicates that the comparison is valid; Python has confirmed this simple fact about the relationship between `3` and `1+1`. The full set of common comparison operators are listed below.
# 
# | Comparison         | Operator | True example | False Example |
# |--------------------|----------|--------------|---------------|
# | Less than          | <        | 2 < 3        | 2 < 2         |
# | Greater than       | >        | 3 > 2        | 3 > 3         |
# | Less than or equal | <=       | 2 <= 2       | 3 <= 2        |
# | Greater or equal   | >=       | 3 >= 3       | 2 >= 3        |
# | Equal              | ==       | 3 == 3       | 3 == 2        |
# | Not equal          | !=       | 3 != 2       | 2 != 2        |

# Notice the two equal signs `==` in the comparison to determine equality. This is necessary because Python already uses `=` to mean assignment to a name, as we have seen. It can't use the same symbol for a different purpose. Thus if you want to check whether 5 is equal to the 10/2, then you have to be careful: `5 = 10/2` returns an error message because Python assumes you are trying to assign the value of the expression 10/2 to a name that is the numeral 5. Instead, you must use `5 == 10/2`, which evaluates to `True`.

# In[5]:


5 = 10/2


# In[6]:


5 == 10/2


# An expression can contain multiple comparisons, and they all must hold in order for the whole expression to be `True`. For example, we can express that `1+1` is between `1` and `3` using the following expression.

# In[7]:


1 < 1 + 1 < 3


# The average of two numbers is always between the smaller number and the larger number. We express this relationship for the numbers `x` and `y` below. You can try different values of `x` and `y` to confirm this relationship.

# In[8]:


x = 12
y = 5
min(x, y) <= (x+y)/2 <= max(x, y)


# <h2>Comparing Strings</h2>
# 
# Strings can also be compared, and their order is alphabetical. A shorter string is less than a longer string that begins with the shorter string.

# In[9]:


'Dog' > 'Catastrophe' > 'Cat'


# Let's return to random selection. Recall the array `two_groups` which consists of just two elements, `treatment` and `control`. To see whether a randomly assigned individual went to the treatment group, you can use a comparison:

# In[6]:


np.random.choice(two_groups) == 'treatment'


# As before, the random choice will not always be the same, so the result of the comparison won't always be the same either. It will depend on whether `treatment` or `control` was chosen. With any cell that involves random selection, it is a good idea to run the cell several times to get a sense of the variability in the result.

# <h2>Comparing an Array and a Value</h2>
# 
# Recall that we can perform arithmetic operations on many numbers in an array at once.  For example, `make_array(0, 5, 2)*2` is equivalent to `make_array(0, 10, 4)`.  In similar fashion, if we compare an array and one value, each element of the array is compared to that value, and the comparison evaluates to an array of Booleans.

# In[7]:


tosses = np.array(['Tails', 'Heads', 'Tails', 'Heads', 'Heads'])
tosses == 'Heads'


# The `numpy` method `count_nonzero` evaluates to the number of non-zero (that is, `True`) elements of the array.

# In[8]:


np.count_nonzero(tosses == 'Heads')


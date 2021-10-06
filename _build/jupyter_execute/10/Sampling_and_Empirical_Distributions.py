#!/usr/bin/env python
# coding: utf-8

# In[2]:


path_data = '../../assets/data/'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
get_ipython().run_line_magic('matplotlib', 'inline')


# # Sampling and Empirical Distributions
# An important part of data science consists of making conclusions based on the data in random samples. In order to correctly interpret their results, data scientists have to first understand exactly what random samples are.
# 
# In this chapter we will take a more careful look at sampling, with special attention to the properties of large random samples. 
# 
# Let's start by drawing some samples. Our examples are based on the <code><a href="../../data/top_movies.csv">top_movies.csv</a></code> data set.

# In[5]:


top = pd.read_csv(path_data + 'top_movies.csv')
top


# <h2>Sampling Rows of a Table</h2>
# 
# Each row of a data table represents an individual; in `top`, each individual is a movie. Sampling individuals can thus be achieved by sampling the rows of a table.
# 
# The contents of a row are the values of different variables measured on the same individual. So the contents of the sampled rows form samples of values of each of the variables.

# <h2>Deterministic Samples</h2>
# 
# When you simply specify which elements of a set you want to choose, without any chances involved, you create a *deterministic sample*.
# 
# You have done this many times, for example by using `take`:

# In[6]:


top.take(np.array([3, 18, 100]))


# You have also used `where`:

# In[11]:


top[top["Title"].str.contains("Harry Potter")]


# While these are samples, they are not random samples. They don't involve chance.

# <h2>Probability Samples</h2>

# For describing random samples, some terminology will be helpful.
# 
# A *population* is the set of all elements from whom a sample will be drawn.
# 
# A *probability sample* is one for which it is possible to calculate, before the sample is drawn, the chance with which any subset of elements will enter the sample.
# 
# In a probability sample, all elements need not have the same chance of being chosen. 
# 
# <h2>A Random Sampling Scheme</h2>
# 
# For example, suppose you choose two people from a population that consists of three people A, B, and C, according to the following scheme:
# 
# - Person A is chosen with probability 1.
# - One of Persons B or C is chosen according to the toss of a coin: if the coin lands heads, you choose B, and if it lands tails you choose C.
# 
# This is a probability sample of size 2. Here are the chances of entry for all non-empty subsets:
# 
#     A: 1 
#     B: 1/2
#     C: 1/2
#     AB: 1/2
#     AC: 1/2
#     BC: 0
#     ABC: 0
# 
# Person A has a higher chance of being selected than Persons B or C; indeed, Person A is certain to be selected. Since these differences are known and quantified, they can be taken into account when working with the sample. 

# <h2>A Systematic Sample</h2>
# 
# Imagine all the elements of the population listed in a sequence. One method of sampling starts by choosing a random position early in the list, and then evenly spaced positions after that. The sample consists of the elements in those positions. Such a sample is called a *systematic sample*. 
# 
# Here we will choose a systematic sample of the rows of `top`. We will start by picking one of the first 10 rows at random, and then we will pick every 10th row after that.

# In[14]:


"""Choose a random start among rows 0 through 9;
then take every 10th row."""

start = np.random.choice(np.arange(10))
top.take(np.arange(start, top.shape[0], 10))


# Run the cell a few times to see how the output varies. 
# 
# This systematic sample is a probability sample. In this scheme, all rows have chance $1/10$ of being chosen. For example, Row 23 is chosen if and only if Row 3 is chosen, and the chance of that is $1/10$. 
# 
# But not all subsets have the same chance of being chosen. Because the selected rows are evenly spaced, most subsets of rows have no chance of being chosen. The only subsets that are possible are those that consist of rows all separated by multiples of 10. Any of those subsets is selected with chance 1/10.  Other subsets, like the subset containing the first 11 rows of the table, are selected with chance 0.

# <h2>Random Samples Drawn With or Without Replacement</h2>
#  
# In this course, we will mostly deal with the two most straightforward methods of sampling. 
# 
# The first is random sampling with replacement, which (as we have seen earlier) is the default behavior of `np.random.choice` when it samples from an array. 
# 
# The other, called a "simple random sample", is a sample drawn at random *without* replacement. Sampled individuals are not replaced in the population before the next individual is drawn. This is the kind of sampling that happens when you deal a hand from a deck of cards, for example. 
# 
# In this chapter, we will use simulation to study the behavior of large samples drawn at random with or without replacement.

# Drawing a random sample requires care and precision. It is not haphazard, even though that is a colloquial meaning of the word "random". If you stand at a street corner and take as your sample the first ten people who pass by, you might think you're sampling at random because you didn't choose who walked by. But it's not a random sample – it's a *sample of convenience*. You didn't know ahead of time the probability of each person entering the sample; perhaps you hadn't even specified exactly who was in the population.

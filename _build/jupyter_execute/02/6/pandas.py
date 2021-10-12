#!/usr/bin/env python
# coding: utf-8

# # Pandas Basics
# 
# Much like numpy can be used to query and analyze data, pandas can do the same thing!  The reason that both tools are used in the data science community is that they fill different requirements and excel at different things.  In this lecture we will be learning more about pandas and it's strengths, specifically:
# 
# * Pandas versus Numpy
# * Pandas indexes
# * Working with data in Pandas
# * SQL Introduction
# * Querying DataFrames
# * Merging DataFrames
# * Aggregations
# 
# ## Pandas versus Numpy
# 
# In the last lecture we learned about Numpy and it's power for making Python very fast.  We saw how to query data, as well as learned how Numpy "thinks" about data, as a tensor.  In this lecture we will look at Pandas, which thinks about data primarily like a database table.  This is because there are obvious primitives for dealing with one dimensional tensors, called `Series` and obvious primitives for dealing with two dimensional tensors called a `DataFrame`, but there are no obvious primitives for dealing with "higher order" tensors in pandas.  You can do some things for creating higher order tensors in pandas, but honestly it's kind of tough to work with that set of primitives.
# 
# While pandas is limited in the order of dimensions it can represent, most data is either one dimensional or two dimensional anyway, or at the very least can be decomposed to an order 1 or order 2 tensor, so this isn't as much of a restriction as you might think.  In this way you can think of pandas as "specializing" in the typical case and not worrying about the exotic cases.
# 
# Additionally, generally speaking pandas is somewhat slower than numpy.  For this reason it is possible to access numpy equivalents of any of the pandas data structures, allowing you to access numpy's speed, while making use of pandas ease of use, in some cases.  That said, not all pandas operations can be done with the numpy objects.
# 
# Let's look at some simple examples of how to do things in numpy and equivalently in pandas:

# In[1]:


import numpy as np
import time

start = time.time()
vector_one = np.array([1, 4, 7])
vector_two = np.array([2, 4, 6])

print("Result", np.matmul(vector_one, vector_two.T))
print("took ", time.time() - start, "seconds")


# In[2]:


import pandas as pd

start = time.time()
series_one = pd.Series(vector_one)
series_two = pd.Series(vector_two)

print("Result", series_one.dot(series_two.T))
print("took", time.time() - start, "seconds")


# As you can see the numpy version is an entire order of magnitude faster.  But the pandas version is a little bit easier to read.
# 
# Next let's look at how to slice pandas versus numpy data structures:

# In[3]:


array = np.random.normal(0, 1, size=10000)

start = time.time()
print("Result", len(array[array > 0.5])/len(array))
print("took", time.time() - start, "seconds")


# In[4]:


series = pd.Series(array)

start= time.time()
print("Result", len(series[series > 0.5])/len(array))
print("took", time.time() - start, "seconds")


# So as you can see, numpy flatly beats pandas for speed.  However, there are two ways in which pandas is the better choice.  First, look at the number of public methods associated with a pandas Series versus a numpy order 1 tensor:

# In[5]:


numpy_methods = [method for method in dir(array) if "_" not in method]
pandas_methods = [method for method in dir(series) if "_" not in method]
print(len(numpy_methods))
print(len(pandas_methods))


# It should be clear, that you can just do _a lot_ more with a pandas series out of the box than a numpy order 1 tensor.  While this isn't always a good thing, it's worth keeping in mind the strengths and deficiencies of both frameworks.
# 
# ## Pandas Indexes
# 
# Pandas dataframe come equipped with three indexes:
# * an index for columns
# * an index for rows
# * an ordering for rows that serves as in implicit index.
# 
# The third index is the least forward without an example, and we'll look at it soon.
# 
# Let's look at a motivating example for the rows and columns first:

# In[6]:


import pandas as pd

supply_matrix = np.random.rand(3,3) * 100
demand_vector = np.random.rand(3) * 100

df = pd.DataFrame(supply_matrix)
df.columns = ["Manufacturing", "Technology", "Real Estate"]
df


# As you can see the columns are listed above the dataframe's data and give us information how each column is semantically named.  If you've ever seen an excel spreadsheet, a database table or a CSV, this is carries the same meaning.
# 
# Additionally there is a row index as shown on the left hand side of the dataframe.  This can either be a simple enumeration of the columns, indexed by the natural numbers, or it can take on a semantic meaning as follows:

# In[7]:


import pandas as pd

supply_matrix = np.random.rand(3,3) * 100

df = pd.DataFrame(supply_matrix)
df.columns = ["Manufacturing", "Technology", "Real Estate"]
df.index = ["Manufacturing", "Technology", "Real Estate"]
df


# But typically it is the former rather than the latter which is used for the row index.  Let's return to our previous example and show the "third" index:

# In[8]:


import pandas as pd

supply_matrix = np.random.rand(3,3) * 100

df = pd.DataFrame(supply_matrix)
df.columns = ["Manufacturing", "Technology", "Real Estate"]
df


# In[9]:


df = df.sort_values("Manufacturing")
df


# As you can see, now the row index is inconflict with order in which the rows appear.  This means we can query for the first row in two ways:

# In[10]:


df.iloc[0]


# In[11]:


df.loc[2]


# Notice these two ways of selecting the first row in the dataframe differed in which index they use, but return the same information.  This will become especially important when we move onto merging dataframes, because the row index is used rather than the "implicit" third index, defined by the order the data appears in the dataframe.  This explicit row index _can_ be mutated of course, but need not be when a mutation to the ordering of data occurs.  This may seem complex, but can be desirable, especially given the ability to control when and if this explicit row index is updated.
# 
# ## Working With Data In Pandas
# 
# One of pandas greatest strengths is it's ability to easily read in data and dump out data.  Let's look at an example:

# In[12]:


supply_matrix = np.round(np.random.rand(500,3) * 100, 2)

df1 = pd.DataFrame(supply_matrix)
df1.columns = ["Manufacturing", "Technology", "Real Estate"]
df1.to_csv("economy.csv", index=False)


# Here we choose not to save our index to the csv which is why `index=False`, this tells the method to not save the index as well, just the data.  Now let's see how to read in the dataframe:

# In[13]:


df2 = pd.read_csv("economy.csv")
df2.equals(df1)


# We can also read csv's directly from the internet with the same method:

# In[ ]:


churn_df = pd.read_csv("https://raw.githubusercontent.com/EricSchles/datascience_book/master/Churn_Modelling.csv")
churn_df


# As you can see, all we need to do is supply a url pointing to a csv and we are all set!  In addition to being able to save to csvs and read from csvs, we can also read data directly from a database into pandas!  This is why pandas is sometimes thought of as an "in-memory" database.
# 
# For this we are going to need a connection object to the database and a relevant query:

# In[14]:


import pandas as pd
import sqlite3 as sql
connection = sql.connect("economy.db")
df = pd.read_sql_query("SELECT * FROM industry", connection)
df.head()


# As you can see, we can pull in any information we might want from a database connect, directly into python.  This is a huge asset for doing data analysis and can make working on real world projects much easier.  Notice that we have all the column names automatically as they appear in the database without any further manipulation in python.  This makes the pandas dataframe, truly a batteries included library.  
# 
# ## SQL Introduction
# 
# Since reading data from a database is so important for working as a data scientist, we'll do a brief review of SQL now and then look at the pandas equivalences along side our SQL queries.
# 
# The most basic SQL query is:
# 
# `SELECT * FROM [SCHEMA NAME].[TABLE NAME];`
# 
# Notice that this statement, like all SQL statements ends with a `;` which is necessary unlike in python.  We've already seen an example, but let's look at it again:

# In[15]:


engine = connection.cursor()
sql_data = engine.execute("SELECT * FROM industry;").fetchall()


# Notice that we need to call the `fetchall` method in order to actually execute the query.  Whenever we are getting data from a database connection object, we need to do a fetch of some kind.  There are multiple fetch methods available:

# In[16]:


[
    method 
    for method in dir(engine.execute("SELECT * FROM industry;")) 
    if "fetch" in method and "_" not in method
]


# We will make use of `fetchall` most often, however for large tables that can't be read in all at once `fetchmany` and `fetchone` are useful primitives.
# 
# Now let's look at the pandas equivalence:

# In[18]:


#id	manufacturing	technology	real_estate
df[["id", "manufacturing", "technology", "real_estate"]]


# As you can see, we have to be explicit about which columns we want in this version of the select statement.  However we can choose specific columns to select in both SQL and in pandas:

# In[19]:


sql_data = engine.execute("SELECT manufacturing FROM industry;").fetchall()


# In[20]:


df["manufacturing"]


# In general SQL statements function sort of like list comprehensions.  And most of them are built around the basic `SELECT` statement we just looked at.  Now let's explore some modifiers to this `SELECT` statement.  First let's look at how to recover information about the data from our query.
# 
# These sorts of statements will take specific columns, apply functions to those columns, and then return the resultant transformation.  Here are some examples:

# In[21]:


engine.execute("SELECT COUNT(manufacturing) FROM industry;").fetchall()


# Here we want to know how many rows the manufacturing column has from the `industry`.  In general database tables all have the same number of rows, however we'll see how other modifers break this rule.  In addition to being able to call `COUNT` on a single column, we can also call it across all columns:

# In[22]:


engine.execute("SELECT COUNT(*) FROM industry;").fetchall()


# Here are the pandas equivalences:

# In[23]:


len(df["manufacturing"]), df["manufacturing"].shape[0]


# The above are two different wants to return the number of rows for a specific column.  We can also do this across all rows:

# In[24]:


len(df), df.shape[0]


# Next let's look at how to get the maximum or minimum of a column in SQL:

# In[25]:


engine.execute(
    "SELECT MAX(manufacturing), MIN(manufacturing) FROM industry;"
).fetchall()


# As you can see, we can return multiple transformations on a single column in one `SELECT` statement.  This makes SQL very flexible, however this can also make things complicated quickly.  We'll see how to resolve that in a moment.  But first let's look at the pandas equivalence:

# In[26]:


df["manufacturing"].max(), df["manufacturing"].min()


# One difference between SQL and pandas is with pandas we can operate over the entire dataframe at once:

# In[27]:


df.max()


# In[28]:


df.min()


# The equivalent is not as easily accomplished in SQL.  Next let's see how to query for rows that meet specific conditions.  For this we will need a `WHERE` clause as follows:
# 
# 
# `SELECT * FROM [SCHEMA NAME].[TABLE NAME] WHERE [TABLE COLUMN MEETS CONDITION];`
# 
# Let's look at some specific examples:

# In[29]:


sql_data = engine.execute("SELECT * FROM industry WHERE manufacturing>0.3;").fetchall()


# The pandas equivalence is:

# In[30]:


df[
    df["manufacturing"] > 0.3
]


# We can modify both of these statements to ensure that the number of rows is the same for both:

# In[31]:


engine.execute("SELECT COUNT(*) FROM industry WHERE manufacturing>0.3;").fetchall()


# In[32]:


df[df["manufacturing"] > 0.3].shape[0]


# As you can see the same number of elements is returned in both cases.  Next let's look at an equality condition:

# In[33]:


engine.execute("SELECT * FROM industry WHERE id=10;").fetchall()


# And the pandas equivalence:

# In[34]:


df[df["id"] == 10]


# Notice the use of double equals in pandas and single equals in SQL as a difference between the two statements.  Sometimes our SQL statements can get very verbose, for this reason sometimes its useful to name our selections, especially if they are being modified.  In order to do this we use the `AS` keyword as follows:
# 
# ```
# SELECT
# [SELECTED COLUMN OR TRANSFORMATION] as transform
# FROM [SCHEMA NAME].[TABLE NAME];
# ```
# 
# Let's look at an example:

# In[35]:


engine.execute("""
SELECT 
    MIN(manufacturing) as min_manufacturing,
    MAX(technology) as max_technology,
    COUNT(real_estate) as size 
FROM 
    industry 
WHERE 
    real_estate >0.5;
""").fetchall()


# There isn't really a pandas equivalence to this naming convention, but it's necessary, when multiple `SELECT` statements are combined:

# In[36]:


engine.execute("""
SELECT 
    MIN(manufacturing)
FROM (
 SELECT * 
 FROM industry 
 WHERE real_estate>0.5
) as expensive_real_estate;
""").fetchall()


# The multiple select statement query does have an equivalence in pandas:

# In[37]:


expensive_real_estate = df[df["real_estate"] > 0.5]
expensive_real_estate["manufacturing"].min()


# One final point to make, and an important difference between SQL statements and querying a pandas dataframe:
# 
# ### Order is not guaranteed in a SQL `SELECT` statement.
# 
# This point may seem trivial but it will come up at some point on a project so I mention it here.  You can always impose an ordering with an `ORDER BY` statement which will see in a moment.  But if you fail to impose an ordering, it is not guaranteed that your rows will be returned in the same order.  Let's see an example now:

# In[38]:


sql_data_one = engine.execute("""
 SELECT * 
 FROM industry 
 ORDER BY manufacturing;
""").fetchall()

sql_data_two = engine.execute("""
 SELECT * 
 FROM industry;
""").fetchall()

sql_data_one == sql_data_two


# While we cannot guarantee ordering in SQL, we can in pandas.  That said, we can choose to change how the data is order with a call to `sort_values`:

# In[39]:


df = df.sort_values("manufacturing")
df


# Notice if we do not mutate the dataframe by reassigning it, the new ordering will not be maintained.  This is why we have an equals statement followed by the `sort_values` method.
# 
# Because this is a course on python and not SQL this ends our demonstration of SQL statements and there pandas equivalences.  The point is hopefully clear - pandas can do most if not all of the same things as a SQL query.
# 
# ## Pandas Querying Techniques
# 
# Next we'll look at some more querying techniques, however just in pandas.  First let's see how to create a compound `SELECT` statement.  For each component statement we simply enclose them in parantheses and then join them with a boolean operator.  Here are the boolean operators we will consider:
# 
# * `&` - The `AND` operator - It's truth table is
# 
# | First  | Second  | First AND Second  |
# |---     |---      |---                |
# | True   | True    | True              |
# | True   | False   | False             |
# | False  | True    | False             |
# | False  | False   | False             |
# 
# As you can see, only when both inputs of the operator are `True` does the `AND` operator return `True`.
# 
# * `|` - the `OR` operator - It's truth table is
# 
# | First  | Second  | First OR Second  |
# |---     |---      |---                |
# | True   | True    | True              |
# | True   | False   | True              |
# | False  | True    | True              |
# | False  | False   | False             |
# 
# As you can see, when either input is `True` the `OR` operator returns `True`.
# 
# * `~` - the `NOT` operator - It's truth table is
# 
# | First  | NOT First |  
# |---     |---        |
# | True   | False     | 
# | True   | False     | 
# | False  | True      | 
# | False  | True      | 
# 
# As you can see, the `NOT` operator simply reverses the truth of the input.
# 
# You may recall from the numpy lecture, the way slicing works.  This is equivalent in pandas:

# In[40]:


import numpy as np
import pandas as pd

matrix = np.random.rand(500, 5) * 100
df = pd.DataFrame(matrix, columns=["A", "B", "C", "D", "E"])

df[
    (df["A"] > 50) &
    (df["B"] < 25)
].shape


# Now let's look at an `OR` example:

# In[41]:


df[
    (df["A"] > 50) |
    (df["B"] < 25)
].shape


# Notice, significantly more data is returned because _either_ of the component statements need to be `True` not both.
# 
# ## Pandas Merging
# 
# In this section we will go over merging two or more dataframes together in pandas.  For this we will look at the following methods:
# 
# * append
# * concat
# * merge
# 
# While we will introduce the topic here, we will not provide an _exhaustive_ enumeration of the functionality of these methods.  Please consider checking out the  [pandas docs](https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html) for more information.
# 
# ### Append
# 
# The most common technique for combining dataframes in the append.  It works similarly to the builtin list's append function.  Let's look at some examples:

# In[42]:


import pandas as pd
import random 

df = pd.DataFrame()

for _ in range(100):
    df = df.append({
        "A": round(random.random() * 100, 2),
        "B": round(random.random() * 1000, 3)
    }, ignore_index=True)
    
df.shape


# As you can see, we can append dictionaries to a dataframe, so long as we use consistent keys.  Those keys get mapped to the columns of the dataframe:

# In[43]:


df.head()


# Also notice the use of ignore_index - this is required when we append a dictionary to a pandas dataframe because dictionaries don't have an index and pandas expects this to know where to put the data.  If no index is present, the data just gets appended to the end of the dataframe.  However, if you append a pandas dataframe to a pandas dataframe and the indexes are the same, something different happens:

# In[44]:


import pandas as pd
import numpy as np

matrix_one = np.random.rand(3, 2) * 100
df_one = pd.DataFrame(matrix_one, columns=["A", "B"])
df_two = pd.DataFrame()

for index in range(3):
    df_two = df_two.append({
        "A": index,
        "B": index
    }, ignore_index=True)
    
df_two


# In[45]:


df_two = df_two.append(df_one)
df_two


# Notice, now the index repeats itself since the dataframes have the same index.  Let's see what happens if we try to select the first element:

# In[46]:


df_two.loc[0]


# This returns two elements, which is certainly unexpected behavior.  Many of pandas other methods rely on the index elements being unique.  Therefore this error will break a bunch of code and is a very common pandas bug.  Luckily this is very easy to resolve:

# In[47]:


df_two = df_two.reset_index()
df_two.loc[0]


# By reseting the index, we recover an ordering with a unique row index.  Be careful when using this that simply resetting the row index is what you want.
# 
# ### Concat
# 
# Next let's look at how to "concatenate" two dataframes together:
# 

# In[48]:


import pandas as pd
import numpy as np

matrix_one = np.random.rand(3, 2) * 100
df_one = pd.DataFrame(matrix_one, columns=["A", "B"])
df_two = pd.DataFrame()

for index in range(3):
    df_two = df_two.append({
        "A": index,
        "B": index
    }, ignore_index=True)
    
pd.concat([df_one, df_two])


# Notice this does the same thing as an append, except it allows us to provide a list of dataframes, rather than having to append them one at a time.  Note that concat expects the columns to be the same for both dataframes.  If you try to concatenate two dataframes with different columns, you will get unexpected behavior:

# In[49]:


import pandas as pd
import numpy as np

matrix_one = np.random.rand(3, 2) * 100
df_one = pd.DataFrame(matrix_one, columns=["A", "B"])
df_two = pd.DataFrame()

for index in range(3):
    df_two = df_two.append({
        "C": index,
        "D": index
    }, ignore_index=True)
    
pd.concat([df_one, df_two])


# Notice that `concat` doesn't know how to handle the missing data, so it just sticks `NaN`s in as a placeholder.
# 
# ### Merge
# 
# Next we'll look at merge which relies on a join.  The nice thing about this method is, it doesn't require all the columns in the two dataframes to be the same.  However they need to have at least one column in common which is used to "merge" the data.  

# In[50]:


import pandas as pd
import numpy as np

df_one = pd.DataFrame()

for index in range(3):
    df_one = df_one.append({
        "A": index,
        "E": index * 3
    }, ignore_index=True)

df_two = pd.DataFrame()

for index in range(3):
    df_two = df_two.append({
        "A": index,
        "D": index * 5
    }, ignore_index=True)
    
pd.merge(df_one, df_two, how="inner", on="A")


# You can make an explicit index column if there is no obvious choice:

# In[51]:


import pandas as pd
import numpy as np

matrix_one = np.random.rand(3, 2) * 100
matrix_two = np.random.rand(3, 2) * 100
df_one = pd.DataFrame(matrix_one, columns=["A", "B"])
df_two = pd.DataFrame(matrix_two, columns=["C", "D"])

df_one["index"] = df_one.index
df_two["index"] = df_two.index

pd.merge(df_one, df_two, how="inner", on="index")


# Notice we've been using something called `how` as one of the keywords in our merge.  Here `how` refers to the type of "join".  There are some variants of this technique, but we will only consider two here:
# 
# * inner - selects values from index in both the left AND right dataframe
# * outer - selects values from index in either the left OR right dataframe
# 
# As you can see, a join is just another way of doing an `AND` or `OR` except it's explicitly over a provided index column which appears in both dataframes.
# 
# ## Aggregations
# 
# Before we close out this chapter we will look at one more technique that can be very useful, an aggregation.  This is often used in conjunction with something called a `groupby`.  Let's see an example of a `groupby` first:

# In[52]:


import pandas as pd
import numpy as np

matrix = np.round(np.random.rand(500, 2) * 100, 2)

df = pd.DataFrame(matrix, columns=["average_income", "age"])
df["city"] = np.nan
df.loc[0:250, "city"] = "New York"
df.loc[250:, "city"] = "Boston"

df


# As you can see, one of these columns has strings for values instead of numbers.  By using a groupby we can select subsections of the above dataframe, conditional on which city we are referring to:

# In[53]:


for group, tmp in df.groupby("city"):
    print(group, tmp.shape)


# Here we print out the slice of the dataframe for Boston and then New York city and we observe their relative number of rows and columns.  Next let's get the average income for each slice:

# In[54]:


for group, tmp in df.groupby("city"):
    print(group, tmp["average_income"].mean())


# We can also accomplish the above with an aggregation:

# In[55]:


df.groupby("city").agg({"average_income":"mean"})


# Notice we no longer need the for loop in order to get the average income by city.  We can also specify a function explicitly:

# In[56]:


df.groupby("city").agg({"average_income": np.mean})


# I find this to be more useful than using the string equivalent, because it gives us far more control.  Additionally we can call an aggregation without the use of a groupby:

# In[57]:


df.agg({"average_income": "mean"})


# We can also supply a function, however this means we must transform across the entire axis:

# In[58]:


df.agg(np.mean, axis=0)


# In[ ]:





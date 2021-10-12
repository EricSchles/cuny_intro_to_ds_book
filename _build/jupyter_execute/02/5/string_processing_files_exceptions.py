#!/usr/bin/env python
# coding: utf-8

# # String Processing, Files and Exceptions
# 
# In this section we will discuss string processing, files and exceptions.  These topics may appear disperate, but really they are all about how to read and process files.
# 
# ## Reading And Writing Files
# 
# We can think of a file as just a giant string, stored on the disk as a file, rather than in memory.  Reading and writing files therefore is pretty straight forward.  Let's look at how to write a file in Python:

# In[1]:


f = open("new_file.txt", "w")
f.write("Hello there")
f.close()


# The above code will open a file called `new_file.txt`.  Since we pass the "w" flag, the file will be opened for writing, meaning it will _overwrite_ any content that is already there.  
# 
# The thing we get back, in this case `f` for file, is sometimes called a file handle.  The object f comes with the following functions:

# In[4]:


[elem for elem in dir(f) if "__" not in elem and not elem.startswith("_")]


# We will be interested in any method with read or write.  As you saw above we used, the `write` method to write the string to the file.  Next let's see how to read from a file:

# In[5]:


with open("new_file.txt", "r") as f:
    print(f.read())


# Here we read the file contents that we wrote to the file in the step above.  So we can think of files as a way to _store_ information beyond the running time of a program.  This notion will be very helpful for things like log files, generating text, or any number of varied applications.
# 
# Notice that we use the `with` statement like we did in a previous section.  The `with` statement is used with any object that has aboth an `__enter__` method and a `__exit__` method.  We can verify our `f` object has both with `dir`:

# In[7]:


if '__exit__' in dir(f) and '__enter__' in dir(f):
    print("yay, we understand")
else:
    print("oh no!  Python's API has changed")


# The `__enter__` method tells Python what to do when the object is created - in this case the `__enter__` method looks for the file in the current working directory, if Python finds it, then it opens the file.  If the file is opened for reading this allows the program to read the contents of the file.  If the file is opened for writing, the contents in the file are cleared, and any text written to the file will take it's place.  
# 
# The `__exit__` method tells us what to do when we leave the scope of the `with` statement, specified by the indent after the `with` statement.  Here the `__exit__` method closes the file.  Therefore once we return to code that is not indented within the `with` statement, we can no longer read from or write to the file.  
# 
# Next let's look at readlines:

# In[10]:


with open("new_file.txt", "w") as f:
    f.write("Hello there.\n")
    f.write("My name is Eric.\n")
    f.write("And I love Data Science.\n")
    
with open("new_file.txt", "r") as f:
    text = f.readlines()
    
text


# The readlines function will read each line in the file as the next element in a list.  This is parsed for us automatically, but unfortunately keeps the newline character, we specified to tell the text to appear on separate lines.  We can get rid of the newline character `\n` with the string method replace:

# In[11]:


text = [elem.replace("\n", "") for elem in text]

text


# All better!  The replace method is pretty amazing: It will replace any substring in a string with another string.  This means we can use it to delete or modify a string with ease.  Let's see what happens if there are multiple characters that match the initial substring we provide, will `replace` replace all of the instances?

# In[12]:


"aaaaaabbbb".replace("a", "")


# Very clearly, yes.  This is both powerful, and potentially dangerous.  What do you do if you want to all replace a single instance of a substring within a string?  Let's look at an example for how to do this:

# In[15]:


string = """
The brown dog runs fast through the fields.  And the orange cat wants to find the ball.
"""

substrings = string.split("wants")
substrings[1] = substrings[1].replace("the", "a")
"wants".join(substrings).replace("\n", "")


# This method shows how we can split on a specific word or phrase that separates the string into two substrings.  Then we act on the substring of instance, updating what's required.  
# 
# In addition to being able to replace to mutate strings, we can upper case, captialize or lower case strings with ease:

# In[19]:


string = "Hello there"
string = string.upper()
print(string)
string = string.lower()
print(string)
string = string.capitalize()
print(string)
string = " ".join([elem.capitalize() for elem in string.split()])
print(string)


# In the fourth instance, we captialize each word in the string.  Finally, we can check if a character is a letter, a number or either a letter or number:

# In[23]:


print("9".isnumeric())
print("9".isalpha())


# In[24]:


print("a".isnumeric())
print("a".isalpha())


# In[26]:


print("a".isalnum())
print("9".isalnum())


# In[31]:


print("/".isalnum())
print("#".isalnum())
print(".".isalnum())
print("?".isalnum())
print("<".isalnum())


# As you can see, anything that's considered a 'special' character is not considered a number or letter, even if that character is related to letters or numbers, like `<` is related to numbers and `.` is related to letters.
# 
# Now that we can read, write and process files - let's talk about exceptions.  An exception can occur in many ways and cases, but generally happens when you write code that follows Python syntax, but is wrong for some other reason.  One example is not initializing a variable and trying to write to it:

# In[39]:


b += 5


# In this case we get a `NameError` exception.  In some cases, Python doesn't know well enough what's correct and what's not.  In those cases, we can catch exceptions with a `try` and `except` block:

# In[40]:


try:
    b += 5
except:
    print("exception reached")


# Next let's look what happens when we try to call a function that doesn't exist:

# In[41]:


thing()


# Again we see this is a name error.  Which we can also catch with `try except`:

# In[43]:


try:
    thing()
except:
    print("no function exists named thing")


# We can also also try to read from a file that doesn't exist:

# In[44]:


open("hello.txt", "r")


# This raises a different error, in this case `FileNotFoundError`, which means the file doesn't exist.  For this we can do a `try except` as well:

# In[45]:


try:
    f = open("hello.txt", "r")
except:
    f = open("hello.txt", "w")
    f.write("")
    f.close()


# In this case, if the file doesn't exist, we create it, so that we don't run into that error next time.  Of course, this error will depend on the requirements of the program.
# 
# In some cases, we only want to catch certain kinds of errors, but let other errors pass through and stop a program.  For this, we can specific what kind of exception to catch.  For instance:

# In[46]:


try:
    x += 7
    f = open("log.txt", "r")
except FileNotFoundError:
    f = open("log.txt", "w")
    f.write("log file generated")
    f.close()


# In this case, the code fails because the variable `x` did not exist.  However, if only the `log.txt` file didn't exist, then the code would still run:

# In[47]:


x = 0
try:
    x += 7
    f = open("log.txt", "r")
except FileNotFoundError:
    f = open("log.txt", "w")
    f.write("log file generated")
    f.close()


# This is because we specifically catch the `FileNotFoundError`, rather than _any_ error.  In addition to being able to make use of Python's built-in exceptions, you can also make custom exceptions.  Typically this is done in functions like so:

# In[48]:


def thing(x):
    if isinstance(x, str):
        raise Exception("This function does not accept strings")
    return x + 7

thing("hello")


# However if we pass the correct parameter type:

# In[49]:


thing(6)


# It works as expected!

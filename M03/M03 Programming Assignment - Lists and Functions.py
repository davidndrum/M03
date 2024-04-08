#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 7.4 Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".


# In[8]:


things = ["mozzarella", "cinderella", "salmonella"]
print(things)


# In[ ]:


# 7.5 Capitalize the element in things that refers to a person and then print the list.  Did it change the element in the list?
# Answer - The element in the list is a string which is immutable.  It did not change the list item when it was capitalized.
# Answer - continued - The element can be replaced with a capitalized value (second sample below), but that required replacement,
# Answer - continued - not just case manipulation.


# In[9]:


things[1].capitalize()
print(things)

things[1] = things[1].capitalize()
print(things)


# In[5]:


# 7.6 Make the cheesy element of things all uppercase and then print the list.
# Using the upper method does not change the immutable string.  Changing the list item (mutable) by passing in the value
# returned when the upper method is applied to the string does work.


# In[10]:


things[0].upper()
print(things)

things[0] = things[0].upper()
print(things)


# In[ ]:


# 7.7 Delete the disease element from things, collect your Nobel Prize, and print the list.


# In[11]:


del(things[2])
print(things)


# In[ ]:


# 9.1 Define a function called good() that returns the following list: ['Harry', 'Ron', 'Hermione'].


# In[12]:


def good():
    return ["Harry","Ron","Hermione"]
print(good())


# In[ ]:


# 9.2 Define a generator function called get_odds() that returns the odd numbers from range(10). Use
# a for loop to find and print the third value returned.


# In[13]:


def get_odds(first=0, last=10, step=1): #Defined the required function
    number = first
    while number <= last:
        yield number
        number += step

got_odds = [] # Defined a list to store values returned from the generator
for x in get_odds(0,10): # Created a for loop to iterate over the generator
    if x % 2 != 0: # Evaluate the returned value from the generator for odd or even
        got_odds.append(x) # Added the odd values to the list
print(got_odds[2]) # Print the third position from the list.  The list starts counting positions at zero, so two is the third position.


# In[ ]:





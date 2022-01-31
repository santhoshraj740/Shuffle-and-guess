#!/usr/bin/env python
# coding: utf-8

# Shuffle and guess 

# In[1]:


from random import shuffle


# In[2]:


def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


# In[10]:


def player_guess():
    
    guess=''
    
    while guess not in ['1','2','0']:
        guess = input('Pick a number: 0, 1 or 2: ')
    return int(guess)


# In[14]:


def check_guess(my_list,guess):
    if mylist[guess] == 'O':
        print("congo")
    else:
        print("wrong guess")


# In[15]:


#final code finish
mylist=[' ','O',' ']
mixed_list = shuffle_list(mylist)
guess = player_guess()
check_guess(mixed_list,guess)


# In[16]:


mylist


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[10]:


import random 


# In[12]:


random.random()


# In[13]:


s=random.randint(1,100)
s


# In[14]:


def get_n_random_numbers(n=10,min_=-5,max_=5):
    numbers=[]
    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers
get_n_random_numbers()


# In[22]:


get_n_random_numbers(15,-4,8)
my_list=get_n_random_numbers(15,-4,8)
my_list


# In[17]:


# for a list [0,-4,8,-1,,-3,6,3,0,1]
histgram_1=[
    (-4,1)
    (0, 2)
    (8,1)
    (3,1)
    (-1,1)
    (6,1)
    (1,1)
]


# In[23]:


my_list


# In[24]:


sorted(my_list)


# In[41]:


def my_frequency_with_dict(list):  #hash yapısı
    frequency_dict={}  #dict()={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return  frequency_dict


# In[43]:


my_frequency_with_dict(my_list)


# In[48]:


def my_frequency_with_list_of_tuples(list_1):
    frequency_list=[]
    for i in range(len(list_1)):
        s=False
        for j in range(len(frequency_list)):
            if (list_1[i])==frequency_list[j][0]:
                frequency_list[j][1]=frequency_list[j][1]+1
                s=True
        if(s==False):
            frequency_list.append([list_1[i],1])
    return  frequency_list


# In[ ]:





# In[ ]:





# In[49]:


result_1= my_frequency_with_dict(my_list)
result_2=my_frequency_with_list_of_tuples(my_list)
result_1,result_2


# In[ ]:





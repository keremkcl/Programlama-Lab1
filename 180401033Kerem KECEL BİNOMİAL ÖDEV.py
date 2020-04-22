#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sympy as sym
from sympy import Symbol
from sympy import pprint


# In[4]:


p=Symbol('p')
x=Symbol('x')
n=Symbol('n')


# In[5]:


my_f_3_part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
my_f_3_part_0


# In[6]:


my_f_3_part_1=p**x
my_f_3_part_1


# In[7]:


my_f_3_part_2=(1-p)**(n-x)
my_f_3_part_2


# In[8]:


my_f_3=my_f_3_part_0*my_f_3_part_1*my_f_3_part_2
my_f_3


# In[15]:


sym.plot(my_f_3.subs({p:0.5,n:50}),(x, 0, 50), title='binomial distribution for n=50')


# In[14]:


x_values=[]
y_values=[]
for value in range (0,50):
    y=my_f_3.subs({p:0.5,n:50,x:value}).evalf()
    y_values.append(y)
    x_values.append(value)
    print(value,y)


# In[11]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# In[12]:


plt.plot(x_values,y_values)


# In[ ]:


plt.show()


# In[ ]:


Kerem Kecel 180401033


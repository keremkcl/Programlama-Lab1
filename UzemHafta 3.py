#!/usr/bin/env python
# coding: utf-8

# In[5]:


import sympy as sym
from sympy import Symbol
from sympy import pprint


# In[6]:


p=Symbol('p')
x=Symbol('x')
n=Symbol('n')


# In[7]:


my_f_3_part_0=sym.factorial(n)/(sym.factorial(x)*sym.factorial(n-x))
my_f_3_part_0


# In[8]:


pprint(my_f_3_part_0)


# In[9]:


my_f_3_part_1=p**x
my_f_3_part_1


# In[10]:


my_f_3_part_2=(1-p)**(n-x)
my_f_3_part_2


# In[11]:


my_f_3=my_f_3_part_0*my_f_3_part_1*my_f_3_part_2
my_f_3


# In[12]:


pprint(my_f_3)


# In[14]:


sym.plot(my_f_3.subs({p:0.5,n:50}),(x, 0, 50), title='binomial distribution for n=50')


# TÜREV

# In[15]:


from sympy import Symbol,Limit


# In[23]:


t=Symbol('t')
St=5*t**3+2*t+8


# In[17]:


t1=Symbol('t1')
delta_t=Symbol('delta_t')


# In[18]:


St1=St.subs({t:t1})
St1_delta=St.subs({t:t1+delta_t})


# In[24]:


Limit((St1_delta-St1)/delta_t,delta_t,0).doit()


# Olasılık Değer

# In[14]:


from sympy import Symbol,exp,sqrt,pi,Integral


# In[15]:


x=Symbol('x')


# In[16]:


p=exp(-(x-10)**2/2)/sqrt(2*pi)


# In[19]:


Integral(p, (x,11,12)).doit().evalf()


# In[ ]:





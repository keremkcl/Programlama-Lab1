#!/usr/bin/env python
# coding: utf-8

# In[9]:


from sympy import Symbol
x=Symbol('x')
y=Symbol('y')
x
y


# In[10]:


p=x*(x+x)
p


# In[9]:


p=(x+2)*(x+3)
p


# In[10]:


from sympy import factor,expand
expr= x**2 - y**2   
factor(expr)   ^#Çarpanlaraayırma 


# In[11]:


factors=factor(expr)
expand=expand(factors) #verilen çarpanların tamamını ele alır


# In[12]:


factors,expand


# In[16]:


expr1=x**3+3*x**2*y+3*x*y**2+y**3


# In[17]:


factors=factor(expr1)
factors


# In[18]:


from sympy import pprint
pprint(factors) #üstel olarak yazma


# In[19]:


x=Symbol('x')
series=x
n=5
for i in range(2,n+1):
    series=series+(x**i)/i   #üstel bi dizioluşturduk
pprint(series)


# In[22]:


expr=x*x+x*y+x*y+y*y
res=expr.subs({x:1,y:2})     #x ile y yer değiştiriyır(subs())
res


# In[23]:


r=expr.subs({x:1-y})  #x'i y ye bağlı bırak
r


# In[26]:


x=Symbol('x')
series=x
n=5
x_value=10
for i in range(2,n+1):
    series=series+(x**i)/i
pprint(series)
series_value=series.subs({x:x_value})
series_value


# In[ ]:


import sympy as sym


# In[ ]:


from sympy import Symbol


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'notebook')
import sympy.plotting as syp


# In[ ]:


sigma=Symbnol('sigma')


# In[ ]:


gauss_function=1/sympy.sqr(2*sympy.pi*sigma)


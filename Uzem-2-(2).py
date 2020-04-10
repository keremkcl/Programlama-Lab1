#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sympy as sym
from sympy import Symbol
from sympy import pprint

import sympy.plotting as syp
sigma=Symbol('sigma')
x=Symbol('x')
mu=Symbol('mu')


a=2*sym.pi*sigma
#print(a)
#pprint(a) 

b=sym.sqrt(2*sym.pi*sigma)
#pprint(b)

c=sym.sqrt(2*sym.pi*sigma*sigma)
#pprint(c)

part_1=1/(sym.sqrt(2*sym.pi*sigma**2))
part_2=sym.exp(-1*((x-mu)**2)/2*sigma**2)

my_gauss_function=part_1*part_2
#pprint(my_gauss_function)

#pprint(syp.plot(my_gauss_function.subs({mu:1,sigma:3}),(x,-10,10),title='gauss distribution'))#bir fonksiyon yazdık değişkenlere değerler atadık ve grafiği çizildi.

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
x_values=[]
y_values=[]
for value in range(-5,5):
    y=my_gauss_function.subs({mu:10,sigma:30,x:value}).doit() 
    y_values.append(y)
    x_values.append(value)
    print(value,y)
    
import matplotlib.pyplot as plt
plt.plot(x_values,y_values)


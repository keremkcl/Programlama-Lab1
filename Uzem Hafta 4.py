#!/usr/bin/env python
# coding: utf-8

# In[1]:


def min_heapify(array,i):
    left=2*i+1
    right=2*i+2
    length=len(array)-1
    smallest=i
    if left<= length and array [i]>array[left]:
        smallest=left
    if right<= length and array[smallest] > array[right]:
        smallest=right
    if smallest !=i:
        array[i],array[smallest] =array[smallest],array[i]
        min_heapify(array,smallest)


# In[2]:


def build_min_heap(array):
    for i in reversed (range(len(array)//2)):
        min_heapify(array,i)


# In[3]:


def heapsort(array):
    array=array.copy()
    build_min_heap(array)
    sorted_array=[]
    for i in range(len(array)):
        array[0],array[-1]=array[-1],array[0]
        sorted_array.append(array.pop())
        min_heapify(array,0)
    return sorted_array


# In[4]:


my_array_1=[8,10,3,4,7,14,15,1,2,16]
my_array_2=heapsort(my_array_1)
my_array_1,my_array_2


# In[5]:


def insertItemToHeap(myheap_1,item):
    if len(myheap_1) == 0:
        myheap_1[0]=item
    else:
        myheap_1.append(item)
    build_min_heap(myheap_1)
    return myheap_1


# In[6]:


myheap=insertItemToHeap(my_array_2,5)
myheap


# In[12]:


def removeItemFrom(myheap_1):
    l = len(myheap_1)
    if l == 0:
        print("heap boş")
        return myheap_1.pop()
    build_min_heap(myheap_1)
    return myheap_1


# In[13]:


removeItemFrom(myheap)
myheap


# In[ ]:





# In[ ]:





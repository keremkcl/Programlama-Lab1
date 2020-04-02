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


# In[89]:


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


# In[90]:


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


# In[53]:


my_list_1=get_n_random_numbers(5,-2,2)
my_hist_d=my_frequency_with_dict(my_list_1)
my_hist_d


# In[64]:


frequency_max=-1
mode=-1
for key in my_hist_d.keys():
    print(key,my_hist_d[key])
    if my_hist_d[key]>frequency_max:
        frequency_max=my_hist_d[key]
        mode=key
frequency_max,mode


# In[70]:


def my_mode_with_dict(my_hist_d):
    frequency_max=-1
    mode=-1
    for key in my_hist_d.keys():
        #print(key,my_hist_d[key])
        if my_hist_d[key]>frequency_max:
            frequency_max=my_hist_d[key]
            mode=key
    return mode,frequency_max


# In[76]:


my_mode_with_dict(my_hist_d)


# In[72]:


my_list_100=get_n_random_numbers(100,-40,40)
my_hist_1=my_frequency_with_dict(my_list_100)
my_mode_with_dict(my_hist_1)


# In[ ]:


my_list_1=get_random_numbers(10)
my_hist_list=my_frequency_with_list_of_tuples(my_list_1)
my_hist_list


# In[ ]:


frequency_max=-1
mode=-1
   for item,frequency in my_hist_list:
        print(item,frequency)
        if frequency>frequency_max:
            frequency_max=frequency
            mode=item
return mode,frequency_max         


# lineer search on list

# In[91]:


def my_linear_search(my_list,item_search):
    found=(-1,-1)
    n=len(my_list)
    for indis in range(n):
        if my_list[indis]==item_search:
            found=(my_list[indis],indis) #listede bulundu ,return bulunan sayı,tuple olarak return edili
    return found


# In[83]:


my_list


# In[92]:


my_linear_search(my_list,3)


# MEAN OF LİST
# 

# In[93]:


my_list


# In[101]:


def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item
    mean_=t/s
    return mean_


# In[103]:


my_list=get_n_random_numbers(10,-10,30)
print(my_list)
my_mean(my_list)


# sort the list

# In[115]:


my_list


# In[ ]:


n=len(my_list)
print(my_list)
for i in range(n-1,-1,-1):
    for j in range (0,i):
        if not(my_list[j]<my_list[j+1]):
            temp=my_list[j]
            my_list[j]=my_list[j+1]
            temp=my=list[j+1]
    return my_list


# In[126]:


#with function
def my_bubble_sort(my_list):
    n=len(my_list)
    #print(my_list)
    for i in range(n-1,-1,-1):
        for j in range (0,i):
            if not(my_list[j]<my_list[j+1]):
                temp=my_list[j]
                my_list[j]=my_list[j+1]
                my_list[j+1]=temp
    return my_list


# In[127]:


my_list=get_n_random_numbers(4,-5,5)
print(my_list)
my_bubble_sort(my_list)


# binary search on a sorted list 

# In[133]:


def my_binary_search(my_list,item_search):
    found=(-1,-1)
    low=0
    high=len(my_list)-1
    
    while low <= high:
        mid=(low+high)//2
        
        if my_list[mid]==item_search:
            return my_list[mid],mid
        elif my_list[mid]>item_search:
            high=mid-1
        else:
            low=mid+1
    return found #none
            


# In[134]:


my_list_1=get_n_random_numbers(10)
print("liste",my_list_1)
my_list_2=my_bubble_sort(my_list_1)
print("sıralı liste",my_list_2)
my_binary_search(my_list_2,3) #1


# median of a list

# In[136]:


size=input("dizi boyutunu giriniz")
size=int(size) #convert str to int
my_list_1=get_n_random_numbers(size)

print("liste",my_list_1)


# In[140]:


my_list_2=my_bubble_sort(my_list_1)


# In[ ]:


def my_median(my_list)
    my_list_2=bubbke_sort(my_list_1)
#print(my_list_2)  
    n=len(my_list_2)
    if n%2==1:
        middle=int(n/2)+1
        median=my_list_2[middle]
        print(median)
    else:
        middle_1=my_list_2[int(n/2)]
        middle_2=my_list_2[int(n/2)+1]
        median=(middle_1+middle_2)/2
    #print(median)
    return median


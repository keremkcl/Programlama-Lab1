
# coding: utf-8

# In[11]:


import csv
import sys

file=open("input_hw_2.csv","r+",encoding="utf-8")
read=file.read() 


a=read.split(";") 
print(a)
month = []
for i in range(3,len(a),3): 
    month.append(a[i].split("-"))


smonth= []
for i in range(len(month)): #çıkış aylarına gittim
    smonth.append(month[i][1])


def my_frequency_with_dict(list): #frekansı hesapladım
    frequency_dict={}
    for item in list:
        if(item in frequency_dict):
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict





fsmonth=my_frequency_with_dict(smonth) 




listmonth=fsmonth.values() 




def my_mean(my_list):
    s,t = 0,0
    for item in my_list:
        s += 1
        t += item
    return t/s





listmonth_mean=my_mean(listmonth)


def my_bubble_sort(my_list):
    n = len(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not(my_list[j] < my_list[j+1]):
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list






list_month_bubble=my_bubble_sort(listemonth) #median bulabilmek için listeyi sıraladım






def my_median(my_list):
       my_list_2 = my_bubble_sort(my_list)
        n = len(my_list_2)
        if(n%2 == 1):
            middle = int(n/2)+1
            median = my_list_2[middle-1]
        else:
            middle_1 = int(n/2)-1
            middle_2 = middle_1+1
            median = (my_list_2[middle_1]+my_list_2[middle_2])/2
        return median


median=my_median(list_month_bubble)






with open("180401033_hw_2_output.txt","w",encoding="utf-8") as dosya:
dosya.write("MEDYAN:"+ str(median) + "\n")
dosya.write("ORTALAMA:"+ str(listemonth_mean))


# In[ ]:





# In[ ]:





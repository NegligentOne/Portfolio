#!/usr/bin/env python
# coding: utf-8

# In[ ]:



def getDataFromUser():
    D = {}
    while True:
        studentId = input("Enter Student ID: ")
        marksList = input("Enter the marks seperated by commas: ")
        moreStudents = input('Enter "no" to quit insertion: ')
        if studentId in D:
            print(studentId, " already listed")
        else:
            D[studentId] = marksList.split(",")
        if moreStudents.lower() == "no":
            return D

studentData = getDataFromUser()


# In[1]:


studentData


# In[21]:


def getAvgMarks(D):
    avgMarks = {}
    for x in D:
        L = D[x]
        s = 0
        for marks in L:
            s+= int(marks)
        avgMarks[x] = s/len(L)
    return avgMarks
        


# In[ ]:


avgM = getAvgMarks(studentData)


# In[ ]:


print(avgM)


# In[ ]:


for x in avgM:
    print("Student:",x,"got an average of",avgM[x])


# In[2]:


import numpy as np


# In[3]:


get_ipython().run_line_magic('pinfo', 'np.arange')


# In[ ]:


np.arange(0,10)


# In[4]:


A = np.arange(1,100)


# In[5]:


get_ipython().run_line_magic('pinfo', 'np.shape')


# In[6]:


A = np.round(10*np.random.rand(5,4))


# In[7]:


print(A)


# In[ ]:


print(A[2,3])


# In[ ]:


print(A[1,1])


# In[ ]:


print(A[1:])


# In[ ]:


print(A[4,:])


# In[ ]:


A[2,:]


# In[ ]:


A[:,1]


# In[ ]:


grads_dict = {'A':4,'B':3.5,'C':3,'D':2.5}


# In[ ]:


grads_dict


# In[ ]:


import pandas as pd


# In[ ]:


grads = pd.Series(grads_dict)


# In[ ]:


grads


# In[ ]:


grads.values


# In[ ]:


grads.index


# In[ ]:


marks_dict = {'A':85,'B':75,'C':65,'D':55}


# In[ ]:


makrs = pd.Series(marks_dict)


# In[ ]:


marks = pd.Series(marks_dict)


# In[ ]:


marks


# In[ ]:


marks['A']


# In[ ]:


marks[0:2]


# In[ ]:


df = pd.DataFrame({'Marks':marks,'Grades':grads})


# In[ ]:


df


# In[ ]:


df.T


# In[ ]:


df


# In[ ]:


df.values[2,0]


# In[ ]:


df.columns


# In[ ]:


df['Scaled Marks']=100*df['Marks']/90


# In[ ]:


df


# In[ ]:


del df['Scaled Marks']


# In[ ]:


df


# In[ ]:


G=df[df['Marks']>70]


# In[ ]:


G


# In[ ]:


A=pd.DataFrame([{'a':1,'b':4},{'b':-3,'c':9}])


# In[ ]:


A


# In[ ]:


A=pd.Series(['a','b','c'],index=[1,3,5])


# In[ ]:


A


# In[ ]:


A[1:3]


# In[ ]:


A.iloc[0:2]


# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


marks


# In[ ]:


grads


# In[ ]:


df = pd.DataFrame({'Marks':marks,'Grades':grads})


# In[3]:


df


# In[22]:


countMarks = df['Marks'].count()


# In[4]:


totalMarks


# In[1]:


conditions =[
            df['Marks'] >= (4.0),
            df['Marks'] < (2.0),
            (df['Marks'] >= (3.0)) & (df['Marks'] < (4.0))
            ]


# In[28]:


conditions


# In[29]:


tiers = ['Valedictorian','HonorRoll','Mediocore']


# In[30]:


df['Rating'] = np.select(conditions,tiers)


# In[31]:


df


# In[33]:


df['Volume_Percent']=np.round(100*df['Marks']/totalMarks,1)


# In[34]:


df


# In[35]:


df


# In[42]:


df = pd.read_csv(r'C:\Users\Negligent\Desktop\owid-covid-data.csv',)


# In[ ]:


df.head()


# In[52]:


df['date']=pd.to_datetime(df['date'])


# In[53]:


df.head()


# In[54]:


df.describe()


# In[58]:


df2 = df.groupby(['location'])[['location','total_cases','total_deaths',]].sum().reset_index()


# In[59]:


df2


# In[ ]:





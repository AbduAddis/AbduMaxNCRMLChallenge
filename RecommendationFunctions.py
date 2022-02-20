#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


dataset = pd.read_csv("superstore.csv")


# In[2]:


dataset


# In[3]:


predictions = pd.read_csv("xhol1.csv")


# In[5]:


predictions


# In[4]:


def calcPercentDownfall(data):
    totPercents = {}
    for index, row in data.iterrows():
        totals[row['Sub.Category']] = ((row['Revenue']-row['PostRevenue'])/row['Revenue'])*100
    return totPercents


# In[6]:


def getSubCat(category):
    if category == "Office Supplies":
        return ["Supplies","Envelopes","Paper","Binders","Labels"]
    elif category == "Technology":
        return ["Phones", "Appliances","Copiers","Machines","Accessories"]
    else:
        return ["Art","Bookcases","Chairs","Fasteners","Storage","Furnishings","Tables"]


# In[7]:


def getLowestSub(category,df):
    subCats = getSubCat(category)
    lowest = 100
    current = 0
    itemindex = 0
    for i in range(0,len(subCats)):
        current = float(df.loc[df["Sub.Category"]==subCats[i],"Ratio"])
       
        if current < lowest:
            
            lowest = current
            itemindex = i
    
    return [subCats[i],lowest]
    
     


# In[8]:


def returnThreeRand(category,df):
    subCatClass = df[df['Sub-Category']==category]
    return subCatClass.sample(n=3)


# In[58]:


threes = returnThreeRand("Accessories",dataset)


# In[59]:


print(threes)


# In[9]:


def findRecs(items,df):
    catCount = {"Furniture":0,"Technology":0,"Office Supplies":0}
    for item in items:
        place = df.loc[df["Product ID"]==item,"Category"]
        catCount[place.iloc[0]]+=1
    max_key = max(catCount, key=catCount.get)
    subCat = getLowestSub(max_key,predictions)
    recs = returnThreeRand(getLowestSub(max_key,predictions)[0],df)
    return recs


# In[13]:


findRecs(["TEC-CO-10002316","TEC-KON-10002194","OFF-AR-10004884","FUR-NOV-10004962"],dataset)


# In[14]:


findRecs(["FUR-SAF-10004530","TEC-STA-10004927","OFF-TEN-10001585","OFF-FA-10003472","OFF-LA-10000413","FUR-OFF-10003703"], dataset)


# In[93]:


findRecs(["OFF-PA-10003838","FUR-CH-10001616","FUR-FU-10003046"],dataset)


# In[ ]:





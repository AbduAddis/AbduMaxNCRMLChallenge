#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


dataset = pd.read_csv("superstore.csv")
hol2011 = pd.read_csv("hol2011.csv")
hol2012 = pd.read_csv("hol2012.csv")
hol2013 = pd.read_csv("hol2013.csv")
post2011 = pd.read_csv("post2011.csv")
post2012 = pd.read_csv("post2012.csv")
post2013 = pd.read_csv("post2013.csv")

print(dataset)


# In[11]:


hol2011
newHol2011 = hol2011[['Sub.Category','Revenue']].copy()


# In[13]:


hol2012
newHol2012 = hol2012[['Sub.Category','Revenue']].copy()


# In[14]:


hol2013
newHol2013 = hol2013[['Sub.Category','Revenue']].copy()


# In[15]:



newPost2011 = post2011[['Sub.Category','Revenue']].copy()


# In[16]:



newPost2012 = post2012[['Sub.Category','Revenue']].copy()


# In[17]:



newPost2013 = post2013[['Sub.Category','Revenue']].copy()


# In[18]:


newPost2013


# In[22]:




def newTotals(df):
   totals = {}
   for index, row in df.iterrows():
       if row['Sub.Category'] not in totals.keys(): 
           totals[row['Sub.Category']] = 0
           totals[row['Sub.Category']] += row['Revenue']
       else:
           totals[row['Sub.Category']] += row['Revenue']
   return totals


# In[5]:


from collections import Counter

counter = Counter(dataset["Country"])


# In[23]:


totHol2011 = newTotals(newHol2011)


# In[24]:


totHol2012 = newTotals(newHol2012)
totHol2013 = newTotals(newHol2013)


# In[25]:


totHol2011 = newTotals(newHol2011)
totHol2012 = newTotals(newHol2012)
totHol2013 = newTotals(newHol2013)
totPost2011 = newTotals(newPost2011)
totPost2012 = newTotals(newPost2012)
totPost2013 = newTotals(newPost2013)


# In[29]:


dfHol2011 = pd.DataFrame(list(totHol2011.items()),
                   columns=['Sub-Category', 'Revenue'])
dfHol2012 = pd.DataFrame(list(totHol2012.items()),
                   columns=['Sub-Category', 'Revenue'])
dfHol2013 = pd.DataFrame(list(totHol2013.items()),
                   columns=['Sub-Category', 'Revenue'])
dfPost2011 = pd.DataFrame(list(totPost2011.items()),
                   columns=['Sub-Category', 'Revenue'])
dfPost2012 = pd.DataFrame(list(totPost2012.items()),
                   columns=['Sub-Category', 'Revenue'])
dfPost2013 = pd.DataFrame(list(totPost2013.items()),
                   columns=['Sub-Category', 'Revenue'])


# In[35]:


dfHol2011.to_csv('newHol2011.csv',index = False)
dfHol2012.to_csv('newHol2012.csv',index = False)
dfHol2013.to_csv('newHol2013.csv',index = False)
dfPost2011.to_csv('newPost2011.csv',index = False)
dfPost2012.to_csv('newPost2012.csv',index = False)
dfPost2013.to_csv('newPost2013.csv',index = False)


# In[ ]:





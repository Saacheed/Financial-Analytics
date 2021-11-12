#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[5]:


rev_m = 170
rev_stdev = 20
iterations = 1000


# In[7]:


rev = np.random.normal(rev_m, rev_stdev, iterations)
rev


# In[9]:


plt.figure(figsize=(15, 6))
plt.plot(rev)
plt.show()


# In[11]:


COGS = - (rev * np.random.normal(0.6,0.1))
 
plt.figure(figsize=(15, 6))
plt.plot(COGS)
plt.show()


# In[13]:


COGS.mean()


# In[15]:


COGS.std()


# In[17]:


Gross_Profit = rev + COGS
Gross_Profit


plt.figure(figsize=(15, 6))
plt.plot(Gross_Profit)
plt.show()


# In[19]:


max(Gross_Profit)


# In[21]:


min(Gross_Profit)


# In[23]:


Gross_Profit.mean()


# In[25]:


Gross_Profit.std()


# In[27]:


plt.figure(figsize=(10, 6));
plt.hist(Gross_Profit, bins = [40, 50, 60, 70, 80, 90, 100, 110, 120]);
plt.show()


# In[28]:


plt.figure(figsize=(10, 6));
plt.hist(Gross_Profit, bins = 20);
plt.show()


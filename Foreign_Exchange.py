#!/usr/bin/env python
# coding: utf-8

# In[4]:


from bs4 import BeautifulSoup
import pandas as pd
import requests


# In[6]:


from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.nrb.org.np/forex/','html.parser')
soup = requests.get(url)
soup = BeautifulSoup(soup.text, "lxml")
soup


# In[25]:


element = soup.find('div', class_='card-layout')
print(element)


# In[26]:


elements = soup.find_all('div', class_='card-layout')
for element in elements:
    print(element)


# In[28]:


tags = table_codes.find_all('tr')
tags


# In[ ]:





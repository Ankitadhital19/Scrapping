#!/usr/bin/env python
# coding: utf-8

# In[1]:


https://www.worldometers.info/coronavirus/


# In[1]:


from bs4 import BeautifulSoup
import requests
url = BeautifulSoup('https://www.worldometers.info/coronavirus/','html.parser')
soup = requests.get(url)
soup = BeautifulSoup(soup.text, "lxml")
soup


# In[2]:


table_codes = soup.table
table_codes 


# In[3]:


tags = table_codes.find_all('tr')
tags


# In[5]:


list_data = []
for i in tags:
    list_data.append(i.text.split('\n')[1:])


# In[6]:


list_data


# In[7]:


cleaned_data = []
for j in list_data:
    if j[0] != "":
        cleaned_data.append(j)
cleaned_data
       


# In[8]:


import csv
file = open('covid_data.csv','w')
x = csv.writer(file)
x.writerows(cleaned_data)
file.close()


# In[14]:





# In[9]:


import pandas as pd
df = pd.read_csv('covid_data.csv',encoding = 'latin1')
df


# In[10]:


df1 = df[['Country,Other','TotalCases','TotalDeaths']].iloc[0:10]
df1['TotalCases'] = [int(i.replace(',',''))for i in df1['TotalCases']]
df1['TotalDeaths'] = [int(i.replace(',',''))for i in df1['TotalDeaths']]
print(df1)


# In[16]:


import plotly.express as px
fig = px.bar(df1, x= 'Country,Other', y = 'TotalCases')
fig.show()


# In[11]:


import plotly.graph_objects as go
fig = go.Figure(data=[
    go.Bar(name='TotalCases', x=df1['Country,Other'], y=df1['TotalCases']),
    go.Bar(name='TotalDeaths', x=df1['Country,Other'], y=df1['TotalDeaths'])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()


# In[18]:


import plotly.express as px
fig = px.pie(df1, values='TotalCases', names='Country,Other', title='Covid Cases of different countries')
fig.show()


# In[1]:


pwd


# In[ ]:





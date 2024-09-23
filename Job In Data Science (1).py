#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('jobs_in_data.csv')


# In[3]:


df.shape


# In[4]:


df.head()


# In[5]:


df.info()


# In[6]:


df.columns


# In[7]:


#check for null values
df.isnull().sum()


# In[9]:


df.describe()


# In[10]:


df.sort_values(by = "salary", ascending = True ).head(10)


# In[11]:


df.corr()


# In[12]:


df[df['job_category'].str.contains('Data Analysis')].head(10)


# In[13]:


df2= df.groupby('work_year')[[ 'job_title', 'job_category', 'salary_currency', 'salary',
       'salary_in_usd', 'employee_residence', 'experience_level']].mean().sort_values(by = 'salary',ascending = False)


# In[14]:


df2


# # EDA
# 

# In[15]:


df2.plot()


# In[16]:


df.head()


# In[21]:


# plotting a bar chart for job_category and it's count

ax = sns.countplot(x = 'job_category',data = df)
sns.set(rc={'figure.figsize':(30,7)})

for bars in ax.containers:
    ax.bar_label(bars)


# In[63]:


# plotting a bar chart for job_category vs salary

job = df.groupby(['job_category'], as_index=False)['salary'].sum().sort_values(by='salary', ascending=False)

sns.boxplot(x = 'job_category',y= 'salary' ,data = df)            
         


# In[64]:


# plotting a box chart for experience_level vs salary

level = df.groupby(['experience_level'], as_index=False)['salary'].sum().sort_values(by='salary', ascending=False)

sns.barplot(x = 'experience_level',y= 'salary' ,data = df)


# In[24]:


sns.heatmap(df.corr(), annot=True, cmap='PuBuGn', square=True)
plt.show()


# the correlation between variables by heatmap

# In[66]:


fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('job_title')['work_year'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# Top 10 most demanding job 

# In[37]:


sns.set(rc={'figure.figsize':(30,10)})
ax = sns.countplot(data = df, x = 'job_category')

for bars in ax.containers:
    ax.bar_label(bars)


# From above graph we can see that most of the jobs are in Data Science & Research category

# Outcomes
# - Cleaned and analyzed dataset ready for further analysis or modeling.
# - Visualizations that show insights into the salary distributions, top job categories, and correlations between variables.
# - A clear understanding of the most in-demand job roles in data science based on factors like salary and experience level.

# In[ ]:





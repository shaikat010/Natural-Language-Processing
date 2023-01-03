#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[5]:


import re
chat1='codebasics: Hello, I am having an issue with my order # 412889912'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat1)
print(matches)
# finds all the matches 


# In[7]:


chat2='codebasics: I have a problem with my order number 412889912'
pattern = 'order[^\d]*(\d*)'
matches = re.findall(pattern, chat2)
print(matches)


# In[ ]:





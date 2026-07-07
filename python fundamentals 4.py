#!/usr/bin/env python
# coding: utf-8

# In[ ]:


Introduction to list datatype:


# In[ ]:


Definition :A List is a collection of items declared in a paticular order.

    classification: It is classified as a mutable datatype

how to define the list-----------------> [  ]


# In[ ]:





# In[2]:


students = ['jyothi','mythili','mounika','shruthi','manisha']   # 0,1,2,3,4


# In[3]:


print(students)


# In[ ]:





# In[4]:


type(students)


# In[ ]:


introduction to indexing: 0,1,2,3,4...........n


# In[ ]:





# In[ ]:


1. how to access the elements from the list.

2.how to modify the elements from the list.

3.how to delete the elements from the list.


# In[ ]:


# i want  to access the jyothi name from the above list   ..?


# In[ ]:





# In[5]:


print(students[0])


# In[7]:


print(students[0].title())


# In[8]:


print(students[3])


# In[ ]:


#req : i want to appreciate jyothi


# In[ ]:





# In[12]:


print(f"keep it up,{students[0].title()}")


# In[13]:


print(students)


# In[ ]:





# In[ ]:


# i want to add mahi name to the list


# In[14]:


students.append("mahi")

print(students)
# In[15]:


print(students)


# In[ ]:


# i want varun in the second index


# In[ ]:





# In[16]:


students.insert(2,"varun")


# In[17]:


print(students)


# In[ ]:





# In[ ]:


note : what is defference between the append and insert method in a datatype....**


# In[ ]:


#how to modify the elements in the list datatype........


# In[ ]:





# In[18]:


print(students)


# In[ ]:


# req : i want modify varun name sravani.....


# In[ ]:





# In[19]:


students[2]="sravani"


# In[20]:


print(students)


# In[ ]:


# i want to delete  sravani name from the aabove list.....


# In[ ]:





# In[22]:


del students[2]


# In[23]:


print(students)


# In[ ]:


# temporary deleting


# In[ ]:


# it will be creating a carbon copy of the delete item..


# In[ ]:


get_ipython().run_line_magic('pinfo', 'list')


# In[24]:


print(students)


# In[25]:


x=students.pop()


# In[26]:


print(students)


# In[27]:


print(x)


# In[ ]:


what is the difference between delete and pop method in the list datatype....?


# In[ ]:





# In[ ]:





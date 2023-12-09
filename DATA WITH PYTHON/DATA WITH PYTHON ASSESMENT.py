#!/usr/bin/env python
# coding: utf-8

# # NUMPY

# In[1]:


#Q.1 Convert a 1D array to a 2D array with 2 rows 


# In[2]:


import numpy as np


# In[3]:


meal=np.array([11,12,13,14,15,16,17,18,19,20])
print(meal,"\n")
sun=meal.reshape(2,5)
print(sun)


# In[ ]:





# In[4]:


#Q.2 Get the common items between a and b 


# In[5]:


#Q.2 Get the common items between a and b 


# In[6]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c=np.intersect1d(a,b)
print(c)


# In[ ]:





# In[7]:


#Q.3 Get all items between 5 and 10 from a.


# In[8]:


a = np.array([2, 6, 1, 9, 10, 3, 27]) 
c=a[(a>=5)&(a<=10)]
print(c)


# In[ ]:





# In[9]:


#Q.4 Limit the number of items printed in python NumPy array a to a maximum of 6
#elements. 


# In[10]:


array1=np.array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]) 
array1[:6]


# In[ ]:





# # PANDAS :-

# In[11]:


#1. Compute the minimum, 25th percentile, median, 75th, and maximum of ser.


# In[12]:


import numpy as np


# In[13]:


import pandas as pd


# In[14]:


sun=pd.Series(np.random.randn(100))
moon=np.percentile(sun,q=[0,25,50,75,100])
print('minimum:',moon[0])
print('25th percentile:',moon[1])
print("Median: ", moon[2])
print("75th percentile: ",moon[3])
print("Maximum: ",moon[4])


# In[ ]:





# In[15]:


#2. Creating A Pandas Data Frame and Using Sample Data Sets 


# In[16]:


name1={'name':['meet','khushi','raj','isha','ronak'],
     'age':['20','20','24','21','28']}
print(name1 ,'\n\n')

meet=pd.DataFrame(name1)
print(meet)


# In[ ]:





# In[17]:


#3. Using NumPy, create a Pandas Data Frame with five rows and three columns. 


# In[18]:


meet=np.random.rand(5,3)
print(meet)
df=pd.DataFrame(meet)
print(df)


# In[19]:


#4. For a Pandas Data Frame created from a NumPy array, what is the default behavior for
#the labels for the columns? For the rows? 


# In[20]:


INDIA= np.array([['gujrat', 'maharashtra', 'panjab'], ['keral','tamilnadu','karnatak'], ['assam','jarkhand','meghalay']])
df=pd.DataFrame(INDIA)
df


# In[21]:


#5. take csv file contains at least 10,000 rows and 12 columns which numerical and text values
#according to that continue following steps


# In[22]:


bharat=pd.read_csv("C:\\Users\\MEET HIRPARA\\Downloads\\business-employment-data-march-2023-quarter-regional-council-revisions.csv")
bharat


# In[23]:


#6. Write the code to show the number of rows and columns in data frame. 


# In[24]:


print(bharat.shape)

num_rows, num_cols = bharat.shape

print(f"Number of rows: {num_rows}")

print(f"Number of columns: {num_cols}")
bharat


# In[25]:


#7. How might you show the first few rows of data frame? 


# In[26]:


bharat.head()


# In[27]:


#8. If you select a single column from the diamonds Data Frame, what will be the type of the
#return value? 


# In[28]:


import seaborn as sns


# In[29]:


rose=sns.load_dataset('tips')
print(rose)
nose=rose['total_bill']
print(type(nose))


# In[30]:


#9. Create a line plot using the x and y values provided below. Label the y-axis as “Y” and
#label the x-axis as “X”.


# In[31]:


import matplotlib.pyplot as plt


# In[32]:


x = [15,25,35,45,55]
y = [3,3.5,4,4.5,5]

plt.plot(x, y)

plt.xlabel('X')
plt.ylabel('Y')

plt.show()


# In[33]:


#10. Create an array of numbers between 0 and 6 with increments of 0.3 and name its “x”.
#Then on the same plot, plot x, x², x³, and x⁴. For consistency, use the following style lines
#respectively, “ro”, “bs”, “g”, and “:”. Lastly, make sure that the x-axis covers 0 to 6, while
#the y-axis spans from 0 to 125. Do not worry if you are not familiar with the style lines —
#you will recognize them as soon as you see the plot. 


# In[37]:


meet= np.arange(0, 6.3, 0.3)
print(list(meet))

plt.plot(x, x, 'ro', label='x')      
plt.plot(x, x**2, 'bs', label='x²')  
plt.plot(x, x**3, 'g', label='x³')   
plt.plot(x, x**4, ':', label='x⁴')   

plt.xlim(0, 6)
plt.ylim(0, 125)


plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()


plt.show()


# In[ ]:


#11. Heights and initials of a group of individuals are provided below. Create a bar plot titled
#“Height Comparison” to compare the heights among this group.
#height = [179, 155, 191, 152, 188, 177]
#names = ['QA', 'WB', 'EC', 'RD', 'TE', 'YF'] 


# In[40]:


height = [179, 155, 191, 152, 188, 177]
names = ['QA', 'WB', 'EC', 'RD', 'TE', 'YF'] 

plt.bar(names, height, color='green')

plt.title('Height male')
plt.xlabel('Names')
plt.ylabel('Height (cm)')


# In[ ]:


#12. Plot a histogram of x, where x consists of 100,000 randomly-selected points with a normal
#distribution (hint: you can use numpy.random.randn() to generate the random points). The
#histogram should have 10 bins. Look at how the histogram changes when we try 20 and 50
#bins. 


# In[44]:


x = np.random.randn(100000)

plt.hist(x, bins=10, color='blue', edgecolor='red')
plt.title('Histogram 10 Bins')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

plt.hist(x, bins=20, color='green', edgecolor='yellow')
plt.title('Histogram 20 Bins')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

plt.hist(x, bins=50, color='orange', edgecolor='pink')
plt.title('Histogram 50 Bins')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()


# In[ ]:





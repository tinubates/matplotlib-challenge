#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Dependencies and Setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')

# File to Load (Remember to Change These)
mouse_drug_data_to_load = "data/mouse_drug_data.csv"
clinical_trial_data_to_load = "data/clinicaltrial_data.csv"

# Read the Mouse and Drug Data and the Clinical Trial Data
mousedata=pd.read_csv(mouse_drug_data_to_load)
clinicaldata=pd.read_csv(clinical_trial_data_to_load)

# Combine the data into a single dataset
data=pd.merge(mousedata,clinicaldata)

# Display the data table for preview
data


# ## Tumor Response to Treatment

# In[3]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 
tumor=data.groupby(['Drug','Timepoint']).mean().reset_index()
tumor=tumor.rename(columns={'Tumor Volume (mm3)':'TVolume'})
tumor=tumor.drop(['Metastatic Sites'],axis=1)

# Preview DataFrame
tumor


# In[ ]:





# In[4]:


# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
error=data.groupby(['Drug','Timepoint']).sem().reset_index()
error=error.rename(columns={'Tumor Volume (mm3)':'TVolume'})
error=error.drop(['Metastatic Sites','Mouse ID'],axis=1)

# Preview DataFrame
error


# In[3]:





# In[5]:


# Minor Data Munging to Re-Format the Data Frames
tumorformat=pd.crosstab(tumor.Timepoint,tumor.Drug,values=tumor['TVolume'],aggfunc='mean')
errorformat=pd.crosstab(error.Timepoint,error.Drug,values=error['TVolume'],aggfunc='mean').reset_index()
errorformat.reset_index()
# Preview that Reformatting worked
errorformat


# In[4]:





# In[7]:


# Generate the Plot (with Error Bars)
tumorformat.plot(yerr=error['TVolume'])
# Save the Figure
plt.savefig('tumorplot.png')


# In[8]:


# Show the Figure
plt.show()


# ![Tumor Response to Treatment](../Images/treatment.png)

# ## Metastatic Response to Treatment

# In[9]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 
met=data.groupby(['Drug','Timepoint']).mean().reset_index()
met=met.rename(columns={'Metastatic Sites':'MSites'})
met=met.drop(['Tumor Volume (mm3)'],axis=1)
# Convert to DataFrame

# Preview DataFrame
met


# In[6]:





# In[21]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 
meterror=data.groupby(['Drug','Timepoint']).sem().reset_index()
meterror=meterror.rename(columns={'Metastatic Sites':'MSites'})
meterror=meterror.drop(['Tumor Volume (mm3)','Mouse ID'],axis=1)
# Preview DataFrame
meterror.head()
# Convert to DataFrame

# Preview DataFrame


# In[7]:





# In[26]:


# Minor Data Munging to Re-Format the Data Frames
metformat=pd.crosstab(met.Timepoint,met.Drug,values=met['MSites'],aggfunc='mean')
meterrorformat=pd.crosstab(meterror.Timepoint,meterror.Drug,values=meterror['MSites'],aggfunc='mean').reset_index()
meterrorformat
# Preview that Reformatting worked


# In[8]:





# In[28]:


# Generate the Plot (with Error Bars)
metformat.plot(yerr=meterror['MSites'])
# Save the Figure
plt.savefig('metplot.png')


# ![Metastatic Spread During Treatment](../Images/spread.png)

# ## Survival Rates

# In[29]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
mice=data.groupby(['Drug','Timepoint']).count().reset_index()
mice=mice.rename(columns={'Mouse ID':'Mouse Count'})
mice=mice.drop(['Metastatic Sites','Tumor Volume (mm3)'],axis=1)
# Convert to DataFrame
mice
# Preview DataFrame


# In[10]:





# In[31]:


# Minor Data Munging to Re-Format the Data Frames
miceformat=pd.crosstab(mice.Timepoint,mice.Drug,values=mice['Mouse Count'],aggfunc='mean')
miceformat
# Preview the Data Frame


# In[11]:





# In[33]:


# Generate the Plot (Accounting for percentages)
miceformat.plot()
# Save the Figure
plt.savefig('survivalplot.png')


# ![Metastatic Spread During Treatment](../Images/survival.png)

# ## Summary Bar Graph

# In[ ]:


# Calculate the percent changes for each drug

# Display the data to confirm


# In[13]:





# In[ ]:


# Store all Relevant Percent Changes into a Tuple


# Splice the data between passing and failing drugs


# Orient widths. Add labels, tick marks, etc. 


# Use functions to label the percentages of changes


# Call functions to implement the function calls


# Save the Figure


# Show the Figure
fig.show()


# ![Metastatic Spread During Treatment](../Images/change.png)

# In[ ]:





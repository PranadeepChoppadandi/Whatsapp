#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system(' pip install pywhatkit')


# In[3]:


import pywhatkit as kit

# Parameters:
# phone number (with country code, e.g., "+1234567890")
# message
# hour (24-hour format)
# minute

phone_number = "+919010330530"
message = "Hello, this is an automated message!, to test the whatsapp automation project using python"
hour = 11  # 2 PM
minute = 48

try:
    kit.sendwhatmsg(phone_number, message, hour, minute)
    print("Message scheduled successfully!")
except Exception as e:
    print(f"An error occurred: {e}")


# In[ ]:





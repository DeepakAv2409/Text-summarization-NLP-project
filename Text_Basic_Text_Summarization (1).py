#!/usr/bin/env python
# coding: utf-8

# ### Deepak AV
# ### Natural Langauge Processing - Text Summarization 

# In[1]:


#importing Necessary libraries 
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist


# In[2]:


#Inputing Data
text = "This is a sample text for summarization. It has multiple sentences and is used to demonstrate the text summarization process. The process of text summarization involves identifying the important information from the text and condensing it into a shorter and more concise form. It is a useful tool for quickly understanding the main points of a document or article. There are various methods for text summarization, including extractive and abstractive approaches. The extractive approach involves selecting important sentences or phrases from the original text and presenting them in a summary. The abstractive approach involves creating a summary by generating new text that is similar to the original text. Both approaches have their own advantages and limitations, and the appropriate method depends on the specific needs of the task."


# In[3]:


#preprocessing the text
text = re.sub(r'[[0-9]*]', ' ', text)
text = re.sub(r'\s+', ' ', text)


# In[4]:


nltk.download('punkt')


# In[5]:


#tokenizing the text
sentences = nltk.sent_tokenize(text)
sentences


# In[6]:


#creating a frequency distribution of the words
word_freq = FreqDist(word_tokenize(text))
word_freq 


# In[7]:


#selecting the most frequent words
most_freq = word_freq.most_common(20)
most_freq


# In[8]:


#creating a list of the most frequent words
most_freq_words = [word[0] for word in most_freq]
most_freq_words


# In[9]:


#creating a list of the sentences containing the most frequent words
important_sentences = []
for sentence in sentences:
  for word in most_freq_words:
    if word in sentence:
      important_sentences.append(sentence)
      break


# In[10]:


#creating the summary
summary = " ".join(important_sentences)
print(summary)


# In[ ]:





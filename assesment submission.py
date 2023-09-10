#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[2]:


from googletrans import Translator 
# Function to convert English text to Hinglish
def translate_to_hinglish(text):
    # Initialize the translator
    translator = Translator()

    # Define a dictionary for English to Hinglish replacements
    replacements = {
        'definitely': 'पक्का',
        'feedback': 'सुझाव',
        'comment section': 'कमेंट सेक्शन',
        'big video': 'बड़ा वीडियो',
        'clearly mention': 'स्पष्ट रूप से बताऊँगा',
        'waiting': 'इंतजार',
        'bag': 'बैग',
    }

    # Replace English words with Hinglish equivalents
    for word, replacement in replacements.items():
        text = text.replace(word, replacement)

    # Translate remaining English words to Hinglish using googletrans
    words = text.split()
    for i, word in enumerate(words):
        if word.isalpha() and word not in replacements.values():
            hinglish_word = translator.translate(word, src='en', dest='hi').text
            words[i] = hinglish_word

    # Reconstruct the translated text
    hinglish_text = ' '.join(words)

    return hinglish_text

# Input English text
input_text = "hi how aew you i am fine ."

# Translate to Hinglish
hinglish_text = translate_to_hinglish(input_text)

# Print the Hinglish text
print(hinglish_text)


# In[ ]:





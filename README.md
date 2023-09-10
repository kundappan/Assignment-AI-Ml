# Assignment-AI-Ml
from googletrans import Translator
#This line imports the Translator class from the googletrans library. It's used for translating text from English to Hindi (Hinglish).

# Function to convert English text to Hinglish
def translate_to_hinglish(text):
#This block defines a function named translate_to_hinglish that takes an English text input as a parameter and will return the Hinglish translation.

    # Initialize the translator
    translator = Translator()
#Here, you initialize the translator object from the googletrans library, which will be used for translating words from English to Hindi.

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
#This part defines a dictionary called replacements, where you map English words to their Hinglish equivalents. This is used to replace certain words directly without translation.

    # Replace English words with Hinglish equivalents
    for word, replacement in replacements.items():
        text = text.replace(word, replacement)

#Here, you loop through the dictionary replacements and replace the English words in the input text with their corresponding Hinglish words.

    # Translate remaining English words to Hinglish using googletrans
    words = text.split()
    for i, word in enumerate(words):
        if word.isalpha() and word not in replacements.values():
            hinglish_word = translator.translate(word, src='en', dest='hi').text
            words[i] = hinglish_word
#In this part, you split the remaining words in the input text into a list called words. Then, you iterate through each word in the list. If a word is alphabetic (not a number or special character) and it's not already in the replacements dictionary, you use the googletrans library to translate it from English to Hindi (Hinglish) and update the word in the words list.

    # Reconstruct the translated text
    hinglish_text = ' '.join(words)
#Here, you join the translated words in the words list to create the final Hinglish translation.

    return hinglish_text
#This line indicates that the function should return the Hinglish translation as the output.

# Input English text
input_text = "hi how aew you."
#Here, you define the input English text that you want to translate into Hinglish.

# Translate to Hinglish
hinglish_text = translate_to_hinglish(input_text)
#This line calls the translate_to_hinglish function with the input text and stores the translated Hinglish text in the variable hinglish_text.

# Print the Hinglish text
print(hinglish_text)
#Finally, you print the translated Hinglish text to the console.


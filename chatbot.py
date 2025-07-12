from googletrans import Translator
import json

translator = Translator()

# Load intents
with open('intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)['intents']

def translate_to_english(text):
    return translator.translate(text, dest='en').text

def translate_from_english(text, dest_lang):
    return translator.translate(text, dest=dest_lang).text

"""def get_response(user_input):
    user_input_en = translate_to_english(user_input).lower()

    for intent in intents:
        for pattern in intent['patterns']:
            if pattern.lower() in user_input_en or any(word in user_input_en for word in pattern.lower().split()):
                return intent['response']
    
    return "Sorry, I couldn't understand that. Please ask something else."
"""
import re
from difflib import SequenceMatcher

def preprocess(text):
    return re.sub(r'[^\w\s]', '', text.lower()).strip()

def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_response(user_input):
    user_input_en = translate_to_english(user_input)
    processed_input = preprocess(user_input_en)

    best_match = None
    best_score = 0.0

    for intent in intents:
        for pattern in intent['patterns']:
            processed_pattern = preprocess(pattern)
            score = similarity(processed_input, processed_pattern)

            if score > best_score:
                best_score = score
                best_match = intent

    # Only respond if similarity score is reasonably high
    if best_match and best_score > 0.5:
        return best_match['response']
    else:
        return "Sorry, I couldn't understand that. Can you rephrase it?"

import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

class Chatbot:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.responses = {
            "hello": "Hi there!",
            "hi": "Hello! How can I help you?",
            "how are you": "I'm doing great, thanks! How about you?",
            "bye": "Goodbye!",
            "what is your name": "I'm Grok, nice to meet you!",
            "default": "Sorry, I don’t understand that. Try something else!"
        }

    def process_input(self, user_input):
        tokens = word_tokenize(user_input.lower())
        return [self.lemmatizer.lemmatize(token) for token in tokens]

    def get_response(self, tokens):
        input_str = " ".join(tokens)
        for pattern, response in self.responses.items():
            if pattern in input_str:
                return response
        return self.responses["default"]
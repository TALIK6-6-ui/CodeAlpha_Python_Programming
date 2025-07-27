import random
import re

# Define possible intents and their keywords
response_map = {
    "greeting": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening"],
        "responses": ["Hi!", "Hello there!", "Hey!", "Hi, how can I help?"]
    },
    "wellbeing": {
        "keywords": ["how are you", "how are you doing", "what's up"],
        "responses": ["I'm fine, thanks!", "Doing great, thanks for asking!", "I'm good! How about you?"]
    },
    "farewell": {
        "keywords": ["bye", "goodbye", "see you", "later"],
        "responses": ["Goodbye!", "See you next time!", "Bye! Have a great day!"]
    }
}

def clean_input(text):
    """
    Normalize and clean user input.
    """
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text.strip()

def get_intent(user_input):
    """
    Match the user input to an intent based on keyword presence.
    """
    for intent, data in response_map.items():
        for keyword in data["keywords"]:
            if keyword in user_input:
                return intent
    return "unknown"

def get_response(intent):
    """
    Return a random response based on the matched intent.
    """
    if intent in response_map:
        return random.choice(response_map[intent]["responses"])
    else:
        return "Sorry, I didn't understand that."

def chatbot():
    """
    Main chatbot loop.
    """
    print("🤖 Smarter Chatbot is ready! Type 'bye' to exit.\n")
    
    while True:
        user_input = input("You: ")
        cleaned_input = clean_input(user_input)
        intent = get_intent(cleaned_input)
        response = get_response(intent)
        print("Bot:", response)

        if intent == "farewell":
            break

# Run the chatbot
if __name__ == "__main__":
    chatbot()

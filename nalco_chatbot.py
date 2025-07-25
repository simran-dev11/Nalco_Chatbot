import nltk
import time
from datetime import datetime

faq = {
    'what is nalco': 'NALCO is National Aluminium Company Limited, a Navratna PSU under the Ministry of Mines.',
    'where is nalco located': 'NALCO has its headquarters in Bhubaneswar, Odisha, India.',
    'tell me about nalco history': 'NALCO was established in 1981. It is one of India’s largest integrated aluminium producers.',
    'what are nalco safety instructions': 'Safety is top priority. Always wear helmets, follow SOPs, and use safety gear in hazardous areas.',
    'what are nalco holidays': 'NALCO follows the central government holiday list including Republic Day, Holi, Independence Day, and Diwali.',
    'who owns nalco': 'NALCO is owned by the Government of India under the Ministry of Mines.',
    'what is alumina': 'Alumina is a refined product from bauxite used to produce aluminium.',
    'who is the chairman of nalco': 'As of 2024, the CMD is Sridhar Patra. Please verify on the official site for updates.',
    'what does nalco produce': 'NALCO primarily produces bauxite, alumina, and aluminium products.',
    'what is the smelter plant': 'NALCO\'s smelter plant is located in Angul and produces aluminium metal using electrolysis.',
}

def get_response(user_input):
    user_input = user_input.lower()
    for question in faq:
        if question in user_input:
            return faq[question]
    return "I'm sorry, I don't understand that. Please try asking differently."

def greet_user():
    hour = datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def bot_print(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

def log_chat(user, bot):
    with open("nalco_chat_log.txt", "a") as log:
        log.write(f"You: {user}\\nBot: {bot}\\n\\n")

print("🤖 Welcome to the NALCO Assistant!")
bot_print(greet_user() + " I’m your chatbot assistant for NALCO.")
print("Type 'exit' or 'quit' to end the conversation.\n")

while True:
    user_input = input("You: ")
    if user_input.lower().strip() in ['exit', 'quit', 'bye']:
        farewell = "Thank you for chatting with NALCO. Have a productive day!"
        bot_print("Bot: " + farewell)
        log_chat(user_input, farewell)
        break
    response = get_response(user_input)
    bot_print("Bot: " + response)
    log_chat(user_input, response)

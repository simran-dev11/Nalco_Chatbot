# 🤖 NALCO Chatbot Assistant

This project is a simple yet functional **Python console chatbot** designed to answer frequently asked questions about **NALCO** (National Aluminium Company Limited). It was built to explore how far I could go with basic logic and user interaction in Python — no fancy machine learning, just simple and clean logic.

---

## 📘 Introduction

This chatbot project started as a fun idea after learning about basic text handling and control structures in Python. I wanted to create something that could simulate a real conversation (in a minimal way) and be useful for answering common organizational questions.

Since NALCO is a well-known public sector company in India, I thought — **why not build a chatbot that knows a few things about it?** And that’s exactly what I did.

I kept it console-based and lightweight but made sure it felt interactive — including time-based greetings and even a chat logging feature. The result is a small yet complete chatbot that’s easy to run and customize.

---

## 🛠️ Functionalities

### 1. 💬 Interactive FAQ Chatbot

- The bot starts with a friendly greeting depending on the time of the day (morning/afternoon/evening).
- It listens to your questions and matches them with pre-set questions stored in a dictionary.
- If the input matches (even partially), it returns the correct response.
- If it doesn’t understand the question, it politely asks you to rephrase.

Some examples of supported questions:
- `What is NALCO?`
- `Where is NALCO located?`
- `What does NALCO produce?`
- `What are NALCO holidays?`
- `What are NALCO safety instructions?`

### 2. 🧠 Simple Matching Logic

The chatbot uses basic keyword matching:
- All questions are stored in lowercase in a dictionary.
- The user input is also converted to lowercase for matching.
- If a key exists inside the input, the corresponding answer is returned.
- Otherwise, it responds with a default "I don’t understand" message.

It’s not AI-powered, but it gets the job done for fixed Q&A!

### 3. 📝 Chat Logging

Every question you ask and every response the bot gives is saved in a file called `nalco_chat_log.txt`. This could be helpful for reviewing conversations or improving the chatbot later.

The format is simple and clean:
```
You: <your question>
Bot: <bot's answer>
```

### 4. 👋 Time-Based Greeting

The bot greets you based on your system clock:
- `Good morning!` if it’s before noon
- `Good afternoon!` from noon to 6 PM
- `Good evening!` after 6 PM

It adds a nice human touch to the interaction.

---

## 🧰 Technologies Used

- **Python 3.x**
- `datetime` module (for greeting)
- `time.sleep` (for typing animation)
- Simple file handling (for chat logging)
- Dictionary-based logic (for FAQs)

---

## 🚀 How to Run the Chatbot

1. Make sure you have **Python 3** installed on your computer.
2. Download or clone the project folder.
3. Open a terminal and navigate to the folder.
4. Run the script:
   ```bash
   python nalco_chatbot.py
   ```
5. Start chatting! To end the session, type:
   ```
   exit
   ```
   or
   ```
   quit
   ```

---

## 💡 What You Can Ask

Here are some sample queries the chatbot understands:

- `What is NALCO?`
- `Tell me about NALCO history`
- `Who is the chairman of NALCO?`
- `Where is the smelter plant?`
- `What is alumina?`
- `Who owns NALCO?`
- `What are NALCO safety instructions?`

If your question doesn’t match, try rephrasing it. The bot only recognizes specific keywords for now.

---

## ✨ What I Learned

- How to work with user input and conditional logic in Python
- How to build simple rule-based chatbots without AI
- How to use file handling to store logs
- How to create more natural interactions with delays and greetings

---

## 📅 Last Updated

**June 2025**

---

Feel free to fork this project, improve it, or add new features like GUI support, NLP integration, or speech recognition. The goal was to keep it minimal, functional, and fun to build. 😊

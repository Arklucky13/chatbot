# chatbot.py
# Simple rule-based chatbot using if-elif-else loops

print("Welcome to SimpleChat! Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    elif "hello" in user or "hi" in user:
        print("Chatbot: Hello! How can I help you today?")
    elif "name" in user:
        print("Chatbot: I am SimpleChat, your rule-based chatbot.")
    elif "help" in user:
        print("Chatbot: Sure! You can ask me basic questions like greetings or my name.")
    elif "how are you" in user:
        print("Chatbot: I am just code, but I'm functioning perfectly! :)")
    else:
        print("Chatbot: Sorry, I don't understand that yet.")

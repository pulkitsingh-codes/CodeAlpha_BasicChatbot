# Simple Rule-Based Chatbot

print("Welcome to My Chatbot!")
print("You can start chatting with me.")
print("Type 'bye' to exit the chat.")

def chatbot_response(message):

    message = message.lower()

    if message == "hello":
        return "Hi! How are you?"

    elif message == "how are you":
        return "I'm fine, thank you!"

    elif message == "what is your name":
        return "I am a simple Python chatbot."

    elif message == "who created you":
        return "I was created using Python."

    elif message == "what can you do":
        return "I can reply to some basic messages."

    elif message == "bye":
        return "Goodbye! Have a nice day."

    else:
        return "Sorry, I don't understand that."

# Chat loop
while True:

    user_message = input("\nYou: ")

    reply = chatbot_response(user_message)

    print("Bot:", reply)

    if user_message.lower() == "bye":
        break

print("\nChat ended. Thank you!")
def reply(user_text):
    if user_text == "hello":
        return "Hi!"
    elif user_text == "how are you":
        return "I'm fine, thanks!"
    elif user_text == "what is your name":
        return "I am a simple chatbot."
    elif user_text == "good morning":
        return "Good morning!"
    elif user_text == "good night":
        return "Good night!"
    elif user_text == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand."
chat_count = 0
while True:
    user_input = input("You : ").lower()
    chat_count += 1
    bot_reply = reply(user_input)
    print("Bot :", bot_reply)
    if user_input == "bye":
        break
print("\nTotal messages entered :", chat_count)
print("Chat ended.")
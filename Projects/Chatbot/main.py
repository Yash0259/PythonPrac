def chatbot_response(user_input):
    response = { 
            "hi":"Hello! How can i help you?",
            "bye":"Goodbye! Have a great day!",
            "how are you":"I'm just a bot,but i'am doind great. How can i help you :"
            }
    return response.get(user_input.lower(),"Sorry, I don't understand that.")

while True:
        user_input = input("You: ")
        if user_input.lower() in ["bye","exit"]:
            print("Chatbot: BYE!")
            break
        print("Chatbot:",chatbot_response(user_input))

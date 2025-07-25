def get_chatbot_response(user_input):
    """
    Simple rule-based chatbot that responds to basic greetings and farewells.
    
    Args:
        user_input (str): The user's input message
        
    Returns:
        str: The chatbot's response
    """
    # Convert input to lowercase for case-insensitive matching
    user_input = user_input.lower().strip()
    
    # Define response rules using if-elif statements
    if user_input == "hello":
        return "Hi!"
    elif user_input == "how are you":
        return "I'm fine, thanks!"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "I don't understand that. Try saying 'hello', 'how are you', or 'bye'."

def main():
    """
    Main function to run the chatbot in a loop.
    """
    print("=== Simple Rule-Based Chatbot ===")
    print("Type 'quit' to exit the chatbot.")
    print("Try saying: hello, how are you, bye")
    print("-" * 40)
    
    while True:
        # Get user input
        user_input = input("You: ")
        
        # Check if user wants to quit
        if user_input.lower() == "quit":
            print("Chatbot: Thanks for chatting! Goodbye!")
            break
        
        # Get chatbot response
        response = get_chatbot_response(user_input)
        
        # Display response
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
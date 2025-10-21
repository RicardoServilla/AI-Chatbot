import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat_with_ai():
    print("Welcome to AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=user_input,
            max_tokens=150
        )
        print("AI:", response.choices[0].text.strip())

if __name__ == "__main__":
    chat_with_ai()

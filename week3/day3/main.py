from dotenv import load_dotenv
from groq import Groq
import os

load_dotenv()

client = Groq()

SYSTEM_PROMPT = "You are a helpful, concise coding assistant."

def ask_llm(conversation_history):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=conversation_history
    )
    return response.choices[0].message.content

def main():
    print("Chatbot with Memory (type 'quit' to exit)\n")

    conversation_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        try:
            user_input = input("You: ")
        except KeyboardInterrupt:
            print("\nExiting chat. Bye!")
            break

        if user_input.lower() == "quit":
            break

        conversation_history.append({"role": "user", "content": user_input})
        
        reply = ask_llm(conversation_history)
        conversation_history.append({"role": "assistant", "content": reply})
        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    main()
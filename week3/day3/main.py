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

    # This list IS the conversation. It only ever grows.
    conversation_history = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    while True:
        user_input = input("You: ")
        if user_input.lower() == "quit":
            break

        # 1. Add the user's new message to the notepad
        conversation_history.append({"role": "user", "content": user_input})

        # 2. Send the ENTIRE notepad, get a reply
        reply = ask_llm(conversation_history)

        # 3. Add the bot's own reply back into the notepad too — 
        #    otherwise it forgets what IT said, which is just as important
        conversation_history.append({"role": "assistant", "content": reply})

        print(f"Bot: {reply}\n")

if __name__ == "__main__":
    main()
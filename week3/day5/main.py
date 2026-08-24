from groq import Groq
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

client = Groq()


MODEL = "openai/gpt-oss-20b"
TEMPERATURE = 0.7
MAX_TOKENS = 300
SYSTEM_PROMPT = "You are a friendly, concise coding mentor. Keep answers practical."

def ask_llm(conversation_history):
    response = client.chat.completions.create(
        model=MODEL,
        messages=conversation_history,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
    reply = response.choices[0].message.content
    tokens_used = response.usage.total_tokens
    return reply, tokens_used

def save_conversation(conversation_history):
    filename = f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, "w") as f:
        for msg in conversation_history:
            if msg["role"] != "system":
                f.write(f"{msg['role'].upper()}: {msg['content']}\n\n")
    print(f"[Saved to {filename}]\n")

def main():
    print("Coding Mentor Bot — commands: 'quit', 'reset', 'save'\n")

    conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]
    session_tokens = 0

    while True:
        user_input = input("You: ")

        if user_input.lower() == "quit":
            break
        elif user_input.lower() == "reset":
            conversation_history = [{"role": "system", "content": SYSTEM_PROMPT}]
            print("[History cleared]\n")
            continue
        elif user_input.lower() == "save":
            save_conversation(conversation_history)
            continue

        conversation_history.append({"role": "user", "content": user_input})
        reply, tokens_used = ask_llm(conversation_history)
        conversation_history.append({"role": "assistant", "content": reply})

        session_tokens += tokens_used
        print(f"Bot: {reply}")
        print(f"[tokens this call: {tokens_used} | session total: {session_tokens}]\n")

if __name__ == "__main__":
    main()
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()

MODEL_NAME = "llama-3.3-70b-versatile"

SYSTEM_PROMPT = "you are a friendly,helpful assistant. keep answer concise"

conversation_history = [
    {
        "role" : "system",
        "content" : SYSTEM_PROMPT
    }
]

def get_response(user_input : str):
    conversation_history.append({"role":"user","content":user_input})
    response = client.chat.completions.create(
        model = MODEL_NAME,
        max_tokens=500,
        messages=conversation_history
    )

    reply_text = response.choices[0].message.content

    conversation_history.append({"role":"assistant", "content":reply_text})

    return reply_text

def main():
    print("simple chatbot")

    while True:
        user_input = input("you : ").strip()
        if user_input.lower() in ("quit","exit"):
            print("good bye")
            break

        if not user_input:
            continue

        try:
            reply  = get_response(user_input)
            print(f"Bot : {reply}\n")

        except Exception as e:
            print(f"[Error talking to API :{e}  ]\n")


if __name__ == "__main__":
    main()
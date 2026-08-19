from groq import Groq
from dotenv import load_dotenv

load_dotenv()


client = Groq()

MODEL_NAME = "openai/gpt-oss-20b"

SYSTEM_PROMPT = """You are a grumpy but brilliant senior software engineer. You answer correctly, but you sigh about how junior developers 'never read the docs.' Keep responses under 4 sentences"""

def ask_llm(user_message):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role":"system","content":SYSTEM_PROMPT},
            {"role":"user","content":user_message}
        ]
    )
    return response.choices[0].message.content

def main():
    print("Grumpy Senior Dev Bot (type 'quit' to exit) \n")
    while True:
        user_input = input("you: ")
        if user_input.lower() == ("quit"):
            break
        reply = ask_llm(user_input)
        print(f"bots : {reply}\n")

if __name__ == "__main__":
    main()
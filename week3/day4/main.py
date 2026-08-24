from groq import Groq
from dotenv import load_dotenv


load_dotenv()

client = Groq()


PROMPT = "Write a one-sentence story about a lost cat."

def run(temperature, max_tokens, label):
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": PROMPT}],
        temperature=temperature,
        max_tokens=max_tokens
    )
    text = response.choices[0].message.content
    finish_reason = response.choices[0].finish_reason
    print(f"--- {label} (temp={temperature}, max_tokens={max_tokens}) ---")
    print(text)
    print(f"[finish_reason: {finish_reason}]\n")

def main():
   
    run(0, 100, "Low temp, run 1")
    run(0, 100, "Low temp, run 2")
    run(0, 100, "Low temp, run 3")

    
    run(1.3, 100, "High temp, run 1")
    run(1.3, 100, "High temp, run 2")
    run(1.3, 100, "High temp, run 3")

    
    run(0.7, 8, "Truncated by max_tokens")

if __name__ == "__main__":
    main()
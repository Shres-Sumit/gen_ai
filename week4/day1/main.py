from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq()

MODEL = "openai/gpt-oss-20b"

text_message = [
    "my orders arrived broken and nobody has replied to my emails.",
    "Does this laptop come with a charger included?",
    "Honestly this is the best customer service I've ever had!",
    "I've been waiting 3 weeks and still no refund",
]

def classify_zero_shot(message):
   prompt = f"""Classify the following customer message into exactly one category: Complaint, Question, or Praise.Message : {message}Respond with ONLY the category name, nothing else."""
   response = client.chat.completions.create(
       model = MODEL,
       messages = [{"role":"user","content":prompt}],
       temperature=0,
   )
   return response.choices[0].message.content.strip()

#few_shot
def classify_few_shot(message):
  prompt = f"""Classify customer messages into exactly one category: Complaint, Question, or Praise.

Examples:
Message: "This product broke after two days, I want a refund."
Category: Complaint

Message: "What colors does this come in?"
Category: Question

Message: "This exceeded my expectations, thank you!"
Category: Praise

Now classify this one:
Message: "{message}"
Category:"""
  response = client.chat.completions.create(
      model = MODEL,
      messages = [{"role":"user","content":prompt}],
      temperature=0
  )

  return response.choices[0].message.content.strip()

if __name__ == "__main__":
   print(f"{'MESSAGE':<55} {'ZERO-SHOT':<12} {'FEW-SHOT':<12}")
   print("-" * 80)
   for msg in text_message:
        zero = classify_zero_shot(msg)
        few = classify_few_shot(msg)
        short_msg = (msg[:50] + "...") if len(msg) > 50 else msg
        print(f"{short_msg:<55} {zero:<12} {few:<12}")

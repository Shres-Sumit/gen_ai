from groq import Groq
import json
from dotenv import load_dotenv

load_dotenv()

client = Groq()

MODEL = "openai/gpt-oss-20b"

test_messages = [
    "My order arrived broken and nobody has replied to my emails in 5 days.",
    "Does this laptop come with a charger included?",
    "Honestly this is the best customer service I've ever had!",
    "URGENT - my payment was charged twice, please fix this today.",
]

def extract_details(message):
  prompt = f"""Analyze this customer message and return ONLY a JSON object
(no explanation, no markdown code fences) with exactly these fields:

- "category": one of "Complaint", "Question", "Praise"
- "urgency": one of "Low", "Medium", "High"
- "summary": a one-sentence summary in your own words

Message: "{message}"

JSON:"""
  response = client.chat.completions.create(
      model = MODEL,
      messages = [{"role":"user","content":prompt}],
      temperature = 0
  )
  return response.choices[0].message.content.strip()

VALID_CATEGORIES = {"Complaint", "Question", "Praise"}
VALID_URGENCY = {"LOW","MEDIUM","HIGH"}

def parse_and_validate(raw_text):
  cleaned_text = raw_text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
  try:
    data = json.loads(cleaned_text)
  except json.JSONDecodeError as e:
        return None, f"Invalid JSON: {e}"

  required_fields = {"category", "urgency", "summary"}
  missing = required_fields - data.keys()

  if missing:
      return None, f"Missing fields: {missing}"

  if data["category"] not in VALID_CATEGORIES:
      return None, f"Bad category value: {data['category']}"

  if data["urgency"] not in VALID_URGENCY:
      return None, f"Bad urgency value: {data['urgency']}"

  return data, None

if __name__ == "__main__":
   for msg in test_messages:
        raw = extract_details(msg)
        data, error = parse_and_validate(raw)

        print(f"\nMessage: {msg}")
        if error:
            print(f"  ❌ VALIDATION FAILED: {error}")
            print(f"  Raw output was: {raw}")
        else:
            print(f"  ✅ category: {data['category']}")
            print(f"     urgency:  {data['urgency']}")
            print(f"     summary:  {data['summary']}")
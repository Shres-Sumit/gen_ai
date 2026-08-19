import os 
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()
client = OpenAI(
    api_key = os.environ['GROQ_API_key'],
    base_url=  "https://api.groq.com/openai/v1"
)

prompt = "Write one sentence about why the sky is blue."

for temp in [0, 0.7, 1,2]:
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=temp
    )
    print(f"\n--- Temperature = {temp} ---")
    print(response.choices[0].message.content)


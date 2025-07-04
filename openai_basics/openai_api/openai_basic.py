from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.responses.create(
    # model="gpt-4.1",
    model="omni-moderation-latest",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
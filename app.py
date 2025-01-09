import os
from io import StringIO
import openai
import argparse
from IPython.display import display, HTML
from dotenv import load_dotenv
client = openai.Client()

# Load the environment variables.
load_dotenv()

# Assign the environment variables.
openai.api_key = os.environ.get('OPENAI_API_KEY')
model = os.environ.get('MODEL')
temperature = float(os.environ.get('TEMPERATURE'))
max_tokens = int(os.environ.get('MAX_TOKENS'))
pre_prompt = os.environ.get('PRE_PROMPT')
prompt = os.environ.get('PROMPT')

# Concatenate the pre_prompt with the following prompt.
avoid_markdown_pre_prompt = "Never use markdown in the response you will provide, only simple text is allowed. For example: **test** is not allowed."
final_pre_prompt = pre_prompt + " " + avoid_markdown_pre_prompt

# Create a function to get prompt AI response
messages = [
    {
        "role": "system",
        "content": final_pre_prompt
        },
    {
        "role": "user",
        "content": prompt
    }
]

try:
    if not openai.api_key:
        raise ValueError("OpenAI API key is not set")

    if not prompt:
        raise ValueError("Prompt is not set")

    print("Generating AI response...\r\n")

    ai_response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Print the AI response
    print(ai_response.choices[0].message.content)

except Exception as e:
    print(f"An error occurred: {e}")

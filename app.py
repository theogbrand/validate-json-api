# app.py
from flask import Flask, render_template
import os
from openai import AzureOpenAI
import dotenv

dotenv.load_dotenv()
app = Flask(__name__)


@app.route('/')
def hello(name=None):
  azure_endpoint = "https://cursor-gpt-4.openai.azure.com"

  api_version="2024-02-15-preview"
  client = AzureOpenAI(
          azure_endpoint=azure_endpoint,
          api_version=api_version,
          api_key = os.environ["AZURE_OPENAI_API_KEY"],
  )
  
  response = client.chat.completions.create(
      model="pjf-dpo-turbo-35",
      # model="cursor-gpt-4",
      temperature = 0.9,
      messages=[
          {"role": "system", "content": "You are helpful assistant"},
          {"role": "user", "content": "what is meaning of life?"}
      ],
  )
  res = response.choices[0].message.content

  return res


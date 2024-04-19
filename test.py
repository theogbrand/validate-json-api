import pytest
from flask import Flask
from app import valid_json

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_valid_json(client):
  system_prompt = "system prompt test"
  user_prompt = "user prompt test"
  output_format = "output format test"
  response = client.post('/validate', json={
    'system_prompt': system_prompt,
    'user_prompt': user_prompt,
    'output_format': output_format
  })
  assert response.status_code == 200
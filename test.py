import pytest
from app import api

@pytest.fixture
def client():
  client = api.test_client()
  return client

def test_home_page(client):
  response = client.get('/validate')
  assert response.status_code == 200

# def test_valid_json(client):
#   system_prompt = "You are helpful assistant"
#   user_prompt = "hello"
#   output_format = {"Answer": "Answer to user prompt"}
#   response = client.get("/validate")
  
#   # ('/validate', json={
#   #   'system_prompt': system_prompt,
#   #   'user_prompt': user_prompt,
#   #   'output_format': output_format
#   # })
#   assert response.status_code == 200
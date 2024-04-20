import pytest
from app import api

@pytest.fixture
def client():
  client = api.test_client()
  return client

# def test_home_page(client):
#   response = client.get('/validate')
#   assert response.status_code == 200

def test_valid_json(client):
  subQnPrompt = """You are an AI language model assistant. Your task is to generate Five
    different versions of the given user question to retrieve relevant documents from a vector
    database. By generating multiple perspectives on the user question, your goal is to help
    the user overcome some of the limitations of the distance-based similarity search.
    Provide these alternative questions seperated by newlines only.

    For example:
    User question: "What is the conclusion of the paper?"

    Generated questions:
    What is the main takeaway from the paper?
    What are the key findings of the paper?
    What is the summary of the paper?
    What is the final thought of the paper?
    What is the ending of the paper?
    
    Output format should be as follows:

    'What is Bill Gates known for?'
│   "Can you provide information about Bill Gates' background?"

    And not this format:

    '1. What is Bill Gates known for?'
│   "2. Can you provide information about Bill Gates' background?"
    """
  
  user_prompt="What is the conclusion of the paper?",
  output_format = {'Generatd Questions': 'Five different versions of questions generated from user question, type: Array[str]',
                                     'Total Number of Questions Generated': 'Number of Generated Questions, type: int'
                                     }

  response = client.post('/validate', json={
    'system_prompt': subQnPrompt,
    'user_prompt': user_prompt,
    'output_format': output_format
  })
  

  assert response.status_code == 200
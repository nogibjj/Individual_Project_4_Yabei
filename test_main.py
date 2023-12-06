import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("API_TOKEN")

def test_html_files_in_directory(directory="templates/"):
    """Verifies the existence of HTML files in the specified directory."""
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            assert os.path.exists(filepath) and os.path.isfile(filepath)
            
def test_openai_api_response():
    """Validates the response from the OpenAI API."""
    prompt = "What's your name"
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Use appropriate engine model
        messages=messages,
        temperature=0,
    )
    print(response.choices[0].message["content"])
    assert response.choices[0].message["content"] is not None
    

if __name__ == "__main__":
    test_html_files_in_directory()
    test_openai_api_response()

from dotenv import load_dotenv
import openai
from flask import Flask, request, jsonify, render_template
import os

load_dotenv()
app = Flask(__name__)

# Use an environment variable for the API key for better security.
openai.api_key = os.getenv("API_TOKEN")

@app.route("/")
def index():
    """Returns the custom index page."""
    # Make sure 'idv4.html' is in the 'templates' directory.
    return render_template("idv4.html")

@app.route("/summarize", methods=["POST"])
def summarize_text():
    """Summarizes text using OpenAI's GPT-3.5-turbo model."""
    # Get the text from the POST request.
    data = request.get_json()
    text_to_summarize = data['text']

    try:
        # Use the OpenAI API to create a completion using the 'gpt-3.5-turbo' model.
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Specify the model here.
            prompt=f"Summarize the following text: {text_to_summarize}",
            max_tokens=150  # Adjust the max tokens as needed.
        )

        # Extract the summary text from the response.
        summary = response.choices[0].text.strip()
        return jsonify({'summary': summary})
    except openai.error.OpenAIError as e:
        # Return the error message and a 500 internal server error status.
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app.
    app.run(debug=True)

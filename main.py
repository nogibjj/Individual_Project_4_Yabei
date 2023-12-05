from dotenv import load_dotenv
import openai
from flask import Flask, request, jsonify, render_template
import os


load_dotenv()


app = Flask(__name__)


api_token = "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"
if not api_token:
    raise EnvironmentError("API_TOKEN not found. Please set the API_TOKEN environment variable.")

# 设置 OpenAI API 密钥
openai.api_key = api_token

@app.route("/")
def index():
    return render_template("idv4.html")

@app.route("/summarize", methods=["POST"])
def summarize_text():

    try:
        data = request.get_json()
        text_to_summarize = data['text']


        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Summarize the following text,The summarized text needs to be under 280 tokens: {text_to_summarize}",
            max_tokens=300
        )

        summary = response.choices[0].text.strip()
        print(f"Summary: {summary}")
        return jsonify({'summary': summary})
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True)

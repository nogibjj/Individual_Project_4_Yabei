[![CI](https://github.com/nogibjj/Individual_Project_4_Yabei/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Individual_Project_4_Yabei/actions/workflows/cicd.yml)
# Project Title

*App Link:* [Text Summarizer App](https://textsummary.gentlesand-bceecd4f.westus2.azurecontainerapps.io/)
*Place for Video Link:* [Your Video Link Here]

## Overview

This project showcases a text summarization application built using Flask and hosted on Azure App Services. It demonstrates an auto-scaling container approach, ideal for scalable web-hosted applications. The core functionality of this app is based on OpenAI's GPT-3.5 model, which is adept at summarizing texts efficiently. This application is a practical application of Flask and GPT-3.5 technology, aiming to provide concise and meaningful summaries of extensive texts.

## Introduction

The main script for our application is in `main.py`, which orchestrates the interaction with the OpenAI API for text summarization. The Flask framework is used to handle web requests and render templates. The key Flask route `/summarize` is designed to receive text and return its summarized version using GPT-3.5. For the web interface, `idv4.html` is the primary template, located in the templates directory. This file outlines the UI and UX of our application.

### main.py Overview

- **Environment Setup**: `load_dotenv()` to load environment variables.
- **Flask App Initialization**: `Flask(__name__)`.
- **OpenAI API Key Configuration**: Set using `openai.api_key`.
- **Routes**: 
  - `/` for the index route to render the main template.
  - `/summarize` for processing text summarization requests.

### Docker Configuration

The Dockerfile is structured as follows:

1. Base Image: `python:3.11`
2. Working Directory: `/code`
3. Dependencies Installation: `pip3 install --no-cache-dir -r requirements.txt`
4. Copying Source Files
5. Exposing Port: `50505`
6. Entry Point: `gunicorn` with configuration for `main:app`

### Azure Container App

The application is designed to be deployed as a container on Azure, utilizing Azure's capabilities for scalability and reliability.
![e25150d04bebd4e3c5ef763b676c5ce](https://github.com/nogibjj/Individual_Project_4_Yabei/assets/143656459/f9716075-624a-411a-aa1c-55b97f3245cc)
![6a2ac2826cc770bcecef9d534028bd1](https://github.com/nogibjj/Individual_Project_4_Yabei/assets/143656459/91a37725-092a-4d59-ac42-9134cd2978a8)
![3e78b3b408d741bb6981db3ae0e7bad](https://github.com/nogibjj/Individual_Project_4_Yabei/assets/143656459/f07b2571-f9af-4b39-89a1-0bd2e6ad48ac)


## Preparation and Deployment

To get started with the application:

1. **Clone the Repository**: Clone this repo to your local machine.
2. **Install Dependencies**: Use `make install` to install required packages.
3. **API Key Setup**: Acquire an OpenAI API key and save it to the `.env` file.
4. **Local Testing**: Run `main.py` locally to test its functionality.
5. **Docker Image**: Build the Docker image for deployment.
6. **Azure CLI**: Login to the Azure CLI.
7. **Deploy on Azure**: Deploy the application as an Azure web app.
8. **Usage**: Access the application using the provided link to start summarizing texts.




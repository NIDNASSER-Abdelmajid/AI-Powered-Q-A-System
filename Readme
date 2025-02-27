# AI-Powered Q&A System

## Overview

This project is an AI-powered Question & Answer (QA) system that retrieves answers from a set of documents. It utilizes FastAPI for the backend, FAISS for vector search, and a Hugging Face model for natural language processing.

## Features

- FastAPI-based API for handling queries
- Document loading and indexing with FAISS
- Sentence-transformers for embeddings
- Hugging Face model for generating responses
- Simple command-line client for interaction

## Requirements

Before running the project, ensure you have the following installed:

- Python 3.8+
- FastAPI
- Uvicorn
- Requests
- LangChain
- FAISS
- Sentence-Transformers

## Installation

1. Clone the repository:
```bash
git clone https://github.com/NIDNASSER-Abdelmajid/AI-Powered-Q-A-System.git 
cd AI-Powered-Q-A-System
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Add your Hugging Face API token in main.py:
```python
huggingfacehub_api_token = "your_huggingface_api_token"
```

## Usage

### Start the API server

Run the following command to start the FastAPI server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at http://localhost:8000.

### Using the client

Run the client script to interact with the QA system:
```bash
python client.py
```
Type your question in the terminal and receive an AI-generated response. To exit, type quit or exit.

## API Endpoint

### **GET** /ask?query=\<question>
- Description: Retrieves an answer to the provided question.
- Example:
```bash
curl "http://localhost:8000/ask?query=What+does+NEOV+do?"
```
- Response:
```json
{"answer": "......"}
```

## Project Structure
```bash
qa-system/
│── data/                # Directory for storing documents
│── client.py            # Command-line client for interacting with the API
│── main.py              # FastAPI backend for Q&A
│── requirements.txt     # Python dependencies
│── README.md            # Project documentation
```

## Notes

- The document loading function currently processes both PDFs and text files.

- Ensure the document files exist in the `data/` folder before starting the API.


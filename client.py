import requests
import sys

def chat_loop():
    print("Welcome to the QA System! Type 'quit' to exit.")
    print("-" * 50)
    
    while True:
        # Get question from user
        q = input("\nYour question: ").split()
        question = '+'.join(q)
        
        # Check if user wants to quit
        if question.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            sys.exit()
            
        # Send request to API
        try:
            response = requests.get("http://localhost:8000/ask?query="+question)
            
            # Print the answer
            print("\nAnswer:", response.text.strip('"'))  # Remove quotes from response
            
        except requests.exceptions.ConnectionError:
            print("Error: Could not connect to the server. Make sure it's running on http://localhost:8000")
            
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    chat_loop()
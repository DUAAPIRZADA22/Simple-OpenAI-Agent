import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")  

client = OpenAI(
    base_url="https://openrouter.ai/api/v1", 
    api_key=api_key,
)

def ask_agent(question):
    response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",  
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    question = input("Ask something: ")
    answer = ask_agent(question)
    print("\nAnswer:", answer)




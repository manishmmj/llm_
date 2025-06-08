from ollama import Client

def chat_with_llm(prompt):
    client = Client()
    response = client.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    return response['message']['content']
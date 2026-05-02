import ollama

response = ollama.chat(model="llama3.2-vision:latest", messages=[
    {'role': 'user', 'content': 'Explicame que es el arco iris'},
])

print(response['message']['content'])
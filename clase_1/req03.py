import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title" : "Demo de requests con Python",
    "body": "Es una prueba",
    "userId": 1
}

response = requests.post(url, json=data)
print("Status:", response.status_code)
print("JSON:", response.json())
print("URL:", response.url)
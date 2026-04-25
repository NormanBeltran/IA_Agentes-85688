import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
print("Status:", response.status_code)
print("JSON:", response.json())
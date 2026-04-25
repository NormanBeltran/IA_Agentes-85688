import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId" : 1
}

response = requests.get(url, params=params)
print("Status:", response.status_code)
print("JSON:", response.json())
print("URL:", response.url)
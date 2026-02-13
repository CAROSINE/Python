import requests

TOKEN = "your_token"
requests.post("https://api.github.com/gists", 
    json={"files": {"hello.py": {"content": "print('Hi')"}}},
    headers={"Authorization": f"token {TOKEN}"})
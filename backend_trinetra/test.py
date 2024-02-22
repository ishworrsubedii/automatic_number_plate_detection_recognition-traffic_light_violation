"""
Created By: ishwor subedi
Date: 2024-02-22
"""
import requests
from requests.auth import HTTPBasicAuth

url = 'http://127.0.0.1:8000/api/alpr/imagecapture/'
action = 'start'

# Replace 'username' and 'password' with your actual credentials
username = 'ishworhero@gmail.com'
password = 'ishwor'

response = requests.post(url, data={'action': action}, auth=(username, password))
print(response.text)

print(response.status_code)
print(response.json())

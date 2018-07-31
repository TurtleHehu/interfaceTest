import requests

response = requests.get('https://miniapp.youxiake.com/api/channel/cn')
print(response.text)
import requests

# AWS lambda API gateway URL
url = 'https://k99h0xmi68.execute-api.eu-central-1.amazonaws.com/test/predict'

# Local machine URL
# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

data = {'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(url, json=data).json()
print(result)

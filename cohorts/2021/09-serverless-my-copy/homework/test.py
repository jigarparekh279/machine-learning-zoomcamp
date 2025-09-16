import requests

# AWS lambda API gateway URL
url = 'https://5jgelf2n4j.execute-api.eu-central-1.amazonaws.com/test/predict'

# Local machine URL
# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'

input_urls = [
    'https://upload.wikimedia.org/wikipedia/commons/9/9a/Pug_600.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/1/18/Vombatus_ursinus_-Maria_Island_National_Park.jpg'
]

for i, input_url in enumerate(input_urls):
    result = requests.post(url, json={'url': input_url}).json()
    print(f"Image in link {i+1} has probabiltiy of dog = {round(result['prediction'], 2)}")

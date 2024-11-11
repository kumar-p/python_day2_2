import requests

request1 = requests.get('https://api.github.com/events')
print(request1)

request2 = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(request2.text)

# passin a dictionary to the 'params' argument
queryParams = {'key1': 'value1', 'key2': 'value2'}
request3 = requests.get('https://httpbin.org/get', params=queryParams)
print(request3.url)
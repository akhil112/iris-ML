import requests


# response = requests.post('https://reqres.in/api/users?page=2')
# response = response.json()

# print(response['id'])
# print(response['createdAt'])


url = 'http://localhost:8090/rest'
payload = {'sl':6, 'sw':5, 'pl':6,'pw':5}
response = requests.post(url,json=payload)
response = response.json()
print(response['class'])


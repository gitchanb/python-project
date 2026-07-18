import requests

api_key = '96e151e41d0191da9f79db6fdcb4670e'
city = input('enter your city:')

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)
data = response.json()

print(data)
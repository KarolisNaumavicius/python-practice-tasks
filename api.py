import requests

response = requests.get('https://randomuser.me/api')

print(response.status_code)
print(response.json())

# indeksai naudojami, nes imame informacija is maysvo, cia toks idomus pastebejimas, nes jeigu imame is info su masyvu, tai nevieks

gender = response.json()['results'][0]['gender']

title = response.json()['results'][0]['name']['title']

first_name = response.json()['results'][0]['name']['first']

last_name = response.json()['results'][0]['name']['last']

age = response.json()['results'][0]['dob']

city = response.json()['results'][0]['location']['city']

state = response.json()['results'][0]['location']['state']

version = response.json()['info']['version']

print(f'{title} {first_name} {last_name}')
print(f'Age : {age}')
print(f'State : {state}')
print(f'city : {city}')
print(f'Version : {version}')

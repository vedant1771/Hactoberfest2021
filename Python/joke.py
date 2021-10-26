import requests;

URL = "https://v2.jokeapi.dev/joke/Any"

data = requests.get(URL)

json_data = data.json()

if json_data['type'] == 'single':
    print(json_data['joke'])
else:
    print(json_data['setup'])
    print(json_data['delivery'])
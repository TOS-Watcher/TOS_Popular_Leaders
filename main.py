import requests


headers = {
}


response = requests.get('https://website-api.tosgame.com/api/checkup/popularLeaders', headers=headers)
print(response.text)
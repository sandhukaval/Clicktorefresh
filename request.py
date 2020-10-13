import requests

#data=requests.get("https://reqres.in/api/users")
data=requests.get("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")

print(data.text)
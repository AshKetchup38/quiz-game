import requests

parameters = {
    "amount":10, 
    "category":9, 
    "type":"boolean"
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response.json()['results']

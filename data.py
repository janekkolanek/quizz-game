import requests

AMOUNT = 10
TYPE = "boolean"
# CATEGORY = 18

parameters = {
    "amount": AMOUNT,
    "type": TYPE,
    # "category": CATEGORY,
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data =  data["results"]


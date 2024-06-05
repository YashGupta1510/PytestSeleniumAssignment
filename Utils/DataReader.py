import json
import os

file_path = os.path.join(os.path.dirname(__file__), 'data.json')

with open(file_path) as file:
    data = json.load(file)

URL = data["url"]
name = data["name"]
email = data["email"]
password = data["password"]
wrong_email = data["wrong_email"]
gender = data["gender"]
day = data["day"]
month = data["month"]
year = data["year"]
fname = data["fname"]
lname = data["lname"]
company = data["company"]
address1 = data["address1"]
address2 = data["address2"]
country = data["country"]
state = data["state"]
city = data["city"]
zipcode = data["zipcode"]
mobile = data["mobile"]
name_on_card = data["nameOnCard"]
cardNumber = data["cardNumber"]
cvc = data["cvc"]
expiry_month = data["expiryMonth"]
expiry_year = data["expiryYear"]
product = data["product"]
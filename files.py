import requests

try:
    text = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
    data = text.json()
    with open("test.txt", "w") as f:
        f.write (f"PLN: {data['rates']['PLN']} \n")
        f.write(f"EUR: {data['rates']['EUR']} \n")
        f.write(f"ALL: {data['rates']['ALL']} \n")

except Exception as e:
    with open("error.txt", "w") as log:
        log.write(str(e))
from weather import data
from datetime import datetime

def clean_data(data):
    for info in data:
        cleaned = {}
        cleaned["country"] = info["country"]
        cleaned["temp"] = int(info["temp"])
        cleaned["date"] = datetime.strptime(info["date"], "%m/%d/%Y")
        cleaned["wind_speed"] = float(info["wind_speed"].replace("mph",""))
        yield cleaned

print(list(clean_data(data)))

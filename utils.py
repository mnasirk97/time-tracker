import json
from datetime import datetime

def load_data(username):
    try:
        with open("database.json", "r") as file:
            all_data = json.load(file)
        return all_data.get(username, {})
    except:
        return {}

def save_data(username, data):
    try:
        with open("database.json", "r") as file:
            all_data = json.load(file)
    except:
        all_data = {}
    all_data[username] = data
    with open("database.json", "w") as file:
        json.dump(all_data, file, indent=4)

def calculate_total_hours(entries):
    total = 0
    for entry in entries:
        t_in = datetime.strptime(entry["in"], "%H:%M:%S")
        t_out = datetime.strptime(entry["out"], "%H:%M:%S")
        worked = (t_out - t_in).seconds / 3600
        total += worked
    return round(total, 2)

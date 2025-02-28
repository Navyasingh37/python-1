import json

# File to store birthdays
BIRTHDAY_FILE = "birthdays.json"

# Load existing birthdays from file
def load_birthdays():
    try:
        with open(BIRTHDAY_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save birthdays to file
def save_birthdays(birthdays):
    with open(BIRTHDAY_FILE, "w") as file:
        json.dump(birthdays, file, indent=4)

# Add a new birthday
def add_birthday(name, date):
    birthdays = load_birthdays()
    birthdays[name] = date
    save_birthdays(birthdays)
    print(f"Birthday for {name} added successfully!")

# View all stored birthdays
def view_birthdays():
    birthdays = load_birthdays()
    if birthdays:
        print("\nStored Birthdays:")
        for name, date in birthdays.items():
   
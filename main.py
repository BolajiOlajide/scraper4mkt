"""
Lots of stuff going on here. Not efficient just hacking this to work.
"""
from secrets import token_hex
import time

import csv
from requests import get as rget


__CSVS__ = [
    'egypt.csv',
    'ghana.csv'
]
# ensure you specify github token here
TOKEN = ''

def get_gh_data(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    data = rget(url, headers=headers)
    return data.json()


def search_for_email(events):
    for event in events:
        if (event.get("type", "") == "PushEvent"):
            commits = event.get("payload", {}).get("commits", [])
            if len(commits) > 0:
                email = commits[0].get("author", {}).get("email", "")
                if email:
                    return email
    return None


def clean_csv_data(FILENAME):
    result = []
    with open(FILENAME, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spamreader:
            full_name = row[1]
            gh_handle = row[2]
            email = row[-1]
            if full_name == "name":
                continue
            if not email:
                events = get_gh_data(gh_handle)
                email = search_for_email(events) or ""
                time.sleep(1000)
            result.append({
                "full_name": full_name,
                "handle": gh_handle,
                "email": email
            })
    return result


def generate_output_name(FILENAME):
    uniq_token = token_hex(4)
    filename, extension = FILENAME.split('.')
    filename = f"{filename}_{uniq_token}"
    return f"output/{filename}.{extension}"


def write_to_csv(filename, data):
    new_file_name = generate_output_name(filename)
    with open(new_file_name, 'w', newline='\n') as csvfile:
        fieldnames = ['full_name', 'handle', 'email']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return True


sample = [
    {
        "full_name": "John Doe",
        "handle": "jdoe",
        "email": "j@doe.com"
    },
    {
        "full_name": "Vanessa Carlton",
        "handle": "vcarl",
        "email": "v.carlton@gmail.com"
    }
]


# if __name__ == "__main__":
#     for file in __CSVS__:

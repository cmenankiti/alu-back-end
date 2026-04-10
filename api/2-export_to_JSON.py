#!/usr/bin/python3
"""
Extends Task 0 to export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    data = {user_id: []}
    for t in todos:
        data[user_id].append({
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        })

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(data, jsonfile)

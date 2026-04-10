#!/usr/bin/python3
"""
Exports all tasks from all employees to a JSON file.
"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    
    all_data = {}
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")
        todos = requests.get(url + "todos", params={"userId": user_id}).json()
        
        all_data[user_id] = [
            {
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed")
            } for t in todos
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(all_data, jsonfile)

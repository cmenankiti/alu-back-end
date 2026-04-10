#!/usr/bin/env python3
"""Export employee TODOs to JSON"""
import requests
import sys
import json

if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    username = user.get("username")

    data = {
        user_id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in todos
        ]
    }

    with open(f"{user_id}.json", "w") as f:
        json.dump(data, f)

#!/usr/bin/env python3
"""Export all employees TODOs to JSON"""
import requests
import json

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    data = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        user_tasks = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in todos if task.get("userId") == user.get("id")
        ]

        data[user_id] = user_tasks

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)

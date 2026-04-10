#!/usr/bin/env python3
"""Export employee TODOs to CSV"""
import requests
import sys
import csv

if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    username = user.get("username")

    with open(f"{user_id}.csv", mode="w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

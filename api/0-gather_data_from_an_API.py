#!/usr/bin/env python3
"""Fetch and display employee TODO progress"""
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user = requests.get(user_url).json()
    todos = requests.get(todo_url).json()

    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)

    print(f"Employee {user.get('name')} is done with tasks({len(done_tasks)}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")

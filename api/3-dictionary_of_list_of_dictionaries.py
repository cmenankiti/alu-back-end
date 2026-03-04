#!/usr/bin/python3
"""
Exports all tasks from all employees into a single JSON file.
Structure: { "USER_ID": [ {"username": "...", "task": "...", "completed": ...}, ... ]}
"""
import json
import requests


def export_all_to_json():
    """Fetches all users and their todos, then exports to JSON."""
    base_url = "https://jsonplaceholder.typicode.com"

    # 1. Fetch all users to get their IDs and Usernames
    users_res = requests.get("{}/users".format(base_url))
    users = users_res.json()

    # 2. Prepare the main dictionary to hold everything
    all_data = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # 3. Fetch the TODO list for this specific user
        todo_res = requests.get("{}/todos".format(base_url),
                                params={'userId': user_id})
        tasks = todo_res.json()

        # 4. Build the list of task dictionaries for this user
        user_tasks = []
        for task in tasks:
            task_info = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            user_tasks.append(task_info)

        # 5. Add this user's list to our main dictionary
        all_data[user_id] = user_tasks

    # 6. Write the final big dictionary to the file
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_data, json_file)


if __name__ == "__main__":
    export_all_to_json()

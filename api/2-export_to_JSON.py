#!/usr/bin/python3
"""
Extends Task #0 to export data in JSON format.
Format: { "USER_ID": [{"task": "TITLE", "completed": STATUS, "username": "NAME"}, ...]}
"""
import json
import requests
import sys


def export_to_json():
    """Fetches API data and exports it to a JSON file."""
    if len(sys.argv) < 2:
        return

    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # 1. Get User info (we need the 'username' field specifically this time)
    user_res = requests.get("{}/users/{}".format(base_url, user_id))
    user_data = user_res.json()
    username = user_data.get("username")

    # 2. Get all TODO tasks for this user
    todo_res = requests.get("{}/todos".format(base_url),
                            params={'userId': user_id})
    tasks = todo_res.json()

    # 3. Structure the data for JSON
    # We create a list of dictionaries as required by the format
    task_list = []
    for task in tasks:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        task_list.append(task_dict)

    # Wrap the list in a dictionary with the User ID as the key
    final_data = {user_id: task_list}

    # 4. Write to the file (USER_ID.json)
    file_name = "{}.json".format(user_id)
    with open(file_name, 'w') as json_file:
        json.dump(final_data, json_file)


if __name__ == "__main__":
    export_to_json()


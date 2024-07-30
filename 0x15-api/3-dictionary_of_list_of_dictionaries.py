#!/usr/bin/python3
"""
Gets data from an API and returns information
for all employees.
Exports the data in JSON format.
"""
import json
import requests


def get_all_users():
    """gets all users info

    Returns:
        _type_: _description_
    """

    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code != 200:
        return None
    return response.json()


def get_all_todos():
    """gets todo data

    Returns:
        _type_: _description_
    """

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if response.status_code != 200:
        return None
    return response.json()


def export_to_json(users, todos):
    """exports all users data to a json file"""

    data = {}
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [task for task in todos if task['userId'] == user_id]
        data[user_id] = [{"username": username, "task": task["title"],
                         "completed": task["completed"]}
                         for task in user_tasks]

    filename = "todo_all_employees.json"
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)


def main():
    users = get_all_users()
    if users is None:
        print("Failed to retrieve user data.")

    todos = get_all_todos()
    if todos is None:
        print("Failed to retrieve TODO data.")

    export_to_json(users, todos)


if __name__ == "__main__":
    main()

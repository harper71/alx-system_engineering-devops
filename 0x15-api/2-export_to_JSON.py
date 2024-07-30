#!/usr/bin/python3
"""
Gets data from an API and returns information
for the specified employee's ID.
Exports the data in JSON format.
"""
import json
import requests
import sys


def get_user_info(employee_id):
    """gets employes infomations"""

    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if response.status_code != 200:
        return None
    return response.json()


def get_todo_data(employee_id):
    """gets to do data"""

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if response.status_code != 200:
        return None
    todo_data = response.json()
    return [task for task in todo_data if task['userId'] == employee_id]


def export_to_json(employee_id, employee_name, todo_data):
    """exports data to a json file"""

    filename = f"{employee_id}.json"
    tasks = [{"task": task["title"], "completed": task["completed"],
              "username": employee_name} for task in todo_data]
    data = {str(employee_id): tasks}

    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, ensure_ascii=False)


def main():
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    user_info = get_user_info(employee_id)
    if user_info is None:
        print(f"No employee found with ID {employee_id}.")
        sys.exit(1)

    employee_name = user_info.get('username')
    todo_data = get_todo_data(employee_id)
    if todo_data is None:
        print("Failed to retrieve TODO data.")
        sys.exit(1)

    export_to_json(employee_id, employee_name, todo_data)


if __name__ == "__main__":
    main()

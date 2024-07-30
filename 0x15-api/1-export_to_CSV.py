#!/usr/bin/python3
"""
Gets data from an API and returns information
for the specified employee's ID.
Exports the data in CSV format.
"""
import csv
import requests
import sys


def get_user_info(employee_id):
    """gets employee info

    Args:
        employee_id (_type_): _description_

    Returns:
        _type_: _description_
    """

    response = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    if response.status_code != 200:
        return None
    return response.json()


def get_todo_data(employee_id):
    """gets data of todos"""

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    if response.status_code != 200:
        return None
    todo_data = response.json()
    return [task for task in todo_data if task['userId'] == employee_id]


def export_to_csv(employee_id, employee_name, todo_data):
    """exports data to a csv file"""

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_data:
            writer.writerow([employee_id, employee_name,
                            task['completed'], task['title']])


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

    export_to_csv(employee_id, employee_name, todo_data)


if __name__ == "__main__":
    main()

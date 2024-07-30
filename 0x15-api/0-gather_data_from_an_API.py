#!/usr/bin/python3
"""
Gets data from an API and returns information
for the specified employee's ID.
"""
import requests
import sys


def get_user_info(employee_id):
    """get user name

    Args:
        employee_id (_type_): _description_

    Returns:
        _type_: _description_
    """

    data = requests.get("https://jsonplaceholder.typicode.com/users")
    employee_data = data.json()

    for item in employee_data:
        if item['id'] == employee_id:
            return item['name']
    return None


def todos_tasks(employee_id):
    """get the todo tasks

    Args:
        employee_id (int): system arguments

    Returns:
        dict: task
    """

    todo_list = requests.get("https://jsonplaceholder.typicode.com/todos")
    todo_data = todo_list.json()

    return [task for task in todo_data if task['userId'] == employee_id]


def main():
    if len(sys.argv) != 2:
        print("Usage: ./script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_name = get_user_info(employee_id)
    if employee_name is None:
        print(f"No employee found with ID {employee_id}.")
        sys.exit(1)

    total_tasks = todos_tasks(employee_id)
    completed_tasks = [completed for completed in total_tasks
                       if completed['completed']]

    print("Employee {} is done with tasks ({}/{}).".
          format(employee_name, len(total_tasks), len(completed_tasks)))

    for task in completed_tasks:
        print(f"\t {task['title']}")


if __name__ == "__main__":
    main()

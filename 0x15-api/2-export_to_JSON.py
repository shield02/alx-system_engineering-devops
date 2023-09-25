#!/usr/bin/python3
"""
Use fake JSON placeholder api to query data about an employee
to test for employeeID, to get info on TODO list progress
and export to JSON
"""

from json import dump
from requests import get
from sys import argv


if __name__ == "__main__":
    todo_url = f"https://jsonplaceholder.typicode.com/user/{argv[1]}/todos"
    name_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_list = []
    for todo in todo_result:
        todo_dict = {}
        todo_dict.update({"task": todo.get("title"), "completed": todo.get(
            "completed"), "username": name_result.get("username")})
        todo_list.append(todo_dict)

    with open("{}.json".format(argv[1]), 'w') as f:
        dump({argv[1]: todo_list}, f)

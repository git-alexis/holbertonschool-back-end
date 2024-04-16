#!/usr/bin/python3

from sys import argv, exit
from requests import get
import json

if __name__ == "__main__":

    if len(argv) < 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    user_id = argv[1]
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = get(url_1).json()
    url_2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    todos = get(url_2).json()

    list_tasks = []
    for task in todos:
        task_dict = {"task": task.get("title"),
                     "completed": task.get("completed"),
                     "username": user.get("username")}
        list_tasks.append(task_dict)

    with open('{}.json'.format(user_id), 'w') as jsonfile:
        """Save the object list_tasks in a JSON file """
        json.dump({user_id: list_tasks}, jsonfile)

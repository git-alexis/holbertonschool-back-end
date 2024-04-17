#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    user_id = sys.argv[1]
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(url_1).json()
    url_2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    todos = requests.get(url_2).json()

    completed = []
    for task in todos:
        if task.get("completed") is True:
            completed.append(task)

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for task in completed:
        print("\t {}".format(task.get("title")))

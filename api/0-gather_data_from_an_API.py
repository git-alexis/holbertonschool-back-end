#!/usr/bin/python3
""" Gather data from an API """

from sys import argv, exit
from requests import get

if __name__ == "__main__":

    """ Check if the user provided an employee ID """
    if len(argv) < 2:
        print("Usage: {} employee_id".format(argv[0]))
        exit(1)

    user_id = argv[1]

    """ Get the user data """
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = get(url_1).json()

    """ Get the user's tasks """
    url_2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    todos = get(url_2).json()

    """ Count the number of completed tasks """
    completed = []
    for task in todos:
        if task.get("completed") is True:
            completed.append(task)

    """ Print the user's tasks """
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    """ Print the completed tasks """
    for task in completed:
        print("\t {}".format(task.get("title")))

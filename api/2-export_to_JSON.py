#!/usr/bin/python3
""" Export data in the JSON format """

import json
import requests
import sys

if __name__ == "__main__":

    """ Check if the user provided an employee ID """
    if len(sys.argv) < 2:
        print("Usage: {} employee_id".format(sys.argv[0]))
        exit(1)

    user_id = sys.argv[1]

    """ Get the user data """
    url_1 = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(url_1).json()

    """ Get the user's tasks """
    url_2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        user_id)
    todos = requests.get(url_2).json()

    list_tasks = []
    """ Create a list of dictionaries with the user's tasks """
    for task in todos:
        task_dict = {"task": task.get("title"),
                     "completed": task.get("completed"),
                     "username": user.get("username")}
        list_tasks.append(task_dict)

    """ Save the user's tasks in a JSON file """
    with open('{}.json'.format(user_id), 'w') as jsonfile:
        """ Save the object list_tasks in a JSON file """
        json.dump({user_id: list_tasks}, jsonfile)

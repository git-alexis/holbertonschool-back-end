#!/usr/bin/python3

import sys
import requests
import json

if __name__ == "__main__":

    all_data = {}
    url_1 = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url_1).json()

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        url_2 = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
            user_id)
        todos = requests.get(url_2).json()

        user_data = []
        for task in todos:
            task_data = {"username": username,
                         "task": task.get("title"),
                         "completed": task.get("completed")}
            user_data.append(task_data)

        all_data[user_id] = user_data

    with open("todo_all_employees.json", "w") as json_file:
        """Save the object all_data in a JSON file """
        json.dump(all_data, json_file)

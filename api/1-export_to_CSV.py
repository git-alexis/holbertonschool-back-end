#!/usr/bin/python3

from sys import argv, exit
import csv
from requests import get

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

    with open("{}.csv".format(user_id), "w") as csvfile:
        """Creates a CSV object to format the CSV file"""
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            """Writes line with the imformation of task to the CSV file """
            writer.writerow([user_id, user.get("username"),
                             task.get("completed"), task.get("title")])

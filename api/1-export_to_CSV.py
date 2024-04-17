#!/usr/bin/python3
""" Export data in the CSV format """

import csv
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

    """ Save the user's tasks in a CSV file """
    with open("{}.csv".format(user_id), "w") as csvfile:
        """ Creates a CSV object to format the CSV file """
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            """ Writes line with the imformation of task to the CSV file
                  """
            writer.writerow([user_id, user.get("username"),
                             task.get("completed"), task.get("title")])

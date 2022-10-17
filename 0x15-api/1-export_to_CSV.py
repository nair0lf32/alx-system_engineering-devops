#!/usr/bin/python3
"""
extend 0-gather_data_from_an_API.py to export data in the CSV format
"""

from csv import DictWriter, QUOTE_ALL
from requests import get
import sys


if __name__ == "__main__":
    req_url = 'https://jsonplaceholder.typicode.com'
    t_endpoint = req_url + "/user/{}/todos".format(sys.argv[1])
    n_endpoint = req_url + "/users/{}".format(sys.argv[1])
    todo = get(t_endpoint).json()
    names = get(n_endpoint).json()

    tasks = []
    for task in todo:
        t_dict = {}
        t_dict.update({"user_ID": sys.argv[1], "username": names.get(
            "username"), "completed": task.get("completed"),
                          "task": task.get("title")})
        tasks.append(t_dict)
    with open("{}.csv".format(sys.argv[1]), 'w', newline='') as f:
        header = ["user_ID", "username", "completed", "task"]
        writer = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
        writer.writerows(tasks)

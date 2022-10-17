#!/usr/bin/python3
"""
extend 0-gather_data_from_an_API.py to export data in the JSON format
"""

from requests import get
import json
import sys


if __name__ == "__main__":
    req_url = 'https://jsonplaceholder.typicode.com'
    u_endpoint = req_url + "/users/"
    users = get(u_endpoint).json()

    data_dict = {}
    for user in users:
        tasks = []
        t_endpoint = req_url + "/user/{}/todos".format(user.get("id"))
        n_endpoint = req_url + "/users/{}".format(user.get("id"))
        todo = get(t_endpoint).json()
        names = get(n_endpoint).json()

        for task in todo:
            t_dict = {}
            t_dict.update({"username": names.get("username"),
                              "task": task.get("title"),
                              "completed": task.get("completed")})
            tasks.append(t_dict)

        data_dict.update({user.get("id"): tasks})

    with open("todo_all_employees.json", 'w') as f:
        json.dump(data_dict, f)

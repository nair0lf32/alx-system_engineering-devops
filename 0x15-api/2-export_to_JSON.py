#!/usr/bin/python3
"""
extend 0-gather_data_from_an_API.py to export data in the JSON format
"""

from requests import get
import sys
import json


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
    with open("{}.json".format(sys.argv[1]), 'w') as f:
        json.dump({sys.argv[1]: tasks}, f)

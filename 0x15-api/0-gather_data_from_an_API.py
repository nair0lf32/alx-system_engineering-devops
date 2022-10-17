#!/usr/bin/python3
"""
using the REST API returns information about TODO list progress for a given employee ID
"""

from requests import get
import sys

if __name__ == '__main__':
    req_url = 'https://jsonplaceholder.typicode.com'
    t_endpoint = req_url + "/user/{}/todos".format(sys.argv[1])
    n_endpoint = req_url + "/users/{}".format(sys.argv[1])
    todo = get(t_endpoint).json()
    names = get(n_endpoint).json()
    tasks = len(todo)
    completed = len([task for task in todo
                         if task.get("completed")])
    name = names.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, tasks))
    for task in todo:
        if (task.get("completed")):
            print("\t {}".format(task.get("title")))

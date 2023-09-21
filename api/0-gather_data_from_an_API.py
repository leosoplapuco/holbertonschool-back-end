#!/usr/bin/python3
""" Getting data from an API """
import requests
import sys


try:
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos", params={"userId": sys.argv[1]}).json()
except Exception as e:
    print(e)
    sys.exit(1)

completed = [t.get("title") for t in todos if t.get("completed") is True]

print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(todos)))
for c in completed:
    print("\t {}".format(c))

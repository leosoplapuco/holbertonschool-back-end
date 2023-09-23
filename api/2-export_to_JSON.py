#!/usr/bin/python3
""" Gettinf data from and API """

if __name__ == '__main__':

    import json
    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/"
    param = argv[1]
    user = requests.get(url + "users?id={}".format(param))
    user = user.json()
    name = user[0]["username"]
    todos = requests.get(url + "todos?userId={}".format(param))
    todos = todos.json()
    output = {}
    output[param] = []

    for todo in todos:
        output[param].append({
            "task": todo["title"],
            "completed": todo["completed"],
            "username": name})

    with open("{}.json".format(param), 'w') as result_file:
        json.dump(output, result_file)

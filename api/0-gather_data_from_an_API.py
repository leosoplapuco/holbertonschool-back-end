#!/usr/bin/python3
"""
To retrieve data from an API
"""

if __name__ == '__main__':

    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/"
    param = argv[1]
    user = requests.get(url + "users?id={}".format(param))
    # Transforms JSON data in Python objects
    user = user.json()
    # Gets the name from the user object
    name = user[0]["name"]
    todos = requests.get(url + "todos?userId={}".format(param))
    # Transforms JSON data in Python objects
    todos = todos.json()
    done = requests.get(url + "todos?userId={}&completed=true".format(param))
    # Transforms JSON data in Python objects
    done = done.json()
    done_list = []

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(done), len(todos)))

    # n is a dictionary and title is the key
    for n in done:
        done_list.append("\t {}".format(n["title"]))
    for task in done_list:
        print(task)

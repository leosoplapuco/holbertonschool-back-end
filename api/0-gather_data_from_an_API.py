#!/usr/bin/python3
""" Getting data from an API """

if __name__ == '__main__':

    import requests
    from sys import argv

    url = "https://jsonplaceholder.typicode.com/"
    param = argv[1]
    user = requests.get(url + "users?id={}".format(param))
    user = user.json()
    name = user[0]["name"]
    todos = requests.get(url + "todos?userId={}".format(param))
    todos = todos.json()
    done = requests.get(url + "todos?userId={}&completed=true".format(param))
    done = done.json()
    done_list = []

    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(done), len(todos)))

    for n in done:
        done_list.append("\t {}".format(n["title"]))
    for task in done_list:
        print(task)

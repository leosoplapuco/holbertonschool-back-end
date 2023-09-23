#!/usr/bin/python3
""" Gettinf data from and API """

if __name__ == '__main__':

    import csv
    import requests
    from sys import argv

    param = argv[1]
    csv_path = "{}.csv".format(param)
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users?id={}".format(param))
    user = user.json()
    name = user[0]["username"]
    todos = requests.get(url + "todos?userId={}".format(param))
    todos = todos.json()

    with open(csv_path, mode="w", newline="") as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)

        for todo in todos:
            writer.writerow([param, name, todo["completed"], todo["title"]])

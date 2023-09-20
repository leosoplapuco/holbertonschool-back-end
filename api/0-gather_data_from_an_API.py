#!/usr/bin/python3
""" Getting data from an API """
import requests
from sys import argv

def todo(userid):
    user_info = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(userid)).json()
    user_name = user_info.get('name')
    tasks = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'.format(userid)).json()
    tasks_done = [dic.get('title') for dic in tasks if dic.get('completed')]
    
    if user_name and tasks:
        num_completed_tasks = len(tasks_done)
        total_tasks = len(tasks)
        print("Employee {} is done with tasks ({}/{}):".format(user_name, num_completed_tasks, total_tasks))
        for task_title in tasks_done:
            print('\t{}'.format(task_title))


if __name__ == "__main__":
    if len(argv) == 2:
        todo(int(argv[1]))

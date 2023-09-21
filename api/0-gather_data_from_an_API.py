#!/usr/bin/python3
"""
This module makes a request to an API to extract specific data
"""
import requests
from sys import argv


url = 'https://jsonplaceholder.typicode.com'

# Acceso a la API
response = requests.get(url)


def make_request():
    # Hacer las solicitudes para obtener los datos de la API
    response_tasks = requests.get(f"{url}/todos?userId={argv[1]}")
    response_user = requests.get(f"{url}/users/{argv[1]}")

    # Convertir de JSON a estrucutura de datos
    all_task = response_tasks.json()
    username = response_user.json().get('name')

    # Lista de tareas completadas por el usuario x
    completed_tasks = []
    for task in all_task:
        if task.get('completed'):
            completed_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):".format(
        username,
        len(completed_tasks),
        len(all_task))
        )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == '__main__':
    make_request()

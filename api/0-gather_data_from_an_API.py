#!/usr/bin/python3
""" Geeting data from an API """
import requests

API_ENDPOINT = "https://example.com/api/todos/{employee_id}"

def get_employee_todo_list_progress(employee_id):
   response = requests.get(API_ENDPOINT.format(employee_id=employee_id))
   
   if response.status_code != 200:
     raise Exception("Failed to get employee TODO list progress: {}".format(response.status_code))
   
   json_response = response.json()
   
   number_of_done_tasks = 0
   total_number_of_tasks = 0
   
   for task in json_response["tasks"]:
    if task["status"] == "done":
      number_of_done_tasks += 1
    total_number_of_tasks += 1
    
    return{
    "employee_name": json_response["employee_name"],
    "number_of_done_tasks": number_of_done_tasks,
    "total_number_of_tasks": total_number_of_tasks,
    }


def main():
  employee_id = int(input("Enter the employee ID: "))
  employee_todo_list_progress = get_employee_todo_list_progress(employee_id)
  
  print("Employee {} is done with tasks({}/{}):".format(
      employee_todo_list_progress["employee_name"],
      employee_todo_list_progress["number_of_done_tasks"],
      employee_todo_list_progress["total_number_of_tasks"],
      ))
  
  for task in employee_todo_list_progress["completed_tasks"]:
    print("\t{}".format(task))


if __name__ == "__main__":
  main()

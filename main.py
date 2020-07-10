from task import *
import json
from readandwrite import write_to_json_file

file_name = 'task_repo.txt'

proceed = True
while proceed:
    task_name = input("What is tasks name?")
    task_description = input("Describe your task")
    write_to_json_file(task_name, task_description, file_name)

    keepGoing = input("Would you like to add another task? Enter [1] Yes or [2] No")
    if keepGoing != "1":
        proceed = False





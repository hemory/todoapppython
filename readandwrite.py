import json


def write_to_json_file(task_name, task_description, path):
    # write the task to a file
    # complete_task = task_name + "," + task_description

    complete_task = f"{task_name},{task_description} \n"

    with open(path, 'a') as file_object:
        file_object.write(complete_task)

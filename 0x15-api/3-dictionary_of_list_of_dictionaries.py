#!/usr/bin/python3
'''
    Dictionary of list of dictionaries
'''
import json
import requests
import sys


if __name__ == "__main__":
    def todos_list(res, inputs=None):
        url = 'https://jsonplaceholder.typicode.com/'
        url += res
        if inputs:
            url += ('?' + inputs[0] + '=' + inputs[1])
        get_data = requests.get(url)
        the_data = get_data.json()
        return the_data
    export = {}
    users = todos_list('users')
    for user in users:
        user_id = user['id']
        export.update({user_id: []})
        user_tasks = todos_list('todos', ('userId', str(user_id)))
        for task in user_tasks:
            export[user_id].append({'username': user['username'],
                                    'task': task['title'],
                                    'completed': task['completed']})

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as file:
        json.dump(export, file)
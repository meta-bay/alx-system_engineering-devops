#!/usr/bin/python3
'''
    Export to JSON
'''
import json
import requests
import sys


if __name__ == "__main__":
    def todos_list(res, inputs):
        url = 'https://jsonplaceholder.typicode.com/'
        url += res
        if input:
            url += ('?' + inputs[0] + '=' + inputs[1])
        get_data = requests.get(url)
        the_data = get_data.json()
        return the_data
    users = todos_list('users', ('id', sys.argv[1]))
    tasks = todos_list('todos', ('userId', sys.argv[1]))
    finished_tasks = [task for task in tasks if task['completed']]
    user_id = users[0]['id']
    export = {user_id: []}
    for task in tasks:
        export[user_id].append({'task': task['title'],
                                'completed': task['completed'],
                                'username': users[0]['username']})

    filename = sys.argv[1] + '.json'
    with open(filename, mode='w') as file:
        json.dump(export, file)

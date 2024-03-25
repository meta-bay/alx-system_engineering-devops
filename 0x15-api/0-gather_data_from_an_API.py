#!/usr/bin/python3
'''
    Gather data from an API
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
    print('Employee {} is done with tasks({}/{}):'.format(users[0]['name'],
                                                          len(finished_tasks),
                                                          len(tasks)))
    for task in finished_tasks:
        print('\t {}'.format(task['title']))

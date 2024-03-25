#!/usr/bin/python3
'''
    Export to CSV
'''
import csv
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

    the_filename = sys.argv[1] + '.csv'
    with open(the_filename, mode='w') as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([users[0]['id'],
                             users[0]['username'],
                             task['completed'],
                             task['title']])

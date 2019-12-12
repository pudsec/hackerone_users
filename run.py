import csv
import json
import requests
import string

with open('users.csv', 'w') as f:
    c = csv.writer(f, delimiter=',', lineterminator='\n')
    for s in string.digits + string.ascii_lowercase:
        s = requests.get(
            'https://hackerone.com/sitemap?first=' + s,
            headers={
                'Accept': 'application/json',
                'X-Requested-With': 'XMLHttpRequest',
            },
        ).json()['users']
        for u in s:
            c.writerow([u['name'], u['username'], 'https://hackerone.com/' + u['username']])

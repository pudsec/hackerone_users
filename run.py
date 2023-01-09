import csv
import json
import requests
import string

with open('users.csv', 'w') as f:
    c = csv.writer(f, delimiter=',', lineterminator='\n')
    for s in string.digits + string.ascii_lowercase:
        r = requests.get(
            'https://hackerone.com/sitemap?first=' + s,
            headers={
                'Accept': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
                'X-Requested-With': 'XMLHttpRequest',
            },
        ).json()['users']
        for u in r:
            c.writerow([u['name'], u['username'], 'https://hackerone.com/' + u['username']])

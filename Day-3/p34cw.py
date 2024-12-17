import requests

pr = requests.get('https://www.python.org')
pr.headers['Conetent-Type']

pr.page = pr.text


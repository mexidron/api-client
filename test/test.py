import requests


url = 'http://192.168.3.101:8000'
multiple_files = [('file', ('README.md', open('README.md', 'rb'), 'text/plain'))]
r = requests.post(url, files=multiple_files)
print r.text

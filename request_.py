import requests
import re

domain = 'http://127.0.0.1'
url = 'https://hey06.cjkypo.com/20211214/81djmKz5/1000kb/hls/uFSyQer7.ts'
arr = re.split('//|/', url)
url = f'{domain}/x/{"/".join(arr[2:])}'
print(url)
response = requests.get(url)
print()
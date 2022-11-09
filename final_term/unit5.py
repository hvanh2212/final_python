import requests
import json
import ast
request = requests.get('https://cataas.com/api/cats?')
link_json = request.json()

link = json.dumps(link_json)

res = ast.literal_eval(link)

tags = []
for cat_pics in res:
    for i in list(cat_pics.values())[2]:
        tags.append(i.strip())
tags = set(tags)
print(tags)


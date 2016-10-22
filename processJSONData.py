# historyStorage_1477123900862362.json

import json

with open('historyStorage_1477123900862362.json') as data_file:    
    searches = json.loads(data_file.read())

for file in files
for search in searches:
    url = search['url']
    lastVisitTime = search['lastVisitTime']
    title = search['title']
    typedCount = search['typedCount']
    visitCount = search['visitCount']

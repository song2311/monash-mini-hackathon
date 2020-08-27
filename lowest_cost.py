import json

with open('team.json') as f:
  team = json.load(f)

for line in team:
    print(line['Skills'])
    
f.close()

with open('tasks.json') as f:
  tasks = json.load(f)


for line in tasks:
    print(line['Skills'])
    
f.close()

list_ = [
    {'id':3, 'name': 'denus'},
    {'id':2, 'name': 'olya'},
    {'id':2, 'name': 'Petro'},
    {'id':89, 'name': 'olya'},
]

def printList(data):
    for i in range(len(data)):
        print(i+1,data[i])

printList(list_)

### sort
# list_.sort(key = lambda id:id['id'])  ### change old list and return them
# sorted(list_, key = lambda id:id['id']) ### new list return
# sorted(list_, key = lambda name: str.lower(name['name']))
# print(f'\n{"-"*40}\n')
# printList(list_)

### filter

import json

print(f'\n{"-"*40}\n')
list_2 = list(filter(lambda item:item['id'] == 1, list_))
printList(list_2)
list_2 = list(filter(lambda item:item['name'] == 'sasha', list_))
printList(list_2)
print(f'\n{"-"*40}\n')
# str.lower str.uper !!!

list_3 = list(map(lambda item:{'id':item['id']+2,'name':item['name']},list_))
printList(list_3)


# with open('example.json','w') as file:
#     file.write(json.dumps(list_))       Write

# with open('example.json','r') as file:
#     res = file.read()
#     print(json.loads(res))              Read




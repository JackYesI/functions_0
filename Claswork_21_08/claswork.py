# import json
# student_1 = {'name':'Valeria','lastname':'Dokukina','rating':11.9, 'group':'F31', 'birthdate':'20.01.05', 'email':"ewcewce@hmail.com", 'phone':'+380687296894' }

# obj = ''
# with open('file/dict.txt', 'r') as file:
#     obj = file.read()
# print(obj)

# print('Print student :: ', student_1)
# student_1['visited'] = 96
# print('Print student :: ', student_1)

# del student_1['phone']

# student_1.popitem()
# student_1.pop('email')

# for key in student_1.keys():
#     print(f'[{key}] - {student_1[key]}')

# for value in student_1.values():
#     print(value)
# print()

# for key,value in student_1.items():
#     print(f'{key} --> {value}')

######## Serialization
#import json

# line = json.dumps(student_1)
# print(line)
# print(type(line))

# obj = json.loads(line)
# print(obj)
# print(type(obj))
# print(obj['name'])

import requests
import json

# result = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5')
# obj = json.loads(result.content)

# for item in obj:
#     for key,value in item.items():
#         print(f'{key} : {value}')

##################### img
# url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pxfuel.com%2Fen%2Fquery%3Fq%3Dwiter&psig=AOvVaw3Lcva-kaRN6dtvJselB-cT&ust=1692708909865000&source=images&cd=vfe&opi=89978449&ved=0CA4QjRxqFwoTCODc_5nm7YADFQAAAAAdAAAAABAI'

# img = requests.get(url)
# with open('file/1.jpg', 'wb') as file:
#     file.write(img.content)
################img

url = 'https://pixabay.com/api/?key=14304821-db198647e0592cf253911c94a&image_type=vector'
images = requests.get(url).json()

images = images['hits']
counter = 1
for img in images:
    pict = requests.get(img['webformatURL'])
    with open(f'file/img/{counter}.jpg', 'wb') as file:
        file.write(pict.content)
    counter += 1










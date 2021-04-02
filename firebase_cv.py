#from firebase import firebase
 
#firebase = firebase.FirebaseApplication('https://fir-real-time-database-96756-default-rtdb.firebaseio.com/', None)
#data =  { 'Name': 'Papawarin',
 #         'Surname': 'Rodpai',
  #        'Gender': 'F',
   #       'Image' : 'oii.jpg'
#}
#result = firebase.post('/person',data)
#print(result)
import json
import requests
 
from firebase import firebase
 
firebase = firebase.FirebaseApplication('https://fir-real-time-database-96756-default-rtdb.firebaseio.com/', None)
result = firebase.get('/person/', '')
for person in result:
    jsn = requests.get('https://fir-real-time-database-96756-default-rtdb.firebaseio.com/person.json')
    data = jsn.json()
    print(data[person]['Name'])
    print(data[person]['Surname'])
    print(data[person]['Gender'])
    print(data[person]['Image'])

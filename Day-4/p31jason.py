import json

print(json.dumps({'name': 'Arsh','Age':'23'}))#---------write json through pytgon
print(json.dumps(['name : Arsh','Age : 23']))
print(json.dumps(('name Arsh','Age: 23')))

file = open('test.json','r')#-----> read json from from python

pd = json.load(file)
file.close()
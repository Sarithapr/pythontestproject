"""
dictionay t json: serialization or EncodingWarning 
"""
import json
from _cffi_backend import typeof
person=[{'name':'test','age':40,"haschild":False,"role":["qa","dev"]},{'name':'sd','age':41},{'name':'sdsdsd','age':40},{'name':'ty','age':24}]
personjson=json.dumps(person,indent=4,sort_keys=True)# as a string so dumps if file its dump
#personjson=json.dumps(person,indent=4,separators=('; ','='))
"""
[
    {
        "name"="test"; 
        "age"=40; 
        "haschild"=false; 
        "role"=[
            "qa"; 
            "dev"
        ]
    }; 
    {
        "name"="sd"; 
        "age"=41
    }; 
    {
        "name"="sdsdsd"; 
        "age"=40
    }; 
    {
        "name"="ty"; 
        "age"=24
    }
]

"""
print(personjson)#"haschild": false,
with open('person.json','w') as file:#its file so dump
    json.dump(person,file,indent=4)
    
persondict=json.loads(personjson)
print(persondict)







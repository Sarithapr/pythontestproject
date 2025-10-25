'''
Created on Oct 20, 2025

@author: rharidas
'''
"""
dictionary stores kv pair and are like hashmap in java.
they are mutable and can add,delete,moify values based on key,key is unique"""
sampledict = {
     "saritha":111,
     "sgd":222
     }
sampledict1 = {
     "sgd":222,
     "saritha":111
     }
sampledict3 = {
     'sgd':1,
     'saritha':2
     }

sampledict4 = {
     'ttt':1,
     'tttttttt':2
     }
sampledict5 = {
     'aaa':1,
     'aaaaaaaa':2
     }
print(sampledict)
print(sampledict['saritha'])
sampledict['saritha']='141414'#modiftying element
print(sampledict)
sampledict['fywtyewygw']='14141434'#adding elements
print(sampledict)
sampledict['sdsds']='14141434'#adding elements
print(sampledict)
del sampledict['sdsds']
print(sampledict)
#looping thro dictionary
for x in sampledict:
    print(x,"=",sampledict[x])
print(len(sampledict))
print(sampledict == sampledict1)
print(sampledict != sampledict3)
print(sampledict.keys())#returns key as tuple
print(sampledict.values())
print(sampledict.get("saritha", "not tere"))
print(sampledict.get("sardsfitha", "not tere"))
print(sampledict.popitem())#randonly prints the valyes to be removed and removes a value from dictionry
print(sampledict)
print(sampledict.clear())
print(sampledict5.pop('aaa'))
print(sampledict5)







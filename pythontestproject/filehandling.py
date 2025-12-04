'''
Created on Oct 21, 2025

@author: rharidas
'''
"""
opening,closing,reading,writing,appeding and looping through data using for loop"""
file=open('/home/rharidas/Documents/pythonfilehandling','w')
file.write('I m testing file writing \n')
file.write('I m testing new file writing')

file.close()
"""
read(specified number of character from file) if ommited enire content will beread)
readline() read next line of file
readlines() read all lines as list of sting in file
"""

file=open('/home/rharidas/Documents/pythonfilehandling','r')
#print(file.read())
print("next")
print(file.read(2)) #both cant be used eith read() or read(charactercount)

file.close()

file=open('/home/rharidas/Documents/pythonfilehandling','r')

print(file.readlines()) #I ['I m testing file writing \n', 'I m testing new file writing

file.close()

file=open('/home/rharidas/Documents/pythonfilehandling','r')

print(file.readline()) #to read ony one line ie first line

file.close()

#Appening data to a file
file=open('/home/rharidas/Documents/pythonfilehandling','a')
#print(file.read())
file.write('again writin \n')
file.close()


file=open('/home/rharidas/Documents/pythonfilehandling','a+')
#print(file.read())
file.write('again writinsfdjshfdkjsfhkjsfhkjfskdfhsdkfhskfdhsdjk \n')
file.close()
#reading using loop
print("print line by line")
file=open('/home/rharidas/Documents/pythonfilehandling','r')
for i in file:#print line by line
    print(i)
file.close()
"""
Use 'a' → just append (write only)

Use 'a+' → append and read (you must .seek(0) before reading)

Mode    Can Read?    Can Write?    File Created if Missing?    Pointer Starts At    Overwrites Existing Data?
'a'    ❌ No    ✅ Yes    ✅ Yes    End of file    ❌ No
'a+'    ✅ Yes    ✅ Yes    ✅ Yes    End of file    ❌ No

with open('log.txt', 'a+') as f:
    f.write('World\n')
    f.seek(0)
    print(f.read())

"""



















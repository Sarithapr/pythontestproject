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

#reading using loop

file=open('/home/rharidas/Documents/pythonfilehandling','r')
for i in file:#print line by line
    print(i)
file.close()




















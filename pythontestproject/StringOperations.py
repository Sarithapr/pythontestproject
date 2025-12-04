#creating string
import keyword
name="John"
name1="John"
name2="C"
name3='C'
name4 = str("test")
name5 = str()
print (name,name1,name2,name3,name4,name5)
#string is immutable, once its created it cannot be modified and if you try to modify it will be different memory address.We can find the memory address with id)
str1 = "welcome"
str2 = "welcome"
print(id(str1),id(str2))#133106970401872 133106970401872
str2 = str2+"please"
print(id(str1),id(str2))#133106970401872 133106970442608
#operation on string *,+
str3 = str1 +"to berlin"
print(str3)
str4 = 2 *"to berlin"
print(str4)
print(2*str1)
#slicing is like substeingprint(str4) Index starts from 0 and end is given value -1
str="Welcome"
print(str[0:3])#Wel
print(str[1:3])#el
print(str[1:])#elcome
print(str[1:-1])#elcom
print("reveresed string",str[::-1])#elcom
print(str[:5])#Welco
#ord and chr functions
print(ord('A'))#char to ascii
print(chr(65))#asci to char
#functions
print(len("welcome"))
print(max("welcome"))
print(min("welcome"))
print("come" in "welcome")#true
print("come" not in "welcome")#false
print("hgfhds" in "welcome")#false 
print("hgfhds" not in "welcome")#true 
#String comparison based on ASCII value and can be checked >,<,>=,<=,!==,==
#Testing string:
s="welcome to worl"
print(s.isalnum())
print(s.isdigit())
print(s.isspace())
print(s.isupper())
print(s.islower())
print(s.isidentifier())#not a numer so false
print(keyword.iskeyword)
print(s.isidentifier())#not a numer so false
print(s.isalpha())
#searching for substring
print("searching for substring")
print("test and learning python".startswith("test"));
print("test and learning python".endswith("test"));
print("test and learning python".endswith("python"));#this is case sensitive search
print("test and learning python".find("test"));
print("test and learning python".find("testing"));#returns -1
print("test and learning python".rfind("t"));#find the position of last "t"
print("test and learning python".count("t"));
#String functions for converting string
print("test and learning python".capitalize());
print("test and learning python".title());
print("test and learning python".upper());
print("test and learning python".lower());
print("testand and LEARN python".swapcase());
print("testand and LEARN python".replace("and","or"));
#looping through string
s="Python"
for i in s:
    #print(s)prints python 6 times
    print(i) # prints each letter of python
#Number of unique characters
testingstring="Number of unique characters"
print(len(set(testingstring)))













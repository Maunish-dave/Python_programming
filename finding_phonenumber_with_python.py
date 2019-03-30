import re
reobject  = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo= reobject.search('My number is 415-555-4242.')
print("phone number is",  mo.group())

import re
phoneno = re.compile(r'\d{3}-\d{3}-\d{4}')
file = open("password.txt",'r')
var = phoneno.findall(file.read())

file2 = open("phone.txt",'w')
for i,j in enumerate(var):
    file2.write("phone{} : {}".format(i+1,j))
    file2.write("\n")
file.close()
file2.close()

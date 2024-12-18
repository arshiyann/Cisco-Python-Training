import re
file = open('emp.csv','r')

for var in file:
    var = var.strip() #remove \n
    if re.search('sales',var):
       print(var)

print('Will Print Who Are Replaced')
for var in file:
    var = var.strip() #remove \n
    if re.search('sales',var):
       result = re.sub('sales','QA',var)
       print(result)
file.close()

file_1 = open('file1.csv','r')
file_2 = open('file2.csv','w')

fobj1 = file_1.readlines()
fobj2 = file_2

for i in fobj1:
    if 'sales' in i:
        fobj2.write(i)



file_1.close()
file_2.close()
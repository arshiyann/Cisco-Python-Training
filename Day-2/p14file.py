file = open('pro_list.csv','w')
pro_list = ['p01,prodA,1000','p02,peodB,2000','p03,prodC,3000']


for i in pro_list:
    fobj = file.write(i+"\n")

file.close()
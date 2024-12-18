import re
used_size = ['12AB','106A','1111','5YS','150g']

total =0
for var in used_size:
    s = re.sub('[A-Za-z]','',var)
    total = total +int(s)
else:
    print(f'Sum of used_size: {total} GB')

s = 'data1:data2-data3!data4'
print(re.findall('[^a-zA-Z0-9]',s))

print(re.sub('[^a-zA-Z0-9]','|',s))

print(re.split('[^a-zA-Z0-9]',s))

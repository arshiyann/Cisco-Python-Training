fobj = open('input.csv','r')
L = fobj.readlines()
fobj.close()


for var in L:
    if 'sales' in var:
        L1 = var.split(',')
        print(f'{L1[1]}\t{L1[2]}')

filtered_lines = filter(lambda var: 'sales' in var, L)

result = map(lambda var: (var.split(',')[1], var.split(',')[2]), filtered_lines)
for col1, col2 in result:
    print(f'{col1}\t{col2}')

d = {}

while True:
    pid = input('Enter Product Id: ')
    if pid in d:
        print(f'Product id Exist: {d[pid]}')
        break
    else:
        pname = input(f'Enter Product Name: ')
        d[pid] = pname

    s = input("Do You Want to Exit? Yes/No: ")
    if s == 'Yes':
        break
    else:
        continue
print("Product ID \t Product Name")
for i in d:
    print(f'{i}\t\t{d[i]}')
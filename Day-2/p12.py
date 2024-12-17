emp = ['101,raj,sales,pune,1000','102,anu,hr,hyd,2000','100,vijay,sales,banglore,3000']

s = list[emp[1]]
sum =0
print("Emp Name   Emp Deaprtment")
for i in emp:
    n = i.split(",")
    print(n[1],"\t\t",n[2])
    sum = sum + int(n[4])

print(f'Total Sum of Emp Cost: {sum}')
    
emp_name = input("Enter Employee Name: ")
emp_id = input(f'Enter {emp_name} ID: ')
emp_dept = input(f'Enter  {emp_name}  Deaprtment: ')
emp_cost = input(f'Enter  {emp_name} Basic pay: ')

tax = float(emp_cost)* 0.32
total = tax + float(emp_cost)

print(f'''\n\nEmployee Name is:{emp_name}\nEmployee ID is:{emp_id}\n
        Employee Department: {emp_dept}\n Employee pay: {emp_cost}\n
        Tax Ampount: {tax}\n Gross Amount Pay: {total} 
''')
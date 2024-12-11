a_name = input(f'Enter App Name: ')

if a_name == "flask" or a_name == "fastapi":
    p_no = input(f'Enter {a_name} Port Number: ')
    print(f'App name: {a_name} \tRunning Port Number Is: {p_no}')
else:
    print("App Name is Not matched")
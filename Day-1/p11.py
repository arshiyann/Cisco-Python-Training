db = ["oracle","sql","mysql","plsql"]

db_in = input(f'Enter Database Name to Check: ')

if db_in in db:
    print(f'Database Exist at Index {db.index(db_in)}')
else:
    print("Database Not Present!!")
    db.append(db_in)

print(f'all Dbs of List')
for i in db: 
    print(f'{i}')
import sqlite3

con = sqlite3.connect('emp.db')

sth = con.cursor()

#sth.execute("create table emp_table(eid int,edept text ,ename text, ecity text, ecost int)")

with open("emp.csv",'r') as obj:
    for var in obj:
        var = var.strip()
        L = var.split(",")
        sth.execute("insert into emp_table values(?,?,?,?,?)",(L[0],L[1],L[2],L[3],L[4]
                                                               ))
sth.execute("select * from emp_table where ecost > 3000")

for var in sth:
    print(var)
    eid,ename,edept,ecity,ecost = var
    with open("emp.cvs",'a') as wobj:
         wobj.write(f'{eid}\t{ename}\t{edept}\t{ecity}\t{ecost}')

con.commit()

con.close()
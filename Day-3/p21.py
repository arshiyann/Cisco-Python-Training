class Enrollment:
    ename = ""
    edob = ""
    eplace = ""

    def f1(self,en,edob,eplace):
        self.ename = en
        self.dob = edob
        self.place = eplace
        print('Enrollment is done')
    def f2(self):
        print(f'About emp {self.ename} details emp name: {self} DOB: {self.dob} working city: {self.place}')

obj1 = Enrollment()

obj1.ename = 'Arsh'
obj1.edob ='1st Jan'
obj1.eplace = 'Aurangabad'

print(obj1.ename,obj1.edob,obj1.eplace)
class student:
    study="python"
    lang="english"

    def __init__(self, s_id,s_fees,s_qualification,s_yop):
        self.s_id=s_id
        self.s_fees=s_fees
        self.s_qualification=s_qualification
        self.s_yop=s_yop

    def student_det(self):
        return f"A student studying {student.study} in the language {self.lang} the student ID {self.s_id} for the fees amount {self.s_fees} the student is qualified as {self.s_qualification} on the year of pass {self.s_yop}"  
class employee:
    company="Pyspider"
    location="BTM"

    def __init__(self,e_id, salary, bond, shift, hours_working):
        self.e_id=e_id
        self.salary=salary
        self.bond=bond
        self.shift=shift
        self.hours_working=hours_working

    def employees_det(self):
        return f"employing status\n{'*'*50} \n the employee working in the company {employee.company} at {self.location} with the ID {self.e_id}, for the salary {self.salary} for {self.bond} number of years bond on {self.shift} with {self.hours_working} working hours"
class person(employee,student):
    planet="earth"
    has_heart='yes'

    def __init__(self, e_id, salary, bond, shift, hours_working,s_id,s_fees,s_qualification,s_yop,name,age,gender):
        super().__init__(e_id, salary, bond, shift, hours_working)
        student.__init__(self,s_id,s_fees,s_qualification,s_yop) 
        self.name=name
        self.age=age
        self.gender=gender
        
        if self.gender.lower()=="male":
            self.ident='his'
        else:
            self.ident='her'

    def person_det(self):

        print(f"the person name is {self.name} on the age of {self.age} {self.ident} {self.employees_det()} \n {'*'*50} \n the student details is \n{self.student_det()} ") 
if __name__ == '__main__':
    # print(dir(person))
    obj=person(101,15000,2,'day shift', 12,3040,35000,'B.E.CSE',2026,'Dhnaush',21,'male')
    obj2=person(102,13000,1,'night',10, 302,35000,'B.Sc',2025,'malya',20,'female')
    # obj.person_det()
    # obj2.person_det()
    # s=obj.s
    obj3=person(103,15000,3,'night',12,7201,45000,'MBA',2023,'aakash',20,'Male')
    obj3.person_det()
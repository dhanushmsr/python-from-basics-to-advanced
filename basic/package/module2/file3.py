class Employee:
    def __init__(self, salary):
        self.__salary = salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary",amount)

    def get_salary(self):
        return self.__salary

emp = Employee(10)
emp.set_salary()
print(emp.get_salary())
# emp.set_salary(-5000)
# print(emp.get_salary())

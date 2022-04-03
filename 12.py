class Employee:
    company = "Google"

    def __init__(self, name, salary, subunit, joining_date):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        self.joining_date = joining_date
        print("Employee is created!") 

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

    def getSalary(self):
        print(f"Salary for this employee working in : {self.company}- is : {self.salary}")
        
    def date_of_joining(self):
        print(f"The date of your joining is : {self.joining_date}")

    @staticmethod
    def greet():
        print("Good Morning, Sir")

    @staticmethod
    def time():
        print("The time is 9'AM in the morning")
        
    @staticmethod
    def congratulations():
        print("Hey , Congratulations you are selected for this job")

harry = Employee("Harry", 100, "YouTube" ,"July")
# harry = Employee() --> This throws an error (missing 3 required positional arguments:)
harry.getDetails()
harry.getSalary()
harry.date_of_joining()              
harry.greet()
harry.time()
(harry.congratulations())
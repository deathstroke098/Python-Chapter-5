#import logging

#logging.basicConfig(format='%(asctime)s - %(message)s',level=logging.DEBUG)

#logging.debug("This is for debugging")
#logging.info("This is for the general information")
#logging.warning("This a warning , Please check the program")
#logging.error("This is an error")
#logging.critical("Internet was down")

#class car:
    #def __init__(self, milage , year, build , engine, tyres):
        #self.milage = milage
        #self.year = year
        #self.build = build
       # #self.engine = engine
        #self.tyres = tyres
    

#these are the objects of the class
#scorpio1 = car(23,2020,"perfect", "KwaTe28" ,"perfect")
#fortuner2 = car(10 , 2020, "excellent" , "JSnsn123" , "Exquisite")

#this is the print statement
#print(scorpio1.engine)
#print(fortuner2.engine, fortuner2.year, fortuner2.build, fortuner2.tyres)


#class Employee:
#    no_of_leaves = 8
#
#    def __init__(self, aname, asalary, arole):
#        self.name = aname
#        self.salary = asalary
#        self.role = arole
#
#    def printdetails(self):
#        print (f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}")


#harry = Employee("Harry", 255, "Instructor")
#jerry = Employee("Lerry", 100, "Manager")



# rohan = Employee()
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"

#print(harry.salary)
#print(jerry.salary, jerry.role, jerry.name)




#class car:
#    def __init__(self,mileage, year, build, engine):
#        self.mileage = mileage
#        self.year = year
#        self.build = build
#        self.engine = engine

#mahindra = car(10, 2020, "njhj12" , "JJHHH121")
#ford = car(5, 2021, "jnjj122321,", "ZJFF123")

#print(f"The Engine of this car is :{mahindra.engine} \nThe build of this car is :{mahindra.build}")
#print(f"The Engine of this car is :{ford.engine} \nThe build of this car is :{ford.build}")

# Python program to demonstrate
# use of class method and static method.

class test:
    def __init__(self, a, b ):
        self.a = a
        self.b = b

    def test_customer(self , z):
        return z + self.a    

    def __str__(self):  # basically thr use of __str__ and @staticmethod are the same...
        return"This is my function for the abstraction"

    @staticmethod #static method can be called using the class name (test) or the variable created by the name (o)
    def statice_method():
        return("This is the static method ")    


    @staticmethod
    def isopen(day):
        if day == "sunday":
            return False
        else :
           return True        

    @staticmethod
    def good_news():
        return ("congratulations bro , you are selected")


o = test(5 , 4)
print(o.test_customer(2))
print(test.statice_method())
print(o)
print(o.isopen("friday"))
print(o.good_news())  #whenever you are calling a function always use () double parentheses

# num1=5
# num2=10
# sum=num1+num2
# print(sum) 



# dic=[]
# for i in range(10):
#     if i%2==0:
#      dic.append(i)
# print(dic)


# sum=0
# for k in dic:
#    sum+=k
# avg=sum/k
# print(avg)

# def sqr(x):
#     return x*x
# print(sqr(5))



# student={ 

# }

# name=input("enter student name: ")
# age=int(input("enter age: "))
# roll_number=int(input("enter student roll number: "))
# student["name"]=name
# student["age"]=age
# student["roll_number"]=roll_number

# print(student)



# student={"Ali": 85, "Sara": 92, "Ahmed": 78}
# print(student["Ali"])
# for i in student:
#     print(f"{name} ke marks: {student[name]}")






# # Dictionary
# student = {"Ali": 85, "Sara": 92, "Ahmed": 78}

# # Single student marks print
# print("Ali ke marks:", student["Ali"])

# # Loop ke through sab students ke marks print karo
# for k in student:
#     print(f"{k} ke marks: {student[k]}")

# name="kainat i love you"
# find=len(name)
# ok=name[2]
# print(ok)



  #string operations

# string="\kainat\ is a good girl but she loves a guy \n who is hindu belongs to\tindia such a bakwas admi"
# # print(string.endswith('y'))
# # print(string.count('a'))
# # print(string.capitalize())
# # print(string.find('i'))
# print(string.replace('jainat','kainat'))
# print(string)



#list operation
# list1=["kainat",9,5,"sana",{"saba":34,"raniya":78}]

# print(list1[4])
# print(list1.insert(1,"karunesh"))
# print(list1)


# store=[]
# dictionar=["kainat","saba","soniya"]
# for i in dictionar:
#     if i.endswith('t'):
#       store.append(i)
# print(store)



# store = []
# dictionar = ["kainat", "saba", 3, "soniya", 5]

# for i in dictionar:
#     if isinstance(i, int) and str(i).endswith('5'): #sting b agr 5 pr end hova ho ya int mai 5 ho
#        store.append(i)

# print(store)
# dictionar.pop(1)
# print(dictionar)
# dictionar.remove("kainat")
# print(dictionar)
# print(dictionar.reverse())
# ok=len(dictionar)
# print(ok)



# fruits=[]
# for i in range(7):
#     user1=input(f"enter fruit:{i} ")
#     fruits.append(i)
# print(fruits)


# list=[1,2,4,5,]
# sum=0
# for i in list:
#     sum+=i
# print(sum)





#dictionay operations:
# dictionary = {
#     'ali': {"age": 45, "marks": 88, "class": 9},
#     'saba': {"age": 15, "marks": 909, "class": 3},
#     'nayaab': {"age": 95, "marks": 100, "class": 6},
# }

# for student, info in dictionary.items():
#     if info['marks'] > 90:
#         print(student, info)


# Nested dictionary example
# dictionary = {
#     'ali': {"age": 45, "marks": 81, "class": 9},
#     'saba': {"age": 15, "marks": 909, "class": 3},
#     'nayaab': {"age": 95, "marks": 100, "class": 6},
#     'batch1': {      # nested dictionary
#         'farah': {"age": 20, "marks": 85, "class": 4},
#         'junaid': {"age": 22, "marks": 95, "class": 5}
#     }
# }

# Recursive function to find all students with marks > 90
# def find_high_marks(d):
#     for key, value in d.items():
#         if isinstance(value, dict):
#             # agar value ke andar 'marks' hai to check karo
#             if 'marks' in value and value['marks'] > 90:
#                 print(key, value)
#             else:
#                 # agar value aur nested dictionary hai
#                 find_high_marks(value)

# Call the function
# print(dictionary)
# def update(d):
#     user=input("enter name: ")
#     updates_marks=int(input("upate marks"))
#     for key,val in d.items():
#         if isinstance(val,dict):
#             if user==key:
#                val['marks']=updates_marks
#                print(f'updated{key} marks are updated to {updates_marks}')
#                return

# # find_high_marks(dictionary)
# update(dictionary)
# print(dictionary)






# print(dictionary)
# def remove(d):
#     user=input("enter name: ")
#     if user in d:
#                del d[user]
#                print(f'{user} remove successfully')
   
   
#     else:
#                print('user not found')          
              
#                return
# remove(dictionary)
# print(dictionary)


# def search(d):
       
#         search_name=input("enter user name to search")
#         for key,val in d.items():
#          if search_name==key:
                
                
#                 print("user found")
                
#                 print(f'{key} {val}')
                
                
#          else:
#                 print("no user")
# search(dictionary)

# num=[]
# for i in range(1,3):
#     numbers=int(input(f"please enter number:{i}"))
#     num.append(numbers)
# print(num)
# print("the greates number is",max(num))



# while True:
#     email=input("enter your email: ")
#     password=int(input("enter your password: "))
#     if(email=="kainat" and password==2345):
#         print("you have login successfully")
#         pass
#     else:
#         print("wrong cridentials")


# for i in range(1,11):
#     print(f"5 * {i} = {5*i}")

# n=5
# for i in range(1, n+1):
#     print("*"*i, end='')
#     print("")
  

# n=5
# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*(2*i-1) , end='')
#     print("")    


# n = 5
# for i in range(1, n+1):
#     print(" " * (n - i) + "*" * (2*i - 1))    ======
                                              #  =     =
# n=5
# for i in range(1, n+1):
#     print("*"*i , end='')
#     print("")  


# n=5

# for i in range(1, n+1):           # row loop
#     for j in range(1, n+1):       # column loop
#         if i == 1 or i == n or j == 1 or j == n:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()  # move to next line 


# def good_day(name,ending):
#     print("good day ",name)
#     print(ending)
#     return "done"
# a=good_day("harry","thankyou")
    
    
# string="sainat is a good girl i realy like her.she lives in islamabad"
# # ok=string.find('girl')
# # print(ok)
# help(string.capitalize())

# help(str.replace)
# help(str.capitalize)
# help(list.append)
# help(set.remove)
# help(list.insert)
# l=["kai","sai","jai",3,5,6]
# l.insert(1,"karunesh")
# print(l)

# l = ["kai","sai","jai",3,5,6]

# l.insert(1, "karunesh")   # correct

# print(l)
# help(list.remove)
# help(len)
# help(sum)
# list1=[1,3,5,6,8]
# # print(dir(list))
# print(isinstance(list1,list))
# # help(isinstance)
# # print(id())
# print(id(list1))
# print(dir(list))


num=['1',3.56,5.9,6,7]


# print(any(isinstance(i,str) for i in num))
# fruits=["mango","banan","orange"]
# # for i in enumerate(fruits):
# #     print(i)
# ok=zip(num,fruits)
# print(list(ok))
# num1=[float(x) for x in num]
# num2=[abs(x) for x in num1]
# print(list(num2))

# print(len(num2))
# kait={2,3,4,5,6}
# sait={4,5,6,8,9,0}

# ok=kait.clear()
# print(ok)
# print(kait)
# help(set.clear)

# students = {
#     "ali": {"age": 20, "marks": 85},
#     "saba": {"age": 18, "marks": 92},
#     "nayaab": {"age": 19, "marks": 78},
#     "kainat": {"age": 21, "marks": 88}
# }

# help(dict.get)
# ok=students.items()
# name=input("enter the name: ")
# update_age=input("update age")
# update_name=input("update the name")
# for key ,val in students.items():
#     if key==name:
#         key=update_name
#         # val['age']=update_age
        
#         print(key,val)
# def update():
#     name=input("enter new name: ")
#     age=int(input("enter tour age: "))
#     marks=int(input("enter new marks: "))
#     students[name]={"age":age, "marks":marks}
# update()
# print(students.copy())
# print(students.get('ali'))
      
# print(students)

# for col in range(1,9):
#     for row in range(1,9):
#        print(f"({col},{row})",end='')

# for i in range(1,6):
#     for j in range(1,6):
#         if i==1 or i==5 or j==1 or j==5:
#             print("*", end='')
#         else:
#             print(" ",end='')
       
#     print("")

# attempt=0
# pin=1234

# while (attempt<3):
#   check=int(input("enter your pin: "))
#   if pin==check:
#         print("Access granted")
#         break
#   else:
#         print(f"wrong pin{2-attempt} ")
#         attempt+=1

# password=1234
# email="kainat@"
# attempt=0
# while attempt<3:
#     user_pas=int(input("enter your passwprd: "))
#     user_email=input("enter your email: ")
#     if(email==password and user_email==email):
#         print("access granted")
#         break
#     else:
#         print("wrong credentials")
#         print(f" you have {2-attempt}")
#         attempt+=1

# for i in range(1,4):
#     for j in range(1,4):
#         print(f'({i},{j})',end='')
# even=[]
# l = [2, 5, 8, 11, 14]
# for i in l:
#  if i%2!=0:
#   even.append(i)
# print(even)


# string=[]
# l = ["ali", 5, "saba", 10, "kainat"]
# for i in l:
#     if isinstance(i,str):
#         string.append(i)
# print(string)


# *
# **
# ***
# ****
# *****

# n=6
# for i in range(1,n):
#     print("*"*(n-i))
    # print(" ")
# l = [10, 45, 2, 99, 23]
# help(max)
# l.max()
# print(max(l))
# max()
# total=[]
# count=0
# help(list.count)
# print(dir(list))
# l = ["ali", 5, "saba", 10, "kainat"]
# for i in l:
#     if isinstance(i,str):
#       total.append(i)
#       count+=1
# print(total)
# print(len(total))
# print(count)
  
# l = [10, 45, 2, 99, 23]
# max1=l[0]
# for i in l:
#     if i>max1:
#      max1=i
# print(max1)

# Ek function banao jo 2 numbers ka sum return kare
# Ek function banao jo number even ya odd check kare
# Ek function banao jo list ka maximum return kare
# Ek function banao jo string reverse kare

# def sum(a,b):
#     return a+b
# print(sum(3,5))

# def cheaker():
#     adder=[]
#     list=[1,2,3,5,6,7]
#     for i in list:
#         if i%2==0:
#             adder.append(i)
#     print(adder)
# cheaker()

# def cheaker(a):
#     if a%2==0:
#         print("even number")
#     else:
#         print("odd")
# print(cheaker(8))

# def max1(list1):

#   max1=list1[0]
#   for i in list1:
#     if i>max1:
#         max1=i
# return max1
        
# result=max1(list1=[1,2,3,5,6,7])
# print(result)





# Ek function banao jo string reverse kare

# def reverser(string):
#     ok= string[::-1]
#     return  ok
# result=reverser("kainat")
# print(result)



# def reverser(string):
#     rev = ""
#     for i in string:
#         rev = i + rev
#     return rev

# result = reverser("kainat")
# print(result)


# day=input("enter your day")
# days={
#     1:"monday",
#     2:"tuesday",
#     3:"wed",
#     4:"invalid"

# }

# print(days.get(day,"invallid"))

# day = input("enter your day: ")

# days = {
#     1: "Monday",
#     2: "Tuesday",
#     3: "Wednesday",
#     4: "Thursday",
#     5: "Friday",
#     6: "Saturday",
#     7: "Sunday"
# }

# # Get day name, default = "Invalid"
# print(days.get(day, "Invalid"))
   
# day = 5

# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:  # default
#         print("Invalid")
# import os
# if os.path.exists:
#  class my_class:
#     @staticmethod
#     def cheaker(file_name):
#         with open(file_name,"a") as f:
#             return f.write("ok good")
#  content=my_class.cheaker("kainat.txt")
#  print(content)

# else:
#     with open(file_name,"w") as f:
#      f.write("good hogaya")
#      content=my_class.cheaker("kainat.txt")
#      print(content)


# import os

# class MyClass:
#     @staticmethod
#     def checker(file_name):
#         with open(file_name, "a") as f:
#             return f.write("ok good\n")

# file_name = "kainat.txt"

# if os.path.exists(file_name):
#     content = MyClass.checker(file_name)
#     print(content)
# else:
#     with open(file_name, "w") as f:
#         f.write("file created\n")
    
#     content = MyClass.checker(file_name)
#     print(content)


# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def show(self):
#         print(self.name, self.marks)
       

# s1 = Student("Ali", 90)
# s2=Student("kainat",900)
# s1.show()
# s2.show()



# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def show_info(self):
#         print(f"{self.name} has scored: {self.marks}")
#     def check_result(self):
#         if self.marks>=100:
#             print("A GRADE")
#         elif  self.marks>=80:
#             print("B GRADE")
#         elif self.marks>=70:
#             print("C GRADE")
#         else:
#             print("FAILED")
# s1=Student("kainat",90)

# s2=Student("saniya",78)
# print("student 1 reullt")
# s1.show_info()
# s1.check_result()
# print("student 2")

# s2.show_info()
# s2.check_result()

 
            



# class bank:
#     def __init__(self, name,balance):
#         self.__balance=balance
#         self.name=name
#     def show_info(self):
#         print(f"{self.name}:{self.__balance}")
#     def deposit(self,amount):
#         self.__balance+=amount
# s1=bank("kainat",900)
# s1.deposit(700)
# s1.show_info()

# Parent class



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     def show_info(self):
#         print(f"Name: {self.name}, Salary: {self.salary}")

# # Child class
# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)  # parent ka constructor call
#         self.department = department

#     def show_department(self):
#         print(f"Department: {self.department}")

# # Objects
# e1 = Employee("Ali", 50000)
# m1 = Manager("Kainat", 70000, "IT")

# e1.show_info()
# m1.show_info()         # inherited from Employee
# m1.show_department()   # specific to Manager


# class  employee:
#     def __init__(self,name, basics_salary):
#         self.name=name
#         self.salary=basics_salary
#     def show_info(self):
#         print(f"{self.name}:{self.salary}")
#     def calculate_balance(self,amount):
#         self.amount=amount
#         self.salary+=(amount/100)*100
#         print(f"toal salary is {self.salary}")
        


      
# class manager(employee):
#     def __init__(self,name,salary,department):
        
#         super().__init__(name,salary)
#         self.department=department
#         # print(f"{self.name} {self.salary}  ")
#     def show_dept(self):
#         print(f"{self.name} department is: {self.department} ,{self.salary}")

# s1=employee("kainat",6000)  
# s1.show_info()
# s1.calculate_balance(500)

# m1=manager("ali",80000,"IT")
# m1.show_dept()


# class cat:
#     @staticmethod
#     def __init__(self,call,eat):
#         self.call=call
#         self.eat=eat
#     def working(self):
#         print(f" cat say {self.call} and eat {self.eat}")
        
    
# class dog(cat):
#     @staticmethod
#     def __init__(self, call, eat,night):
#         super().__init__(call, eat)
#         self.night=night
#     def working(self):
       
#         print(f"dog say{self.call} and eat {self.eat} in the noght do {self.night}")
    
# cat.working("meo", "meat")


# dog.working("barking","plao","duty")




# class Cat:
#     def __init__(self, call, eat):
#         self.call = call
#         self.eat = eat

#     def working(self):
#         print(f"Cat says {self.call} and eats {self.eat}")


# class Dog(Cat):
#     def __init__(self, call, eat, night):
#         super().__init__(call, eat)
#         self.night = night

#     def working(self):
#         print(f"Dog says {self.call}, eats {self.eat} and does {self.night} at night")


# # Objects
# animal1 = Cat("meow", "meat")
# animal2 = Dog("barking", "pulao", "guarding")

# # Method calls
# animal1.working()
# animal2.working()



# try:
#     # risky code
#     num = int(input("Enter a number: "))
#     print(10 / num)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except ValueError:
    
    
#     print("Please enter a valid number!")

# try:

#   with open("sanat.txt", "a") as f:
#    data=f.write("Nosheeno mairi jaan ho")
#    print(data)
# except FileNotFoundError:
#   print("file not found")


# data=[1,2,3,4,5]
# index=5
# try:
    
#         print("it is in working",data[6])

# except IndexError:
#         print("out of range")


#  Requirements
# Student Class
# Attributes: name, roll_number, marks
# Methods:
# show_info() → print student info
# update_marks(new_marks) → update marks
# File Handling
# Data file: "students.txt"
# Save new student → append to file
# Load students → read file
# Handle FileNotFoundError
# User Menu
# Add new student
# Display all students
# Update marks
# Exit
# Error Handling
# Wrong input (ValueError)
# File missing (FileNotFoundError)
# Invalid student roll number (custom check)


# class student:

#  def __init__(self,name, roll_number, marks):
#                 self.name=name
#                 self.roll_number=roll_number
#                 self.marks=marks
# def show_info(self):
         
#                 print(f"name:{self.name} roll number: {self.roll_number} marks:{self.marks}")
                
        
# def create_user(self):
              
#               record=[]
#               self.name=input("please enter the user name:")
#               self.roll_number=int(input("please enter the user roll number:"))
#               self.marks=int(input("please enter the user marks:"))
#               record.appent(self.name,self.roll_number, self.marks)



# def update_marks(self,new_marks):
#               self.marks=new_marks
#               user_name=input("please enter the name to update the marks of user:")
#               updated_marks=int(input("please enter the marks to update:"))
#               for i in student.record.items():
              
            
#                     if student.record.name==user_name:
#                           student.record.marks=updated_marks
                          
#               print("marks successfully updates")
# def store_data(filename):
#               with open(filename,"a") as f:
#                     return f.write(name,roll_number,marks)
        
# def load_data(filename):
#               with open(filename,"r") as f:
#                     return f.read()
# print("enter number 1 to 4")
# number=int("enter number to swich the mode:")  

# match case(number):

#  case 1:
#    show_info()
#  case 2:
#   create_user()

#  case 3:
#   update_marks()

#  case 4:
#   print("invlaid number")               
                 

  

# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks

#     def show_info(self):
#         print(f"Name: {self.name}, Roll: {self.roll_number}, Marks: {self.marks}")

#     def update_marks(self, new_marks):
#         self.marks = new_marks
#         print(f"{self.name}'s marks updated to {self.marks}")

#     def store_data(self, filename):
#         with open(filename, "a") as f:
#             # Store in CSV-like format
#             f.write(f"{self.name},{self.roll_number},{self.marks}\n")

#     @staticmethod
#     def load_data(filename):
#         students = []
#         try:
#             with open(filename, "r") as f:
#                 for line in f:
#                     name, roll, marks = line.strip().split(",")
#                     students.append(Student(name, int(roll), int(marks)))
#         except FileNotFoundError:
#             print("File not found, starting fresh!")
#         return students


# # 🧪 Usage Example
# students_list = Student.load_data("data.txt")  # load existing data

# # Add new student
# s1 = Student("Kainat", 101, 95)
# students_list.append(s1)
# s1.store_data("data.txt")

# # Show info
# s1.show_info()

# # Update marks
# s1.update_marks(98)




# class Student:

#     def __init__(self, name="", roll_number=0, marks=0):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks

#     def show_info(self):
#         print(f"Name: {self.name}, Roll: {self.roll_number}, Marks: {self.marks}")

#     def create_user(self):
#         self.name = input("Enter name: ")
#         self.roll_number = int(input("Enter roll number: "))
#         self.marks = int(input("Enter marks: "))

#     def update_marks(self):
#         self.marks = int(input("Enter new marks: "))
#         print("Marks updated")

#     def store_data(self, filename):
#         with open(filename, "a") as f:
#             f.write(f"{self.name},{self.roll_number},{self.marks}\n")

#     @staticmethod
#     def load_data(filename):
#         try:
#             with open(filename, "r") as f:
#                 print(f.read())
#         except FileNotFoundError:
#             print("File not found")


# # 🔹 Main Program
# s = Student()

# print("1. Show Info")
# print("2. Create User")
# print("3. Update Marks")
# print("4. Load Data")

# number = int(input("Enter choice: "))

# match number:
#     case 1:
#         s.show_info()
#     case 2:
#         s.create_user()
#         s.store_data("data.txt")
#     case 3:
#         s.update_marks()
#     case 4:
#         Student.load_data("data.txt")
#     case _:
#         print("Invalid choice")



#/////////////////////////////////////////


# class Student:
#     def __init__(self, name, roll_number, marks):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = marks

#     def show_info(self):
#         print(f"Name: {self.name}, Roll: {self.roll_number}, Marks: {self.marks}")


# # 🔹 Load Data from File
# def load_data(filename):
#     students = []
#     try:
#         with open(filename, "r") as f:
#             for line in f:
#                 name, roll, marks = line.strip().split(",")
#                 students.append(Student(name, int(roll), int(marks)))
#     except FileNotFoundError:
#         print("File not found, starting fresh!")
#     return students 

# # 🔹 Save All Data (Overwrite)
# def save_all(students, filename):
#     with open(filename, "w") as f:
#         for s in students:
#             f.write(f"{s.name},{s.roll_number},{s.marks}\n")


# # 🔹 Add New Student
# def add_student(students):
#     try:
#         name = input("Enter name: ")
#         roll = int(input("Enter roll number: "))
#         marks = int(input("Enter marks: "))

#         s = Student(name, roll, marks)
#         students.append(s)

#         print("Student added successfully!")

#     except ValueError:
#         print("Invalid input! Please enter correct data.")


# # 🔹 Display Students
# def display_students(students):
#     if not students:
#         print("No students found!")
#     else:
#         for s in students:
#             s.show_info()


# # 🔹 Update Marks
# def update_marks(students):
#     try:
#         roll = int(input("Enter roll number to update: "))
#         new_marks = int(input("Enter new marks: "))

#         for s in students:
#             if s.roll_number == roll:
#                 s.marks = new_marks
#                 print("Marks updated!")
#                 return

#         print("Student not found!")

#     except ValueError:
#         print("Invalid input!")


# # 🔹 Main Program
# filename = "students.txt"
# students = load_data(filename)

# while True:
#     print("\n--- MENU ---")
#     print("1. Add Student")
#     print("2. Display Students")
#     print("3. Update Marks")
#     print("4. Exit")

#     try:
#         choice = int(input("Enter choice: "))

#         if choice == 1:
#             add_student(students)
#             save_all(students, filename)

#         elif choice == 2:
#             display_students(students)

#         elif choice == 3:
#             update_marks(students)
#             save_all(students, filename)

#         elif choice == 4:
#             print("Exiting program...")
#             break

#         else:
#             print("Invalid choice!")

#     except ValueError:
#         print("Please enter a valid number!")



# class Student:
#     def __init__(self, name, roll_number,marks):
#         self.name=name
#         self.roll=roll_number
#         self.marks=marks
    
#     def show_info(self):
#         print(f" name: {self.name} roll number:{self.roll} marks:{self.marks}")

# def load_data(filename):
#         students=[]
#         try:
#             with open(filename,"r") as f:
#              for line in f:
#                 name,roll,marks=line.strip().split(",")
#                 students.append(Student(name, int(roll) , int(marks)))
#             return students
       
#         except FileNotFoundError:
#          print("file not found")
#          return []  

        
# def save_students(students,filename):
#        with open(filename,"w") as f:
#         for s in students:
#           f.write(f"{s.name},{s.roll},{s.marks}\n")
        
# def add_students(students):
#        name=input("please enter student name: ")
#        roll_number=int(input("please enter student roll number: "))
#        marks=int(input("please enter student marks: "))
#        s=Student(name,roll_number,marks)
#        students.append(s)
#///////////////////////////////////////////////


    # try:  
    #     name = input("Enter name: ")
    #     roll = int(input("Enter roll number: "))
    #     marks = int(input("Enter marks: "))

    #     s = Student(name, roll, marks)
    #     students.append(s)

    #     print("Student added successfully!")

    # except ValueError:
    #     print("Invalid input! Please enter correct data.")

# class hadi:
#    def __init__(self,name,kaam,daam):
#         self.name=name
#         self.kaam=kaam
#         self.daam=daam
#    def show_data(self):
#         print(f"{self.name},{self.kaam}, {self.daam}")
        
# def load_hadi(filename):
#         student=[]
#         try:
#             with open(filename,"r") as f:
#                 for h in f:
#                     name,kaam,daam=h.strip().split(",")
#                     s=hadi(name,kaam,daam)
#                     student.append(s)
#                 return student
#         except FileNotFoundError:
#             print("list not found")
#             return []
        
# def save_file(filename,student):
#         with open(filename,"w")as f:
#             for s in student:
#                 f.write(f"{s.name},{s.kaam},{s.daam}\n")
                
                
# def add_hadi(student):  
        
#         try: 
#          name=input("enter name")  
#          kaam=input("enter kaam") 
#          daam=input("enter daam") 
        
#          s=hadi(name,kaam,daam)
#          student.append(s)
         
#         except ValueError:
#             print("invaid input")
           
    

               
# def update_hadi(students):
#       user_name = input("Enter name to update: ")

#       for s in students:
#         if s.name == user_name:

#             while True:
#                 print("\n1. Update name")
#                 print("2. Update kaam")
#                 print("3. Update daam")
#                 print("4. Exit")

#                 choice = int(input("Enter choice: "))

#                 if choice == 1:
#                     s.name = input("Enter new name: ")
#                     print("name updated")

#                 elif choice == 2:
#                     s.kaam = input("Enter new kaam: ")
#                     print("kaam updated")

#                 elif choice == 3:
#                     s.daam = input("Enter new daam: ")
#                     print("daam updated")

#                 elif choice == 4:
#                     break

#                 else:
#                     print("Invalid input")

#             return   # stop after updating one student

#       print("Student not found")
# # def find_hadi(student):
# #     found=False
# #     user_name=input("enter user name")
# #     for s in student:
# #         if s.name==user_name:
# #             print(student)
# #             found=True
# #         if not found:
# #             print("student not found")

# def find_hadi(student):
#     found = False
#     user_name = input("Enter user name: ")

#     for s in student:
#         if s.name.strip().lower() == user_name.strip().lower():
#             s.show_data()   # 👈 correct print
#             found = True
#             break           # optional (stop after found)

#     if not found:
#         print("Student not found")
    
    
# def display_result(student):
        
#     for s in student:
#         s.show_data()
# filename="dot.txt"
# student=load_hadi(filename) 
    
                
# while True:
#     print("user menu")
#     print("enter 1 to add student")
#     print("entert 2 to update student")
#     print("enter 3 to show result")
#     print("entetr 4 to exit")  
    
#     try:
#         choice=int(input("enter your choice: "))
#         if choice==1:
#          add_hadi(student)
#          save_file(filename,student)
#         elif choice==2:
#             update_hadi(student)
#             save_file(filename,student)
#         elif choice==3:
#             print(student)
#             display_result(student)
#         elif choice==4:
#             find_hadi(student)
             
#         else:
#             print("invalid input")
#     except ValueError:
#       print("invalid input")
      
      
      
        
                 
        

        

   

         
          
          
             

        
           

        
# class Allah:
#     def __init__(self,bnda, ibadat,kaam):
#         self.bnda=bnda
#         self.ibadat=ibadat
#         self.kaam=kaam
#     def show_info(self):
#         print(f"{self.bnda},{self.ibadat},{self.kaam}")
        
# def load_bnda(file_name):
#     bnda1=[]
#     try:
#      with open(file_name,"r") as f:
       
#          for s in f:
#             bnda,ibadat,kaam=s.strip().split(",")
#             S=Allah(bnda,ibadat,kaam)
#             bnda1.append(S)
#          return bnda1
#     except FileNotFoundError:
#             print("file not found")
#             return []
# def save_bnda(filename,bnda1):
    
#      with open(filename,"w")as f:
#          for s in bnda1:
#           f.write(f'{s.bnda},{s.ibadat},{s.kaam}\n')

# def add_bnda(bnda1):
#     bnda=input("enter bnda name: ")
#     ibadat=input("entr ibadat type:")
#     kaam=input("enter kaam: ")
#     bnda1.append(Allah(bnda,ibadat,kaam))
       
    
# def update_bnda(bnda1):
#     user=input("enter bnda name")
#     for s in bnda1:
#         if s.bnda==user:
#             while True:
              
#                print("enter 1 name: ") 
#                print("enter 2 bnda ibadat: ") 
#                print("enter 3 bnda kaam: ") 
               
#                print("enter 4 to exit")
#                try:
#                 choice=int(input("enter your choices"))
#                except ValueError:
#                    print("invalid attempt")
#                    continue
#                if choice==1:
#                    s.bnda=input("updata bnda name")
#                elif choice==2:
#                    s.ibadat=input("update ibadat")
#                elif choice==3:
                   
#                    s.kaam=input("update kaam")
#                elif choice==4:
#                    break
#                else:
#                    print("invalid atttempt")
#             return
# def find_bnda(bnda1):
#     user=input("enter user name")
#     # for s in bnda1:
#     #     if s.bnda.lower()==user.lower():
#     #         return s.bnda
#     # return None
#     for s in bnda1:
#         if s.bnda.strip().lower() == user.strip().lower():
#             s.show_info()   # 👈 correct print
#             found = True
#             break           # optional (stop after found)

#     if not found:
#         print("Student not found")
    
    
                
# def remove_bnda(bnda1):
#     user=input("enter user name to remove")
#     for s in bnda1:
#         if s.bnda.lower()==user.lower():
#             bnda1.remove(s)
#             print("person deleted")
#             return
#     print("no bnda find")
            
# def display_allbndas(bnda1):
#     try:
#      for s in bnda1:
#        result= s.show_info()
#        print(result)
#     except FileNotFoundError:
#         print("no list")
        
         
# filename="cot.txt"
# bnda1=load_bnda(filename)
# while True:
#     print("------menue-----")
#     print("1 for bnda add")
#     print("2 for update bnda")
#     print("3 for remove student")
#     print("4 to search bnda")
#     print("5 show all user")
#     print("6 for terminate")
#     choice=int(input("enter your choice: "))
#     if choice==1:
#         add_bnda(bnda1)
#     elif choice==2:
#         update_bnda(bnda1)
#         save_bnda(filename,bnda1)
#     elif choice==3:
#         remove_bnda(bnda1)
#         save_bnda(filename,bnda1)
#     elif choice==4:
#         find_bnda(bnda1)
      
    
#     elif choice==5:
#         display_allbndas(bnda1)
#     elif choice==6:
#         break
#     else:
#         print("invalid attempt")
#         continue
                   
                   
                       
               
# storage={}
# def store(storage):
#   name=input("enter namee")
#   age=int(input("enter your age:"))
#   work=input("enter your work")
    
#   storage[name]={"age":age,"work":work}

#   for i,v in storage.items():
#     print({i},{v})
   
# storage = {}

# def store(storage):
#     name = input("enter name: ")
#     age = int(input("enter your age: "))
#     work = input("enter your work: ")
    
#     storage[name] = {"age": age, "work": work}

#     # for i, v in storage.items():
#     #     print(i, v)
#     for i, v in storage.items():
#      print(f"Name: {i}, Age: {v['age']}, Work: {v['work']}")
# while True:
#     print("------menue-------")
#     choice=int(input("enter your choices"))
   
        
#     if choice==1:
#         store(storage)
#     elif choice==2:
#         break
#     else:
#         print("invalid attem")
        
        
        
        
#         C:\Windows\system32>sfc /scannow

# Beginning system scan.  This process will take some time.

# Beginning verification phase of system scan.
# Verification 100% complete.

# Windows Resource Protection found corrupt files but was unable to fix some of them.
# For online repairs, details are included in the CBS log file located at
# windir\Logs\CBS\CBS.log. For example C:\Windows\Logs\CBS\CBS.log. For offline
# repairs, details are included in the log file provided by the /OFFLOGFILE flag.


# storage={}

# def load_data(filname,storage):
#    try:
#        with open(filname,"r")as f:
#            for data in f:
#                name,age,task=data.strip().split(",")
#                storage[name]={"age":age,"task":task}
#            return storage
#    except FileNotFoundError:
#        print("file not found")  
       
# def save_data(filename,storage):
#     with open(filename,"w")as f:
#         for s,v in storage.items():
#             f.write(f"{s},{v['age'],{v["task"]}}")
#         return storage
        
# import numpy as np    
   
# x=[10,20,30,40,50,60]
# v=np.array(x)  
# sum=np.mean(v)
# variance=np.var(v)
# standard_deviation=np.std(v)
# normalize=(x-sum)/standard_deviation
# print(normalize)
# import numpy as np

# # x=([1,3,4,5,6],[5,6,3,2,4])
# # v=np.array(x)
# # print(np.dot(v))
# a=np.array([1,2,3,4,5])
# # b=np.array([5,6,7,8,7])
# # print(np.dot(a,b))

# print(np.var(a))
# print(np.std(a))


# new_list=[]

# marks=[2,3,4,5,6]
# for i in marks:
#     new1=i+5
#     new_list.append(new1)
# print(new_list)

import numpy as np
# marks=[3,4,6,7,8]
# x=np.array(marks)
# new_marks=x+5
# print(new_marks)

# marks=np.array([[1,2,0.4,5.6,7],
#                [1,2,0.4,5.6,7],
#                [1,2,0.4,5.6,7],
#                [1,2,0.4,5.6,7]])
# weight=np.array  ([[1,2,0.4,5.6,7],
#                [1,2,0.4,5.6,7],
#                [1,2,0.4,5.6,7],
#                [1,2,0.4,5.6,7]])
# print(np.dot(marks,weight))

# print(marks.shape)
# print(marks.size)



# marks = np.array([
#     [1, 2, 0.4, 5.6, 7],
#     [1, 2, 0.4, 5.6, 7],
#     [1, 2, 0.4, 5.6, 7],
#     [1, 2, 0.4, 5.6, 7]
# ])

# weight = np.array([
#     [1, 2, 0.4, 5.6, 7],
#     [1, 2, 0.4, 5.6, 7],
#     [1, 2, 0.4, 5.6, 7],
#     [1, 2, 0.4, 5.6, 7]
# ])

# # Weight transpose karo — shape (4,5) se (5,4) ho jayega
# result = np.dot(marks, weight.T)
# print(result)
# print(result.shape)  # (4, 4) aayega


# import numpy as np

# class_a = np.array([89, 90, 91, 90, 90])
# class_b = np.array([40, 95, 60, 100, 55])

# print("Class A Mean:", np.mean(class_a))
# print("Class B Mean:", np.mean(class_b))

# print("Class A Variance:", np.var(class_a))
# print("Class B Variance:", np.var(class_b))

# print("Class A Std Dev:", np.std(class_a))
# print("Class B Std Dev:", np.std(class_b))

import pandas as pd

# data = {
#     "Name": ["Ali", " " ,"Ahmed", "Ayesha"],
#     "Age": [20, 22, 21, 23],
#     "Marks": [90, 85, 78, 92]
# }

# df = pd.DataFrame(data)
# print(df)
# print(df.head())     # Pehli 5 rows dikhao
# print(df.shape)      # Kitni rows, kitne columns?
# print(df.info())

import pandas as pd
# import numpy as np

# data = {
#     "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"],
#     "Age": [20, None, 21, 23, None],
#     "Marks": [90, 85, None, 92, 78]
# }

# df = pd.DataFrame(data)
# df["Age"].fillna(df["Age"].mean(), inplace=True)

# print(df)
# print(df.isnull().sum())


data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"],
    "Age": [20, None, 21, 23, None],
    "Marks": [90, 85, None, 92, 78]
}

df = pd.DataFrame(data)

df["Age"].fillna(df["Age"].mean(),inplace=True)
df["Marks"].fillna(df["Marks"].median(),inplace=True)

print(df)
print(df.isnull().sum())
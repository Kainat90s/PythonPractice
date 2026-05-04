class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
      
    def show_data(self):
        print(f"{self.name}->{self.age}->{self.marks}")
        
        
def data_loader(filename):
    student=[]
    try:
      with open(filename,"r")as f:
        for h in f:
         name,age,marks= h.strip().split(",")
         s=Student(name,int(age),int(marks))
         student.append(s)
    except FileNotFoundError:
        print("file not found")   

def save_data(filname,student):
   
    with open(filname,"w")as f:
        for s in student:
         f.write({s.name},{s.age},{s.marks})
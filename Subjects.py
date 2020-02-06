class student:
    
    def __init__(self,name,rollno,DM,WP,OOPs):
        #Student and subject declaration
        self.name=name
        self.rollno=rollno
        self.DM=DM
        self.WP=WP
        self.OOPs=OOPs

    def display(self):
        #Display output function
        print("name: ",self.name)
        print("rollno: ",self.rollno)
        print("marks of DM: ",self.DM)
        print("marks of WP: ",self.WP)
        print("marks of OOPs: ",self.OOPs)

    def final_result(self,DM,WP,OOPs):
        #Calculations
        self.tot=DM+WP+OOPs                 #Subject Total
        self.res=100*(self.tot/300)         #Subject Percentage
        print("total marks is: ",self.tot)
        print("total percent is: ",self.res)
        if(self.res>=75):
            print("the grade obtained is:A")
        elif(self.res>=50):
            print("the grade obtained is:B")
        elif(self.res>=75):
            print("the grade obtained is:C")
        else:
            print("the grade obtained is:F")
            
            
            


    
#Taking input
name=input("Please enter your name: ")
rollno=int(input("Please enter your roll no.: "))
DM=float(input("Please enter your marks of DM.: "))
WP=float(input("Please enter your marks of WP.: "))
OOPs=float(input("Please enter your marks of OOPs.: "))

#Calling functions
S1=student(name,rollno,DM,WP,OOPs)
S1.display()
S1.final_result(DM,WP,OOPs)     

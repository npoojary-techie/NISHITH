#Passing instance as argument

class demo:
    
    a=0 #Variable 'a' declaration.
    b=0 #Variable 'b' declaration.
    
    def __init__(self):
        
        #Initialising a and b.
        self.a=5
        self.b=10
        
    def display(self):

        #Display function for first demonstration.
        print("a=",self.a)
        print("b=",self.b)
              
class demo1:
              
    x=0
    y=0
              
    def data(self,demo):

        #Initialising x and y.     
        self.x=demo.a
        self.y=demo.b
              
    def display(self):
        
        #Display function for second demonstration.
        print("x=",self.x)
        print("y=",self.y)

#Function calling.
d1=demo()
d1.display()
d2=demo1()
d2.data(d1)
d2.display()

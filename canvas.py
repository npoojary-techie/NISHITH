from tkinter import *
root=Tk()
root.title("AJAY MISHRA")
canvas_width=500
canvas_height=500
c=Canvas(root,width=canvas_width,height=canvas_height,bg="green")
c.pack()
y=int(canvas_height/2)
c.create_line(10,y,canvas_width,y,fill="blue")
coord=10,50,240,210
arc=c.create_arc(coord,start=90,extent=190,fill="red")
oval=c.create_oval(50,60,100,100)
w=root.winfo_screenwidth()
h=root.winfo_screenheight()
print("screen width: ",w)
print("screen height: ",h)
root.geometry("300x150+50+50")
root.mainloop()


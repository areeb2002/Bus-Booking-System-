from tkinter import *
from tkinter import messagebox
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 0, columnspan = 3)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

detail = Label(root, text = "Add New Details to Database", fg ="green", font = 'Arian 14 bold')
detail.grid(row = 6, column = 0, columnspan = 3)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)

def newoperator():
    root.destroy()
    import add_bus_operator

def newbus():
    root.destroy()
    import add_bus_details

def newroute():
    root.destroy()
    import add_bus_route
def newrun():
    root.destroy()
    import add_bus_run
def fun():
    root.destroy()
    import home_page

operator_but= Button(root, text ="New Operator", bg = "lightgreen",command=newoperator)
operator_but.grid(row= 9, column=0)

bus_but= Button(root, text ="New Bus", bg = "orange",command=newbus)
bus_but.grid(row= 9, column=1)

route_but= Button(root, text ="New Route", bg = "lightblue",command=newroute)
route_but.grid(row= 9, column=2)

run_but= Button(root, text ="New Run", bg = "lightpink",command=newrun)
run_but.grid(row= 9, column=3)

blank = Label(root, text = "                            " )
blank.grid(row = 13, column = 0)

blank = Label(root, text = "                            " )
blank.grid(row = 14, column = 0)

house = PhotoImage(file = ".\\home.png")
house_but = Button(root, image=house,command=fun)
house_but.grid(row = 15, column = 3)

root.mainloop()
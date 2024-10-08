from tkinter import *
from tkinter import messagebox
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 10, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 0, columnspan = 10)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

title = Label(root, text = "Add Bus Route Details" , fg = 'green' , font = 'Arian 14 bold')
title.grid(row = 6, column = 0, columnspan = 10)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 9, column = 0)

route_text = Label(root, text = "Route Id")
route_text.grid(row=10, column=0)

route_ent = Entry(root)
route_ent.grid(row=10, column=1)
route_id=route_ent.get()

stname_text = Label(root, text = "Station name")
stname_text.grid(row=10, column=2)

stname_ent = Entry(root)
stname_ent.grid(row=10, column=3)
stname = stname_ent.get()


stid_text = Label(root, text = "Station ID")
stid_text.grid(row=10, column=4)

stid_ent = Entry(root)
stid_ent.grid(row=10, column=5)
stid=stid_ent.get()

import sqlite3
with sqlite3.connect('database.db') as bus:
    cur = bus.cursor()

def add_busroute():
    route_id=route_ent.get()
    stname = stname_ent.get()
    stid=stid_ent.get()
    if(route_id=='' or stname=='' or stid==''):
        messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
    else:
        cur.execute('''insert into route(route_id,station_name,station_id) values(?,?,?)''',(route_id,stname,stid))
        bus.commit()
        messagebox.showinfo('BUS ENTRY','BUS ADDED SUCCESFULLY')

def del_busroute():
    route_id=route_ent.get()
    stname = stname_ent.get()
    stid=stid_ent.get()
    if(route_id=='' or stname=='' or stid==''):
        messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
    else:
        
        cur.execute('''delete from route where route_id=? and station_id=?''',(route_id,stid))
        bus.commit()
        messagebox.showinfo('BUS DELETE','BUS DELETION SUCCESFULL')


def text():
    Label(root,text=" "+route_ent.get()+"  "+stname_ent.get()+"  "+stid_ent.get()).grid(row=11,column=4)



add_but = Button(root, text = "Add Route", bg ="lightgreen",command=lambda:[add_busroute(),text()])
add_but.grid(row = 10, column = 7)

edit_but = Button(root, text = "Delete Route", fg = "red", bg = "lightgreen",command=del_busroute)
edit_but.grid(row = 10, column = 8)

blank = Label(root, text = "                            " )
blank.grid(row = 11, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 12, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 13, column = 0)

def home():
    root.destroy()
    import home_page

house = PhotoImage(file = ".\\home.png")
house_but = Button(root, image=house,command=home)
house_but.grid(row = 14, column = 6)

root.mainloop()
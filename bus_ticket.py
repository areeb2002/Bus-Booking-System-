from tkinter import *
from tkinter import messagebox
from seatbooking import *
root = Tk()
h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
def fun(e=0):
    root.destroy()
    import home_page
house = PhotoImage(file = ".\\home.png")
house_but = Button(root, image=house,command=fun)
house_but.grid(row = 14, column =1 )              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 1, columnspan = 3, padx = w//3)
blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)
title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 1, columnspan = 3, padx = w//3)
blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)
ticket_text = Label(root, text ="Bus Ticket")
ticket_text.grid(row = 6, column=1, columnspan=3)
final = LabelFrame(root)
final.grid(row = 7, column =1, columnspan=3)
passenger_text = Label(final, text = "Passenger: ")
passenger_text.grid(row =8, column=0)
seats_text = Label(final, text = "No of seats: ")
seats_text.grid(row =10, column=0)
age_text = Label(final, text = "Age: ")
age_text.grid(row =12, column=0, columnspan=2)
travel_text = Label(final, text = "Travel On: ")
travel_text.grid(row =14, column=0)
seats_text = Label(final, text = "No of Seats: ")
seats_text.grid(row =16, column=0)
g_text = Label(final, text = "Gender: ")
g_text.grid(row =8, column=2)
phone_text = Label(final, text = "Phone: ")
phone_text.grid(row =10, column=2)
flare_text = Label(final, text = "Fare Rs: ")
flare_text.grid(row =12, column=2)
detail_text = Label(final, text = "Bus Detail: ")
detail_text.grid(row =14, column=2)
booked_text = Label(final, text = "Booked On: ")
booked_text.grid(row =16, column=2)
point_text = Label(final, text = "Boarding Point: ")
point_text.grid(row =18, column=2)
import sqlite3
with sqlite3.connect('database.db') as con:
    cur = con.cursor()
booked_bus_id=rv1.get()
cur.execute('''select max(passenger_id) from passenger''')
a=cur.fetchone()
maxid = a[0]
cur.execute('''select fare from bus where bus_id=?''',[booked_bus_id])
m=cur.fetchone()
Fare = m[0]
cur.execute('''select no_of_seats from passenger where passenger_id=?''',[maxid])
k=cur.fetchone()
seats=k[0]
totalfare = str(Fare*seats)
cur.execute('''select name,gender,no_of_seats,mob_no,age,travelling_date,booking_date,source from passenger,ticket where passenger_id=? ''',[maxid])
res = cur.fetchall()
for i in res:
    Label(final,text = i[0]).grid(row=8,column = 1)
    Label(final,text = i[1]).grid(row=8,column = 3)
    Label(final,text = i[2]).grid(row=10,column = 1)
    Label(final,text = i[3]).grid(row=10,column = 3)
    Label(final,text = i[4]).grid(row=12,column = 1)
    Label(final,text = i[5]).grid(row=14,column = 1)
    Label(final,text = i[6]).grid(row=16,column = 3)
    Label(final,text = i[7]).grid(row=18,column = 3)
    Label(final,text = i[2]).grid(row=16,column = 1)

cur.execute('''select name from bus as a,bus_operator as b where a.op_id = b.op_id and bus_id=? ''',(booked_bus_id) )
temp = cur.fetchall()
for i in temp:
    Label(final,text = i[0]).grid(row=14,column = 3)
cur.execute('''select bus_id from passenger where passenger_id=?''',[maxid])
z=cur.fetchone()
busid = z[0]
cur.execute('''select no_of_seats from passenger where passenger_id=?''',[maxid])
p=cur.fetchone()
booked_seats = p[0]
cur.execute('''select availaible_seats from bus where bus_id=?''',[busid])
w=cur.fetchone()
availaibleseats = w[0]
updated_seats = availaibleseats - booked_seats
cur.execute('''update bus set availaible_seats =? where bus_id=?''',(updated_seats,busid))
con.commit()
str(updated_seats)    
Label(final,text = ''+totalfare).grid(row=12,column = 3)
last_text = Label(final, text = "Total amount Rs  "+totalfare+ "  to be paid at the time of boarding the bus")
last_text.grid(row =20, column=0)
root.mainloop()
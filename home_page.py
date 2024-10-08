from tkinter import *
root = Tk()

h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))

def seatbooking():
    root.destroy()
    import bus_ticket

def checkbooked():
    root.destroy()
    import check_booking

def adddetails():
    root.destroy()
    import add_details


bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 25 bold')
title.grid(row = 2, column = 0, columnspan = 3, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 4, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

seat_booking = Button(root, text ="Seat Booking " , fg = 'blue', bg ='lightgreen',command=seatbooking,font = 'Arian 15 ')
seat_booking.grid(row = 6, column = 0)

check_booked_seat = Button(root, text ="Check Booked Seat" , fg = 'blue', bg ='lightgreen',command=checkbooked,font = 'Arian 15 ')
check_booked_seat.grid(row = 6, column = 1)

add_bus = Button(root, text ="Add Bus Details" , fg = 'blue', bg ='darkgreen',command=adddetails,font = 'Arian 15 ')
add_bus.grid(row = 6, column = 2)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)
blank = Label(root, text = "                            " )
blank.grid(row = 8, column = 0)

admin = Label(root, text = "For Admin Only", fg = 'red')
admin.grid(row = 9, column =2)



root.mainloop()
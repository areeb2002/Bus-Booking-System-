from tkinter import *
from tkinter import messagebox
root = Tk()
h,w = root.winfo_screenheight(), root.winfo_screenwidth()
root.geometry('%dx%d+0+0'%(w,h))
clicked = StringVar()
clicked.set("Male")
def book():
    booked_bus_id=rv1.get()
    print(booked_bus_id)
    if booked_bus_id=='None':
        messagebox.showwarning("Warning", "Please select a bus")
    else:
        blank = Label(root, text = "                            " )
        blank.grid(row = 11, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 12, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 13, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 14, column = 0)
        fill_label = Label(root, text = "Fill Passenger Details to book the bus ticket" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
        fill_label.grid(row = 15, column = 0, columnspan = 8)
        blank = Label(root, text = "                            " )
        blank.grid(row = 16, column = 0)
        name_text = Label(root, text = "Name")
        name_text.grid(row = 17, column=0)
        name_ent = Entry(root)
        name_ent.grid(row =17, column=1)
        name = name_ent.get()
        gender_text = Label(root, text = "Gender")
        gender_text.grid(row = 17, column=2)
        gender_drop = OptionMenu(root, clicked , "Male", "Female", "Third Gender")
        gender_drop.grid(row = 17, column = 3)
        gender = clicked.get()
        seats_text = Label(root, text = "No of Seats")
        seats_text.grid(row = 17, column=4)
        seats_ent = Entry(root)
        seats_ent.grid(row =17, column=5)
        Capacity = seats_ent.get()
        mobile_text = Label(root, text = "Mobile No")
        mobile_text.grid(row = 17, column=6)
        mobile_ent = Entry(root)
        mobile_ent.grid(row =17, column=7)
        phone = mobile_ent.get()
        age_text = Label(root, text = "Age")
        age_text.grid(row = 17, column=8)
        age_ent = Entry(root)
        age_ent.grid(row =17, column=9)
        age = age_ent.get()
    def book_seat():
        phone = mobile_ent.get()
        Capacity = seats_ent.get()
        import sqlite3
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
        booked_bus_id=rv1.get()
        if(len(phone)!=10):
            messagebox.showwarning("Warning", "Please Enter Valid 10 digit Mobile NO.")
        age = age_ent.get()
        if(int(age)<1 or int(age)>120):
            
            messagebox.showwarning("Warning", "Please Enter Valid age.")
        cur.execute('''select availaible_seats from bus where bus_id=?''',[booked_bus_id])
        i= cur.fetchone()
        compare = i[0]
        if(int(Capacity)>compare):
            messagebox.showwarning("Warning", "Tickets can't be booked since no. of seats entered is greater tha availaible seats")
        else:
            answer = messagebox.askyesno("bus confirmation", "Are you sure you want to book the bus?")
            if answer:
                age = age_ent.get()
                phone = mobile_ent.get()
                Capacity = seats_ent.get()
                gender = clicked.get()
                name = name_ent.get()
                travel_date=ent_date.get()
                booked_bus_id=rv1.get()
                To=ent_To.get()
                From=ent_From.get() 
                import sqlite3
                with sqlite3.connect('database.db') as con:
                    cur = con.cursor()
                cur.execute('''insert into passenger(name,gender,no_of_seats,mob_no,age,travelling_date,booking_date,bus_id) values(?,?,?,?,?,?,DATE(),?)''',[name,gender,Capacity,phone,age,travel_date,booked_bus_id])
                cur.execute('''insert into ticket(source,destination,rv1,mobile) values(?,?,?,?)''',(To,From,booked_bus_id,phone))
        
                con.commit()
                root.destroy()
    book_button = Button(root, text = "Book Seat", bg ="lightgreen", command = book_seat)
    book_button.grid(row = 17, column=10)
def show():
    select_text = Label(root, text = "Select Bus", fg = "green")
    select_text.grid(row = 8, column=0)

    opt_text = Label(root, text = "Operator", fg = "green")
    opt_text.grid(row = 8, column=1)

    type_text = Label(root, text = "Bus Type", fg = "green")
    type_text.grid(row = 8, column=2)

    available_text = Label(root, text = "Available/Capacity", fg = "green")
    available_text.grid(row = 8, column=3)

    fare_text = Label(root, text = "Fare", fg = "green")
    fare_text.grid(row = 8, column=4)
    
    
    blank = Label(root, text = "                            " )
    blank.grid(row = 9, column = 0)

    import sqlite3
    with sqlite3.connect('database.db') as con:
        cur = con.cursor()
    To=ent_To.get() 
    From=ent_From.get() 
    Date=ent_date.get()
    if(To=='' or From=='' or Date==''):
        messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
    elif(Date!='2022-12-01' and Date!='2022-12-02' and Date!='2022-12-03' and Date!='2022-12-04' ):
        messagebox.showinfo("BUS ", "BUS NOT AVAILAIBLE ON THIS DATE")   
    elif((To=='Kota' or To=='Leh' or To=='Manali' or To=='Udaipur') and (From=='Jaipur' or From=='Manali' or From=='Delhi')) :
        To=ent_To.get()
        From=ent_From.get() 
        Date=ent_date.get()
        cur.execute('''Select name,bus_type,capacity,fare,bus_id,availaible_seats from bus as a,bus_operator as b,route as f, route as t where f.station_name=? and t.station_name=? and f.station_id<t.station_id and f.route_id=t.route_id and t.route_id=f.route_id and a.op_id=b.op_id''',(From,To))
        res=cur.fetchall()
        num=10
        for i in res:   
            r1=Radiobutton(root,variable=rv1,value=i[4])
            r1.grid(row=num,column=0)
            operator1=Label(root, text = i[0], fg = "blue1")
            operator1.grid(row = num, column=1)
            operator=Label(root, text = i[1], fg = "blue1")
            operator.grid(row = num, column=2)
            b_type=Label(root, text = str(i[5])+'/'+str(i[2]), fg = "blue1")
            b_type.grid(row = num, column=3)
            seat=Label(root, text = i[3], fg = "blue1")
            seat.grid(row = num, column=4)
            num=num+1
        booked_bus_id=rv1.get()
        con.commit()
        book_button = Button(root, text="Proceed to Book", bg = "lightgreen", command = book)
        book_button.grid(row =10 , column= 6, columnspan=2)
    
    else:
        messagebox.showwarning("BUS", "BUS NOT AVAILAIBLE ON THIS ROUTE")
        

        
        











    
    
rv1=StringVar()
rv1.set(None)
mobile_ent = IntVar()


              
bus = PhotoImage(file = ".\\Bus_for_project.png")
Label(root, image = bus).grid(row = 0, column = 0, columnspan = 8, padx = w//3)

blank = Label(root, text = "                            " )
blank.grid(row = 1, column = 1)

title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'Arian 14 bold')
title.grid(row = 2, column = 0, columnspan = 8)

blank = Label(root, text = "                            " )
blank.grid(row = 3, column = 0)

title1 =Label(root, text = "Enter Journey Details", bg="lightgreen", fg = "darkgreen", font = "Arian 14 bold" )
title1.grid(row=4, column = 0, columnspan =8 )


blank = Label(root, text = "                            " )
blank.grid(row = 5, column = 0)

To_text = Label(root, text = "To")
To_text.grid(row = 6, column =0)


ent_To = Entry(root, width=20)
ent_To.grid(row = 6, column =1)



From_text = Label(root, text = "From")
From_text.grid(row = 6, column =2)

ent_From = Entry(root, width=20)
ent_From.grid(row = 6, column =3)

date_text = Label(root, text = "Journey Date(YYYY-MM-DD)")
date_text.grid(row = 6, column =4)

ent_date = Entry(root,text='a', width=20)
ent_date.grid(row = 6, column =5)
travel_date=ent_date.get()




show_button = Button(root, text = "Show Bus", fg = "blue", bg ="green", command = show)
show_button.grid(row = 6, column =6)

def home():
    root.destroy()
    import home_page

house = PhotoImage(file = ".\\home.png")
home_button = Button(root, image = house,command=home)
home_button.grid(row =6 , column= 7)

blank = Label(root, text = "                            " )
blank.grid(row = 7, column = 0)























root.mainloop()






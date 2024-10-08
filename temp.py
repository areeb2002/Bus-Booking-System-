from tkinter import *
from tkinter import messagebox

import sqlite3
with sqlite3.connect('database.db') as con:
    cur=con.cursor()

cur.execute(''' update route set station_name="Udaipur" where route_id=2 and station_id=3;''',)
con.commit()


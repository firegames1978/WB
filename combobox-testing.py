from tkinter import *
import tkinter.messagebox
import random
import sqlite3
from tkinter import ttk
import json

root = Tk()
        
root.geometry("600x250+250+250")

connection = sqlite3.connect("WeighBridgeMaster.db")
cursor = connection.cursor()
#Transproter Table Call
cursor.execute("SELECT oid, Trn_Id, TransporterName FROM TRNSMASTER")
records = cursor.fetchall()

# Transport_string = ''' {"transporter": 
#             [
#                 {
#                     "ID": "KGN",
#                     "NAME": "KHUWJA GARIB NAWAZ",
#                     "CITY": "AJMER"
#                 },
#                 {
#                     "ID": "TK",
#                     "NAME": "TARIQ KHAN",
#                     "CITY": "CHITTORGARH"
#                 },
#                 {
#                     "ID": "SH",
#                     "NAME": "SHARIQ HUSSAIN",
#                     "CITY": "HYDERABAD"
#                 }
#             ]
#             }'''

# data = json.loads(Transport_string)

# for trans in data['transporter']:
#     print(trans['ID']+trans['NAME'])
    

global clicked
clicked = StringVar()

for record in records:
    clicked.set(record[0])
    
print(records)

def FGcomboclick(*args):
    # print(record[FG_combo.current()])
    global clicked
    Trn_Label2 = Label(root, text=clicked.get())
    Trn_Label2.grid(row=1, column=1, ipadx=30, ipady=5)
    
    Trn_Label4 = Label(root, text=FG_combo.current())
    # Trn_Label4 = Label(root, text=trans['NAME'])
    Trn_Label4.grid(row=2, column=1, ipadx=30, ipady=5)

Trn_Label = Label(root, text="Please select Transporter : ", bg="powder blue", font=("Times new roman",10,"bold"))
Trn_Label.grid(row=0, column=0, ipadx=30, ipady=5)

# FG_combo = ttk.Combobox(root, values=data['transporter'], justify="center")

FG_combo = ttk.Combobox(root, values=records, justify="center", textvariable=clicked)
FG_combo.current()
FG_combo.bind("<<ComboboxSelected>>", FGcomboclick)
FG_combo.grid(row=0, column=1, ipadx=30, ipady=5)

    # var_material = tk.StringVar()
    # combo_material = ttk.Combobox(root, values=list(materialDict.keys()), justify="center", textvariable=var_material)
    # combo_material.bind('<<ComboboxSelected>>', lambda event: label_selected.config(text=materialDict[var_material.get()]))

Trn_Label1 = Label(root, text="Transporter Code : ", bg="powder blue", font=("Times new roman",10,"bold"))
Trn_Label1.grid(row=1, column=0, ipadx=30, ipady=5)

Trn_Label2 = Label(root, text=" ", font=("Times new roman",10,"bold"))
Trn_Label2.grid(row=1, column=1, ipadx=30, ipady=5)

Trn_Label3 = Label(root, text="Transporter Name : ", bg="powder blue", font=("Times new roman",10,"bold"))
Trn_Label3.grid(row=2, column=0, ipadx=30, ipady=5)

Trn_Label4 = Label(root, text=" ", font=("Times new roman",10,"bold"))
Trn_Label4.grid(row=2, column=1, ipadx=30, ipady=5)


connection.commit()
connection.close()

Trn_Label5 = Label(root, text="GATE PASS No", bg="powder blue", font=("Times new roman",10,"bold"))
Trn_Label5.grid(row=3, column=0, ipadx=30, ipady=5)

trn_IW_Gateno_entry = Entry(root, width=30, bg='burlywood1', font=10)
trn_IW_Gateno_entry.grid(row=3, column=1, ipadx=30, ipady=5)

Trn_Label6 = Label(root, text="TRUCK No", bg="powder blue", font=("Times new roman",10,"bold"))
Trn_Label6.grid(row=4, column=0, ipadx=30, ipady=5)

trn_IW_Truckno_entry = Entry(root, width=30, bg='burlywood1', font=10)
trn_IW_Truckno_entry.grid(row=4, column=1, ipadx=30, ipady=5)



root.mainloop()
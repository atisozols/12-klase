from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import sqlite3

edit = False
edit_id = 0

# Create table
conn = sqlite3.connect("datasheet.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS datasheet (id INTEGER PRIMARY KEY, type VARCHAR, model VARCHAR, price FLOAT)")
conn.commit()

# Display data in Tree widget
def display():
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM datasheet")
    parts = cursor.fetchall()
    
    for part in parts:
        tree.insert('', 'end', text="2", values=(part[0], part[1], part[2], part[3]))
        

# Submit
def submit():
    cursor = conn.cursor()
    if type.get() != "" and name.get() != "" and price.get() != "":
        cursor.execute("INSERT INTO datasheet (type, model, price) VALUES (?, ?, ?)", (type.get(), name.get(), float(price.get())))
    else:
        messagebox.showinfo("Error", "Lūdzu, ievadiet vērtības!")
    type.delete(0, len(type.get()))
    name.delete(0, END)
    price.delete(0, END)
    conn.commit()
    display()

# Delete item
def delete():
    treeIndex = tree.focus()
    if treeIndex:
        id = tree.item(treeIndex)["values"][0] # focus atgriež indeksu, kuru izmanto, lai dabūtu konkrēto item
        print(treeIndex, id)
        cursor.execute("DELETE FROM datasheet WHERE id = ?", str(id))
        conn.commit()
        display()
    else:
        messagebox.showinfo("Error", "Lūdzu, izvēlieties ierakstu!")

def update():
    global edit
    global edit_id
    
    if not edit:
        treeIndex = tree.focus()
        if treeIndex:
            edit_id = tree.item(treeIndex)["values"][0] # focus atgriež indeksu, kuru izmanto, lai dabūtu konkrēto item
            cursor.execute("SELECT * FROM datasheet WHERE id = " + str(edit_id))
            part = cursor.fetchone()
            
            type.insert(0, part[1])
            name.insert(0, part[2])
            price.insert(0, part[3])
            edit = True
        else:
            messagebox.showinfo("Error", "Lūdzu, izvēlieties ierakstu!")
    else:
        if type.get() != "" and name.get() != "" and price.get() != "":
            cursor.execute("UPDATE datasheet SET type = ?, model = ?, price = ? WHERE id = ?", (type.get(), name.get(), float(price.get()), str(edit_id)))
            conn.commit()
            type.delete(0, END)
            name.delete(0, END)
            price.delete(0, END)
            display()
            edit = False
            
def printFile():
    treeIndex = tree.focus()
    if treeIndex:
        edit_id = tree.item(treeIndex)["values"][0] # focus atgriež indeksu, kuru izmanto, lai dabūtu konkrēto item
        cursor.execute("SELECT * FROM datasheet WHERE id = " + str(edit_id))
        part = cursor.fetchone()
        print(part)
        
        with open("sastavdala" + str(part[0]) + ".txt", "w") as f:
            f.write("-Datora sastavdala-\n")
            f.write("Veids:" + part[1] + "\n")
            f.write("Modelis:" + part[2] + "\n")
            f.write("Cena:" + str(part[3]) + "\n")
    else:
        messagebox.showinfo("Error", "Lūdzu, izvēlieties ierakstu!")


# Window configuration
window = Tk()

window.geometry("800x400")
window.title("Datora sastavdalas")
window.config(background="white")

# Title
name = Label(window,
             font=("Visby",20, "bold"),
             text="Datora sastāvdaļas",
             background="#94a0a8",
             relief=FLAT)

name.place(x=10, y =10)

# Entry Boxes
type = Entry(window,
             font=("Visby",20),
             fg="Black",
             background="white")

type.place(x=10, y=60)

name = Entry(window,
             font=("Visby",20),
             fg="Black",
             background="white")

name.place(x=10, y=100)

price = Entry(window,
             font=("Visby",20),
             fg="Black",
             background="white")

price.place(x=10, y=140)

# Submit Button
submitb = Button(window,
                font=("Visby",13, "bold"),
                text="submit",
                background="#94a0a8",
                activebackground="#94a0a8",
                command=submit)

submitb.place(x=330, y= 140)

printb = Button(window,
                font=("Visby",13, "bold"),
                text="to file",
                background="#fca1ff",
                activebackground="#fca1ff",
                command=printFile)

printb.place(x=650, y= 140)

tree = ttk.Treeview(window, column=("c1", "c2", "c3", "c4"), show='headings', height=8)

tree.column("# 1", anchor=CENTER)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER)
tree.heading("# 2", text="Type")
tree.column("# 3", anchor=CENTER)
tree.heading("# 3", text="Name")
tree.column("# 4", anchor=CENTER)
tree.heading("# 4", text="Price")

tree.pack(side=BOTTOM)

# Delete button from list
ldelete = Button(window,
                 font=("Visby",13, "bold"),
                 text="delete",
                 background="Red",
                 activebackground="Red",
                 command=delete)

ldelete.place(x=450,y=140)

edit = Button(window,
                 font=("Visby",13, "bold"),
                 text="edit",
                 background="White",
                 activebackground="White",
                 command=update)

edit.place(x=550,y=140)


# Program executer
edit = False
edit_id = 0
display()
window.mainloop()
conn.close()
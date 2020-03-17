# Tkinter is Python's de-facto standard GUI (Graphical User Interface) package.
# "*" means everything.so we import everything from the tkinter package.
from tkinter import *
from tkinter import messagebox
from db import Database

db = Database('store.db')

# Functions


def populate_list():
    # used so that when the populate_list fnc is called,its doesnt repeat the same data again.
    stocks_list.delete(0, END)
    for row in db.fetch():
        # used to loop through the data stored in db.
        stocks_list.insert(END, row)


def add_item():
    if stock_text.get() == '' or transtype_text.get() == '' or number_text.get() == '' or price_text.get() == '':
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    # to get the input data of the form fields and insert in db but not in the list table.
    db.insert(stock_text.get(), transtype_text.get(),
              number_text.get(), price_text.get())
    stocks_list.delete(0, END)  # delete stuff from list
    stocks_list.insert(END, (stock_text.get(), transtype_text.get(), number_text.get(
    ), price_text.get()))  # inserts the inputs in database in the list table
    clear_text()
    populate_list()

# to select list item


def select_item(event):  # we bind listtable to this function
    try:
        global selected_item  # we use global so that we can use the variable later
        index = stocks_list.curselection()[0]  # to get the index
        selected_item = stocks_list.get(index)
        # print(selected_item)
        # till here,on selecting the list-item we get the data value of that selected item.

        # to insert the selected item in the input fields
        stock_entry.delete(0, END)
        stock_entry.insert(END, selected_item[1])
        transtype_entry.delete(0, END)
        transtype_entry.insert(END, selected_item[2])
        number_entry.delete(0, END)
        number_entry.insert(END, selected_item[3])
        price_entry.delete(0, END)
        price_entry.insert(END, selected_item[4])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], stock_text.get(
    ), transtype_text.get(), number_text.get(), price_text.get())
    populate_list()


def clear_text():
    stock_entry.delete(0, END)
    transtype_entry.delete(0, END)
    number_entry.delete(0, END)
    price_entry.delete(0, END)


# Creating the Window Object i.e. the basic structure of the window on which we will build our app on.
app = Tk()


# Stock
stock_text = StringVar()  # declaring a variable
# creating the label tag.first being the tk method(here its app),the text value to be shown,styles like font and padding.pady means padding along y-axis.
stock_label = Label(app, text='Stock Name', font=('bold', 10), pady=20)
# we can use 'Label()' and 'StringVar()' because we have imported tkinter.
stock_label.grid(row=0, column=0, sticky=W)  # uses the python grid system.
# sticky means aligning which takes in W/E which refers to West/East resp.
stock_entry = Entry(app, textvariable=stock_text)
# entry is for the input whose value is bound by the variable 'stock_text' which takes in a 'stringvar' datatype
stock_entry.grid(row=0, column=1)

# Transaction type
transtype_text = StringVar()
transtype_label = Label(
    app, text='Transaction(Sold/Bought):', font=('bold', 10))
transtype_label.grid(row=0, column=2, sticky=W)
transtype_entry = Entry(app, textvariable=transtype_text)
transtype_entry.grid(row=0, column=3)

# Number Of Shares
number_text = StringVar()
number_label = Label(app, text='Number of Shares:', font=('bold', 10))
number_label.grid(row=1, column=0, sticky=W)
number_entry = Entry(app, textvariable=number_text)
number_entry.grid(row=1, column=1)

# Price per Share
price_text = StringVar()
price_label = Label(app, text='Price per Share:', font=('bold', 10))
price_label.grid(row=1, column=2, sticky=W)
price_entry = Entry(app, textvariable=price_text)
price_entry.grid(row=1, column=3)

# Stocks Lists(ListTable)
stocks_list = Listbox(app, height=8, width=50, border=0)
stocks_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# ScrollBar
# Create Scroll Bar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scrollbar to List
stocks_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=stocks_list.yview)
# Bind select
stocks_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Add Stock', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20, padx=20)

remove_btn = Button(app, text='Remove Stock',
                    width=12, command=remove_item)
remove_btn.grid(row=2, column=1, padx=10)

update_btn = Button(app, text='Update Stock',
                    width=12, command=update_item)
update_btn.grid(row=2, column=3)

clear_btn = Button(app, text='Clear Input', width=12, command=clear_text)
clear_btn.grid(row=2, column=2, padx=10)

# to change the title of the window
app.title('Stock Manager')
# to change the dimensions of the window
app.geometry('550x400')

# Populate Data
populate_list()

# Start program
app.mainloop()

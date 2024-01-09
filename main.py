from tkinter import *
from tkinter import messagebox, Text
from Controller import BTreeController

def display_text(data_list):
    text_display.delete('1.0', END)
    formatted_text = ""
    for item in data_list:
        formatted_text += f"{item[0]} : {item[1]}\n"
    text_display.insert("1.0", formatted_text)

def get_entries_values():
    return key_entry.get(), value_entry.get()

def insert_btn_active():
    key, value = get_entries_values()
    if not key.isdigit() or not value:
        error_msg = "Incorrect data"
        messagebox.showerror("Error", error_msg)
        return
    key = int(key)
    if not controller.insert((key, value)):
        error_msg = "Key exist"
        messagebox.showerror("Error", error_msg)
    display_text(controller.get_current_data())

def search_btn_active():
    key, value = get_entries_values()
    if not key.isdigit():
        error_msg = "Incorrect data"
        messagebox.showerror("Error", error_msg)
        return
    key = int(key)
    result, comp = controller.search(key)
    if not result:
        error_msg = "Key does not exist!"
        messagebox.showerror("Error", error_msg)
    else:
        msg = f"Found Key:{key} : Value:{result} in {comp} comparisons"
        messagebox.showinfo("Success", msg)

def delete_btn_active():
    key, value = get_entries_values()
    if not key.isdigit():
        error_msg = "Incorrect data"
        messagebox.showerror("Error", error_msg)
        return
    key = int(key)
    if not controller.delete(key):
        error_msg = "Key does not exist!"
        messagebox.showerror("Error", error_msg)
    display_text(controller.get_current_data())

def update_btn_active():
    key, value = get_entries_values()
    if not key.isdigit():
        error_msg = "Incorrect data"
        messagebox.showerror("Error", error_msg)
        return
    key = int(key)
    if not controller.update(key, value):
        error_msg = "Key does not exist!"
        messagebox.showerror("Error", error_msg)
    display_text(controller.get_current_data())

def save_btn_active():
    controller.save_data_to_file()

def load_btn_active():
    global controller
    controller = BTreeController(50)
    controller.load_data_from_file()
    controller.save_data()
    display_text(controller.get_current_data())

def generate_btn_active():
    global controller
    controller = BTreeController(50)
    controller.generate_random_data()
    controller.save_data()
    display_text(controller.get_current_data())

window = Tk()
window.title("BTree (t = 50)")

key_entry = Entry(window, width=11, font=("Arial", 15))
value_entry = Entry(window, width=11, font=("Arial", 15))

key_label = Label(window, text="Key: ", font=('Arial', 15, 'bold'))
value_label = Label(window, text="Value: ", font=('Arial', 15, 'bold'))

key_label.grid(row=0, column=0, padx=5, pady=10)
key_entry.grid(row=0, column=1, padx=0, pady=10)
value_label.grid(row=0, column=2, padx=5, pady=10)
value_entry.grid(row=0, column=3, padx=0, pady=10)

buttons_frame = Frame(window)
buttons_frame.grid(row=0, column=4, rowspan=5, padx=5, pady=10)

insert_btn = Button(buttons_frame, text="Insert", font=("Comic Sans", 15), command=insert_btn_active)
search_btn = Button(buttons_frame, text="Search", font=("Comic Sans", 15), command=search_btn_active)
delete_btn = Button(buttons_frame, text="Delete", font=("Comic Sans", 15), command=delete_btn_active)
update_btn = Button(buttons_frame, text="Update", font=("Comic Sans", 15), command=update_btn_active)
save_btn = Button(buttons_frame, text="Save", font=("Comic Sans", 15), command=save_btn_active)
load_btn = Button(buttons_frame, text="Load", font=("Comic Sans", 15), command=load_btn_active)
generate_btn = Button(buttons_frame, text="Generate", font=("Comic Sans", 15), command=generate_btn_active)

insert_btn.grid(row=0, column=0, padx=0, pady=5, sticky="ew")
search_btn.grid(row=1, column=0, padx=0, pady=5, sticky="ew")
delete_btn.grid(row=2, column=0, padx=0, pady=5, sticky="ew")
update_btn.grid(row=3, column=0, padx=0, pady=5, sticky="ew")
save_btn.grid(row=4, column=0, padx=0, pady=5, sticky="ew")
load_btn.grid(row=5, column=0, padx=0, pady=5, sticky="ew")
generate_btn.grid(row=6, column=0, padx=0, pady=5, sticky="ew")

text_display_text = ""

text_display = Text(window, height=20, width=100, font=("Arial", 12))
text_display.insert("1.0", text_display_text)
text_display.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

for col in range(4):
    window.grid_columnconfigure(col, weight=1)

window.grid_rowconfigure(1, weight=1)

controller = BTreeController(50)

window.mainloop()

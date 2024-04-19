from tkinter import *

def add_language():
    language_name = language_input.get().strip()
    if language_name:
        language_list.insert(END, language_name)
        language_input.delete(0, END)

def update_language():
    selected_index = language_list.curselection()
    if selected_index:
        language_name = language_input.get().strip()
        if language_name:
            language_list.delete(selected_index)
            language_list.insert(selected_index, language_name)

def delete_language():
    selected_index = language_list.curselection()
    if selected_index:
        language_list.delete(selected_index)

root = Tk()``
root.title("South African Languages")

language_label = Label(root, text="South African Languages", font=("Arial", 12))
language_label.pack(pady=10)

form_frame = Frame(root)
form_frame.pack()

language_input = Entry(form_frame, width=30)
language_input.grid(row=0, column=0, padx=5)

add_button = Button(form_frame, text="Add", command=add_language)
add_button.grid(row=0, column=1, padx=5)

list_frame = Frame(root)
list_frame.pack(pady=10)

language_list = Listbox(list_frame, width=40)
language_list.pack(side=LEFT, fill=Y)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side=RIGHT, fill=Y)

language_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=language_list.yview)

update_button = Button(root, text="Update", command=update_language)
update_button.pack(pady=5)

delete_button = Button(root, text="Delete", command=delete_language)
delete_button.pack()

root.mainloop()
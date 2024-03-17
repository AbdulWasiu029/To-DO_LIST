import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, f"{len(task_listbox.get('0', tk.END)) + 1}. {task}")
        task_entry.delete(0, tk.END)
        
def update_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        updated_task = task_entry.get() 
        task_listbox.delete(selected_task)
        task_listbox.insert(selected_task, f"{selected_task[0]+1}. {updated_task}")
        task_entry.delete(0, tk.END)
        
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
        for i in range(selected_task[0], task_listbox.size()):
            task_listbox.delete(i)
            task_listbox.insert(tk.END, f"{i+1}. {task_listbox.get(i)}")
    
root = tk.Tk()
root.geometry("1300x700")
root.title("TO-DO LIST")
root.config(bg='LightGray')

title_label = tk.Label(root, text="TO-DO LIST", font=("Arial", 30, "bold"),
                        border=7, relief=tk.GROOVE, bg="DimGray", fg="White")
title_label.pack(side="top", fill="x")

task_frame = tk.Frame(root, border=7, relief=tk.GROOVE, bg="LightGrey")
task_frame.place(x=40, y=90, width=1195, height=580)

aud_frame = tk.Frame(task_frame, border=7, relief=tk.GROOVE, bg="Gainsboro")
aud_frame.place(x=0, y=0, height=70, width=1182)

add_button = tk.Button(aud_frame, text="ADD TASK", font=("Arial", 15, "bold"),
                       bg="LightSkyBlue", relief=tk.GROOVE, bd=7, command=add_task)
add_button.place(x=500, y=0, width=150, height=55)
update_button = tk.Button(aud_frame, text="UPDATE", font=("Arial", 15, "bold"),
                          bg="LightSkyBlue", relief=tk.GROOVE, bd=7, command=update_task)
update_button.place(x=725, y=0, width=150, height=55)
delete_button = tk.Button(aud_frame, text="DELETE", font=("Arial", 15, "bold"),
                          bg="LightSkyBlue", relief=tk.GROOVE, bd=7, command=delete_task)
delete_button.place(x=950, y=0, width=150, height=55)

task_entry = tk.Entry(aud_frame, font=("Arial", 15), bd=7, bg="LightSkyBlue", relief=tk.GROOVE)
task_entry.place(x=60, y=0, width=370, height=55)

scrollbar = tk.Scrollbar(task_frame, orient=tk.VERTICAL)
scrollbar.place(x=1185, y=90, height=460)

task_listbox = tk.Listbox(task_frame, font=("Arial", 15), bg="Gainsboro", bd=5, relief=tk.GROOVE,
                          yscrollcommand=scrollbar.set)
task_listbox.place(x=60, y=90, width=1070, height=460)
scrollbar.config(command=task_listbox.yview)

root.mainloop()
import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_listBox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.delete(selected_task)

def mark_task():
    selected_task = task_listBox.curselection()
    if selected_task:
        task_listBox.itemconfig(selected_task, bg="slate blue")

def save_tasks():
    with open ('tasks.txt', 'w') as file:
        tasks = task_listBox.get(0, tk.END)
        for task in tasks:
            file.write(task + '\n')



root = tk.Tk()
root.title("Задачи на сегодня")
root.configure(background="aquamarine")

text1 = tk.Label(root, text="Введите вашу задачу:", bg="SlateGray1")
text1.pack(pady=5)

task_entry = tk.Entry(root, width=30, bg="snow2")
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Добавить задачу", bg="SlateGray1", command=add_task)
add_task_button.pack(pady=5)

delete_button = tk.Button(root, text="Удалить задачу", bg="SlateGray1", command=delete_task)
delete_button.pack(pady=5)

mark_button = tk.Button(root, text="Отметить выполненную задачу", bg="SlateGray1", command=mark_task)
mark_button.pack(pady=5)

save_button = tk.Button(root, text="Сохранить задачу на завтра", bg="SlateGray1", command=save_tasks)
save_button.pack(pady=5)

text2 = tk.Label(root, text="Список задач:", bg="grey78")
text2.pack(pady=5)

task_listBox = tk.Listbox(root, height=20, width=70, bg="snow2")
task_listBox.pack(pady=10)

root.mainloop()

def area_square_area(a):
    S_s = a ** 2
    return S_s
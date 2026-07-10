import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self):
        if self.head is None:
            return False

        self.head = self.head.next
        return True

    def traverse(self):
        elements = []
        temp = self.head

        while temp:
            elements.append(str(temp.data))
            temp = temp.next

        return " -> ".join(elements) + " -> None" if elements else "Linked List is Empty"


sll = SinglyLinkedList()


def insert_node():
    value = entry.get()

    if value == "":
        messagebox.showerror("Error", "Enter a value")
        return

    sll.insert(int(value))
    entry.delete(0, tk.END)
    display_list()


def delete_node():
    if not sll.delete():
        messagebox.showinfo("Info", "Linked List is Empty")

    display_list()


def display_list():
    output.config(text=sll.traverse())


root = tk.Tk()
root.title("Singly Linked List")
root.geometry("500x300")

title = tk.Label(root, text="Singly Linked List Operations",
                 font=("Arial", 16, "bold"))
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

insert_btn = tk.Button(btn_frame, text="Insert",
                       width=10, command=insert_node)
insert_btn.grid(row=0, column=0, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete",
                       width=10, command=delete_node)
delete_btn.grid(row=0, column=1, padx=5)

display_btn = tk.Button(btn_frame, text="Traverse",
                        width=10, command=display_list)
display_btn.grid(row=0, column=2, padx=5)

output = tk.Label(root, text="Linked List is Empty",
                  font=("Arial", 13), fg="blue")
output.pack(pady=20)

root.mainloop()

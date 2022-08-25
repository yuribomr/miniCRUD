import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
from tkinter.messagebox import showinfo
from tkinter import messagebox as msg

mydb = mysql.connector.connect(
    host="localhost",
    user="Yuri",
    password="yuribr12",
    database="dbpython"
)
cursor = mydb.cursor()


class Person:
    def __init__(self, nome):
        self.nome = nome

    def retornaNome(nome):
        return nome


def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['text']
        nome = item["values"][0]
        res = msg.askyesnocancel(title='Excluir usuario ',
                                 message=f"Tem certeza que deseja excluir o usuario: {nome}")
        if res == 1:
            query = f'DELETE FROM pessoas WHERE id = "{record}"'
            cursor.execute(query)
            mydb.commit()
        if res == 0:
            return

        retornarDados()


def clear_entry():
    entrada.delete(0, ["end"])
# CREATE


def adicionarAoDB():
    if entrada.get() == "":
        print("Coloque algum nome")
    else:
        p1 = Person(entrada.get())
        query = f'INSERT INTO pessoas (Nome) values ("{p1.nome}")'
        cursor.execute(query)
        mydb.commit()
        retornarDados()
        clear_entry()


# READ
def retornarDados():
    tree.delete(*tree.get_children())

    queryP = 'SELECT * FROM pessoas;'
    cursor.execute(queryP)
    resultado = cursor.fetchall()

    for data in resultado:
        tree.insert('', ['end'], text=data[0], values=[data[1]])


# DELETE
def deletarPessoa():
    return


window = tk.Tk()
window.resizable(False, False)

frame = tk.Frame(borderwidth=1)

window.geometry("300x500")

tk.Label(text="Tabela de Nomes").pack()
entrada = tk.Entry(width=40)

entrada.pack()


tk.Button(text="Adicionar",
          width=10, command=adicionarAoDB).pack()


tree = ttk.Treeview(columns=("Nome"))

tree.bind('<<TreeviewSelect>>', item_selected)

tree.heading('Nome', text='Nome', anchor=['center'])

tree.column('#0', width=0, stretch="no")

tree.place(y=70, relwidth=1, relheight=1, relx=0)

retornarDados()

window.mainloop()

tk.mainloop()

cursor.close()
mydb.close()

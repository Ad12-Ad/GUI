# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:56:18 2020

@author: MAHENDRA DEWASI
"""


from tkinter import * 
import mysql.connector as db 
from tkinter import ttk 
from tkinter import messagebox 
import sys 
#from components import *

def search_books(): 
    '''Search books window''' 
    search_window = Tk() 
    search_window.title('Search Books') 
    search_window.geometry("740x500+400+200") 
    search_window.resizable(False, False)
    
    class MyTree(ttk.Treeview): 
        def __init__(self, parent, **options): 
            self.tree_frame = Frame(parent) 
            self.tree_frame.grid(options) 
            self.tree_scroll = Scrollbar(self.tree_frame) 
            self.tree_scroll.pack(side=RIGHT, fill=Y) 
            self.tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll.set) 
            self.tree_scroll.config(command=self.tree.yview) 
            self.tree.pack(expand=True) 
            def set_columns(self, columns, headings, widths): 
                self.tree['columns'] = tuple(columns) 
                self.tree.column('#0', width=0, stretch=NO)
                self.tree.heading('#0', text='') 
                for column, heading, width in zip(columns, headings, widths): 
                    self.tree.column(column, anchor=CENTER, width=width) 
                    self.tree.heading(column, text=heading) 
        def insert_data(self, data): 
            i = 0 
            for row in data: self.tree.insert(parent='', index='end', iid=i, text='', value=row) 
            i += 1
    
    entry_name = MyEntry(search_window, width=28) 
    entry_author = MyEntry(search_window, width=22) 
    entry_id = MyEntry(search_window, width=6) 
    lb_length = Label(search_window, font=FONT_SMALL, fg=CLR_GRAY) 
    lb_length.grid(row=5, column=0) 
    btn_search = Button(search_window, text='Search', width=10, font=FONT_BIG, command=lambda: populate_table()) 
    btn_search.grid(row=3, column=0, columnspan=5, pady=15) 
    Label(search_window, text='Search Books', font=FONT_REALLY_BIG).grid( row=0, column=0, columnspan=4, pady=15) 
    MyLabel(search_window, text='Enter Id:').grid(row=1, column=0) 
    MyLabel(search_window, text='Enter Name:').grid( row=1, column=1, columnspan=2, pady=2) 
    MyLabel(search_window, text='Enter Author:').grid( row=1, column=3, columnspan=2, pady=2) 
    entry_id.grid(row=2, column=0, ipady=2, padx=45) 
    entry_name.grid(row=2, column=1, columnspan=2, ipady=2, padx=30, pady=2) 
    entry_author.grid(row=2, column=3, columnspan=2, ipady=2, padx=30, pady=2) 
    def populate_table(): 
        book_id = entry_id.val()
        name = entry_name.val() 
        author = entry_author.val() 
        tree = MyTree(search_window, row=4, column=0, columnspan=4, padx=20, pady=15) 
        cols = ['id', 'name', 'author', 'fiction', 'issued'] 
        col_names = ['Id', 'Name', 'Author', 'Type', 'Is issued'] 
        widths = [50, 250, 200, 100, 90]
        tree.set_columns(columns=cols, headings=col_names, widths=widths) 
        data = db.get_search(book_id, name, author) 
        lb_length.configure(text=f'{len(data)} results') 
        tree.insert_data(data)
    populate_table()
    search_window.mainloop()
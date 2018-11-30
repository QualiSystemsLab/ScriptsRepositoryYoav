import tkinter
from tkinter import ttk

import tkinter as tk

class SubWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.x = tk.Text(self)
        self.x.pack(expand=1, fill='both')

    def draw_tree(self):
        self.current_selection = None
        self.tree = ttk.Treeview(self.x)
        self.tree.pack()
        for j in range(10):
            self.tree.insert(
                parent='',
                index=j,
                iid='gallery_{}'.format(j),
                text='Applications_{}'.format(j)
            )
            for k in range(3):
                self.tree.insert(
                    parent='gallery_{}'.format(j),
                    index=k,
                    iid='gallery_{0}_{1}'.format(j, k),
                    text='Applications_{0}_{1}'.format(j, k)
                )
        self.tree.bind('<<TreeviewSelect>>', self.foo)
        self.tree.config(selectmode='browse')


    def foo(self, event):
        self.current_selection = self.tree.selection()

    def bar(self, win1, w):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in range(w):
            self.tree.insert(
                parent='',
                index=i,
                iid='{}'.format(i),
                text=''
            )
        for i in range(w):
            if win1.current_selection:
                self.tree.set(item=str(i), column='Name', value=win1.current_selection)
                self.tree.set(item=str(i), column='Value', value=win1.current_selection)
            else:
                self.tree.set(item=str(i), column='Name', value=str(i))
                self.tree.set(item=str(i), column='Value', value=str(i+2))

    def draw_table(self, win1):
        self.tree = ttk.Treeview(self.x)
        self.tree.pack()
        self.tree.config(columns=('Name', 'Value'))
        self.tree.column('Name', anchor='center', width=200)
        self.tree.column('Value', anchor='center', width=400)
        self.tree.heading('Name', text='Name')
        self.tree.heading('Value', text='Value')

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self)
        self.win1 = SubWindow(self)
        self.win1.draw_tree()
        self.win1.pack(side="left", expand=1, fill=tk.BOTH)
        self.win2 = SubWindow(self)
        self.win2.draw_table(self.win1)
        self.win2.pack(side="right", expand=1, fill=tk.BOTH)

    def repack_win2(self, w):
        if w:
            self.win2.bar(self.win1 ,w)
        else:
            self.win2.bar(self.win1, 0)

    def in_loop(self):
        while True:
            try:
                w = None
                if self.win1.current_selection:
                    w = int(self.win1.current_selection[0].split('_')[-1])
                self.repack_win2(w)
                self.update()
            except:
                pass

if __name__ == "__main__":
    main = MainWindow()
    main.in_loop()

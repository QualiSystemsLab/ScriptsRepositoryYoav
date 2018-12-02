from tkinter import ttk
import tkinter as tk
import uuid


class SubWindow(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.x = tk.Text(self)
        self.x.pack(expand=1, fill='both')

    def _get_short_uuid(self):
        return str(uuid.uuid4())[:8]

    def get_all_children(self, item=""):
        children = self.tree.get_children(item)
        for child in children:
            children += self.get_all_children(item=child)
        return children

    def draw_tree(self, levels):
        self.current_selection = None
        self.tree = ttk.Treeview(self.x)
        self.tree.pack()
        skipped = []
        for j,level in enumerate(levels):
            my_items = self.get_all_children()
            if level.Parent == []:
                if level not in skipped:
                    self.tree.insert(
                        parent=level.Parent if level.Parent != [] else '',
                        index=j,
                        iid=level.Name,
                        text=level.Name
                    )
                    skipped.append(level)
            else:
                for apperant in level.Parent:
                    if apperant in my_items:
                        if apperant not in skipped and level not in skipped:
                            self.tree.insert(
                                parent=apperant,
                                index=j,
                                iid=level.Name,
                                text=level.Name
                            )
                            skipped.append(level)
                        elif apperant not in skipped and level in skipped:
                            self.tree.insert(
                                parent=apperant,
                                index=j,
                                iid='{}_{}'.format(level.Name, self._get_short_uuid()),
                                text=level.Name
                            )
                    else:
                        needed_parent = [par_level for par_level in levels if par_level.Name == apperant][0]
                        if needed_parent not in skipped:
                            self.tree.insert(
                                parent=needed_parent.Parent,
                                index=j,
                                iid=needed_parent.Name,
                                text=needed_parent.Name
                            )
                            skipped.append(needed_parent)

            self.tree.bind('<<TreeviewSelect>>', self.foo)
            self.tree.config(selectmode='browse')


    def foo(self, event):
        self.current_selection = self.tree.selection()

    def bar(self, win1, item):
        for i in self.tree.get_children():
            self.tree.delete(i)
        if item:
            for i,attr in enumerate(item.Attributes):
                self.tree.insert(
                    parent='',
                    index=i,
                    iid='{}'.format(i),
                    text=''
                )
            for i, attr in enumerate(item.Attributes):
                if win1.current_selection:
                    self.tree.set(item=str(i), column='Name', value=attr)
                else:
                    self.tree.set(item=str(i), column='Name', value=str(i))


    def draw_table(self, win1):
        self.tree = ttk.Treeview(self.x)
        self.tree.pack()
        self.tree['show'] = 'headings'
        self.tree.config(columns=('Name', ))
        self.tree.column('Name', anchor='center', width=200)
        # self.tree.column('Value', anchor='center', width=400)
        self.tree.heading('Name', text='Attribute Name')
        # self.tree.heading('Value', text='Value')

class MainWindow(tk.Tk):
    def __init__(self, levels, *args, **kwargs):
        tk.Tk.__init__(self)
        self.levels = levels
        self.win1 = SubWindow(self)
        self.win1.draw_tree(levels)
        self.win1.pack(side="left", expand=1, fill=tk.BOTH)
        self.win2 = SubWindow(self)
        self.win2.draw_table(self.win1)
        self.win2.pack(side="right", expand=1, fill=tk.BOTH)

    def repack_win2(self, item):
        if item:
            self.win2.bar(self.win1 ,item)
        else:
            self.win2.bar(self.win1, 0)

    def in_loop(self):
        while True:
        # try:
            item = None
            if self.win1.current_selection:
                if self.win1.current_selection[0].__contains__('_'):
                    item = filter(lambda x: x.Name == self.win1.current_selection[0].split('_')[0], self.levels)[0]
                else:
                    item = filter(lambda x:x.Name ==self.win1.current_selection[0], self.levels)[0]
                # print item
            self.repack_win2(item)
            self.update()
            # except Exception as e:
            #     print e.message


__author__ = 'yoav.e'
import pymssql
import os
import sqlinfo
import Tkinter
import tkMessageBox
import tktable


class poolitem:
    def __init__(self, ID , poolId, value, ReservationId, ownerId, IsoLevel):
        self.ID = ID
        self.poolId = poolId
        self.value = value
        self.ReservationId = ReservationId
        self.ownerId = ownerId
        self.IsoLevel = IsoLevel

itemList = []
top = Tkinter.Tk()


def getpoolstatus(cursor):
    query = r'SELECT * FROM [' + sqlinfo.database + '].[dbo].[VLanItems]'
    cursor.execute(query)
    row = cursor.fetchone()
    msgboxtxt = '\n'
    while row:
        msgboxtxt += "ID = {0}  poolId = {1}  value = {2}  ReservationId = {3}  ownerId = {4}  IsoLevel = {5}\n"\
            .format(row[0], row[1], row[2], row[3], row[4], row[5])
        itemList.append(poolitem(row[0], row[1], row[2], row[3], row[4], row[5]))
        row = cursor.fetchone()
    return itemList


conn = pymssql.connect(sqlinfo.server, sqlinfo.user, sqlinfo.password)
cursor = conn.cursor()
itl = getpoolstatus(cursor)
Tkinter.Label(top, text='ID').grid(row=0, column = 0)
Tkinter.Label(top, text='poolId').grid(row=0, column = 1)
Tkinter.Label(top, text='value').grid(row=0, column = 2)
Tkinter.Label(top, text='ReservationId').grid(row=0, column = 3)
Tkinter.Label(top, text='ownerId').grid(row=0, column = 4)
Tkinter.Label(top, text='IsoLevel').grid(row=0, column = 5)
i = 1
for item in itl:
    Tkinter.Label(top, text=str(itl[i-1].ID)).grid(row=i, column = 0)
    Tkinter.Label(top, text=str(itl[i-1].poolId)).grid(row=i, column = 1)
    Tkinter.Label(top, text=str(itl[i-1].value)).grid(row=i, column = 2)
    Tkinter.Label(top, text=str(itl[i-1].ReservationId)).grid(row=i, column = 3)
    Tkinter.Label(top, text=str(itl[i-1].ownerId)).grid(row=i, column = 4)
    Tkinter.Label(top, text=str(itl[i-1].IsoLevel)).grid(row=i, column = 5)
    i = i + 1
top.mainloop()
conn.close()
pass

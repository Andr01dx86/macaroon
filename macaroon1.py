import datetime
import time
import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import os
import sys
import threading
import array
import string

win = Tk()
#win.iconbitmap("macaroon.ico")
win.title('Macaroon v0.1')
#win.geometry('100x300')

vheader = ''
vfooter = 'Macaroon V0.1'

def clear_text(text):
   text.delete("1.0","end")
   win.update()

def add_clip(text):
    command = "echo " + text + '| clip'
    os.system(command)

def conv_caps():
    global vIOS
    vtext = []
    vbase = []
    vIOS = []
    stringIOS = ""
    strdups = ""
    strclip = ""
    vtext = ttext.get('1.0','end-1c')
    vlines = str.splitlines(vtext)
    print(vlines)
    for row in vlines:
        strnoco = str(row).translate(str.maketrans('', '', string.punctuation))
        strbase = (strnoco.upper()).replace(':','')
        vbase.append(strbase)
        strIOS = res = ':'.join(strbase[i:i + 2] for i in range(0, len(strbase), 2))
        vIOS.append(strIOS + '\n')
    dups = list_duplicates(vbase)
    if dups != []:
        messagebox.showinfo(title='Dupicates Detected', message='Duplicates have been found!\n\n' + strdups.join(dups))
    clear_text(ttext)
    ttext.insert(END,(stringIOS.join(vIOS)))

def conv_low():
    global vIOS
    vtext = []
    vbase = []
    vIOS = []
    stringIOS = ""
    strdups = ""
    vtext = ttext.get('1.0','end-1c')
    vlines = str.splitlines(vtext)
    print(vlines)
    for row in vlines:
        strnoco = str(row).translate(str.maketrans('', '', string.punctuation))
        strbase = (strnoco.lower()).replace(':','')
        vbase.append(strbase)
        strIOS = res = ':'.join(strbase[i:i + 2] for i in range(0, len(strbase), 2))
        vIOS.append(strIOS + '\n')
    dups = list_duplicates(vbase)
    if dups != []:
        messagebox.showinfo(title='Dupicates Detected', message='Duplicates have been found!\n\n' + strdups.join(dups))
    clear_text(ttext)
    ttext.insert(END,(stringIOS.join(vIOS)))

def conv_IOS():
    global vIOS
    vtext = []
    vbase = []
    vIOS = []
    stringIOS = ""
    strdups = ""
    vtext = ttext.get('1.0','end-1c')
    vlines = str.splitlines(vtext)
    print(vlines)
    for row in vlines:
        strnoco = str(row).translate(str.maketrans('', '', string.punctuation))
        strbase = (strnoco.lower()).replace(':','')
        vbase.append(strbase)
        strIOS = res = '.'.join(strbase[i:i + 4] for i in range(0, len(strbase), 4))
        vIOS.append(strIOS + '\n')
    dups = list_duplicates(vbase)
    if dups != []:
        messagebox.showinfo(title='Dupicates Detected', message='Duplicates have been found!\n\n' + strdups.join(dups))
    clear_text(ttext)
    ttext.insert(END,(stringIOS.join(vIOS)))

def conv_IB():
    global vIOS
    vtext = []
    vbase = []
    vIOS = []
    stringIOS = ""
    strdups = ""
    vtext = ttext.get('1.0','end-1c')
    vlines = str.splitlines(vtext)
    print(vlines)
    for row in vlines:
        strnoco = str(row).translate(str.maketrans('', '', string.punctuation))
        strbase = (strnoco.lower()).replace(':','')
        vbase.append(strbase)
        vIOS.append(strbase + '\n')
    dups = list_duplicates(vbase)
    if dups != []:
        messagebox.showinfo(title='Dupicates Detected', message='Duplicates have been found!\n\n' + strdups.join(dups))
    clear_text(ttext)
    ttext.insert(END,(stringIOS.join(vIOS)))

def list_duplicates(seq):
    seen = set()
    seen_add = seen.add
    # adds all elements it doesn't know yet to seen and all other to seen_twice
    seen_twice = set(x for x in seq if x in seen or seen_add(x))
    # turn the set into a list (as requested)
    return list(seen_twice)


lheader = Label(win, text=vheader, anchor=W)
bbutton1 = ttk.Button(win, text="Caps", command=conv_caps)
bbutton2 = ttk.Button(win, text="Lower", command=conv_low)
bbutton3 = ttk.Button(win, text="IOS", command=conv_IOS)
bbutton4 = ttk.Button(win, text="IB", command=conv_IB)

ttext = ScrolledText(win, wrap=tkinter.WORD, width=40, height=40)
lfooter = Label(win, text=vfooter)

lheader.grid(row=0, column=0, columnspan=4, sticky=W)

bbutton1.grid(row=1, column=0)
bbutton2.grid(row=1, column=1)
bbutton3.grid(row=1, column=2)
bbutton4.grid(row=1, column=3)

ttext.grid(row=2, column=0, columnspan=4)

lfooter.grid(row=3,column=0, columnspan=4)

win.mainloop()
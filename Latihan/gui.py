'''Mencoba membuat app interaksi sederhana'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
os.system("cls")

'''INIT'''
# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("400x300")
window.resizable(False,False)
window.title("Halo")

'''variable dan fungsi'''
# variable dan fungsi
nama_depan = tk.StringVar()
nama_belakang = tk.StringVar()

def tombol_fungsi():
    '''fungsi untuk tombol'''
    pesan = f"{nama_depan.get()} {nama_belakang.get()},selamat datang"
    showinfo(title="halo",message=pesan)
    
'''frame input'''
# frame input
frame_input = ttk.Frame(window)

'''penempatan grid,pack,place'''
frame_input.pack(padx=10,pady=10,fill="x",expand=True)

'''komponen komponen'''
# komponen label 
# 1.label nama depan
nama_depan_label = ttk.Label(frame_input,text="nama depan")
nama_depan_label.pack(padx=10,fill="x",expand=True)
# 2.entry nama depan
nama_depan_entry = ttk.Entry(frame_input,textvariable=nama_depan)
nama_depan_entry.pack(padx=10,fill="x",expand=True)
# 3. label nama belakang
nama_belakang_label = ttk.Label(frame_input,text="nama belakang")
nama_belakang_label.pack(padx=10,fill="x",expand=True)
# 4.entry nama belakang
belakang_entry = ttk.Entry(frame_input,textvariable=nama_belakang)
belakang_entry.pack(padx=10,fill="x",expand=True)
# 5.tombol
tombol = ttk.Button(frame_input,text="click",command=tombol_fungsi)
tombol.pack(fill='x',expand=True,padx=10,pady=10)

window.mainloop()


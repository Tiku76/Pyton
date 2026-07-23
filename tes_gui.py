# '''Mencoba membuat app interaksi sederhana'''

# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo
# import os
# os.system("cls")

# '''INIT'''
# # init
# window = tk.Tk()
# window.configure(bg="white")
# window.geometry("400x300")
# window.resizable(False,False)
# window.title("Halo")

# '''variable dan fungsi'''
# # variable dan fungsi
# angka_depan = tk.IntVar()
# angka_belakang = tk.IntVar()
# def tombol_fungsi():
#     '''fungsi untuk tombol'''
#     pesan = f"hasil perhitungan {angka_depan.get()}, {angka_belakang.get(),}"
#     showinfo(title="halo",message=pesan)
    
# '''frame input'''
# # frame input
# frame_input = ttk.Frame(window)

# '''penempatan grid,pack,place'''
# frame_input.pack(padx=10,pady=10,fill="x",expand=True)

# '''komponen komponen'''
# # komponen label 
# # 1.label angka depan
# angka_depan_label = ttk.Label(frame_input,text="angka depan")
# angka_depan_label.pack(padx=10,fill="x",expand=True)
# # 2.entry angka depan
# angka_depan_entry = ttk.Entry(frame_input,textvariable=angka_depan)
# angka_depan_entry.pack(padx=10,fill="x",expand=True)
# # 3. label angka belakang
# angka_belakang_label = ttk.Label(frame_input,text="angka belakang")
# angka_belakang_label.pack(padx=10,fill="x",expand=True)
# # 4.entry angka belakang
# belakang_entry = ttk.Entry(frame_input,textvariable=angka_belakang)
# belakang_entry.pack(padx=10,fill="x",expand=True)
# # 5.tombol
# tombol = ttk.Button(frame_input,text="click",command=tombol_fungsi)
# tombol.pack(fill='x',expand=True,padx=10,pady=10)

# window.mainloop()

'''CATATAN'''
# Menambahkan beberapa yang diperlukan pada code yang di bawah
# 1. menambahkan comobobox +,-,/,*
# 2. menambahkan if else statment
# 3. mengubah Intvar menjadi DoubleVar  
# 4. menambahkan try dan except
# 5. menambahkan beberapa seperti value,textvariable,dan state

'''yang bawah di pebagus menggunakan AI'''

'''Mencoba membuat app interaksi sederhana'''

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import os
os.system("cls")

'''INIT'''
# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("400x350")
window.resizable(False,False)
window.title("Halo")

'''variable dan fungsi'''
# variable dan fungsi
angka_depan = tk.DoubleVar()
angka_belakang = tk.DoubleVar()
operasi_var = tk.StringVar(value="+")

def tombol_fungsi():
    '''fungsi untuk tombol'''
    try:
        a = angka_depan.get()
        b = angka_belakang.get()
        op = operasi_var.get()

        if op == "+":
            hasil = a + b
        elif op == "-":
            hasil = a - b
        elif op == "*":
            hasil = a * b
        elif op == "/":
            if b == 0:
                showerror(title="Error", message="Tidak bisa membagi dengan nol!")
                return
            hasil = a / b
        else:
            showerror(title="Error", message="Operasi tidak dikenali")
            return

        pesan = f"{a} {op} {b} = {hasil}"
        showinfo(title="Hasil", message=pesan)

    except tk.TclError:
        showerror(title="Error", message="Input harus berupa angka!")

'''frame input'''
# frame input
frame_input = ttk.Frame(window)

'''penempatan grid,pack,place'''
frame_input.pack(padx=10,pady=10,fill="x",expand=True)

'''komponen komponen'''
# komponen label 
# 1.label angka depan
angka_depan_label = ttk.Label(frame_input,text="angka depan")
angka_depan_label.pack(padx=10,fill="x",expand=True)
# 2.entry angka depan
angka_depan_entry = ttk.Entry(frame_input,textvariable=angka_depan)
angka_depan_entry.pack(padx=10,fill="x",expand=True)

# 3. label operasi
operasi_label = ttk.Label(frame_input,text="operasi")
operasi_label.pack(padx=10,fill="x",expand=True)
# 4. combobox operasi
operasi_combobox = ttk.Combobox(
    frame_input,
    textvariable=operasi_var,
    values=["+", "-", "*", "/"],
    state="readonly"
)
operasi_combobox.pack(padx=10,fill="x",expand=True)

# 5. label angka belakang
angka_belakang_label = ttk.Label(frame_input,text="angka belakang")
angka_belakang_label.pack(padx=10,fill="x",expand=True)
# 6.entry angka belakang
belakang_entry = ttk.Entry(frame_input,textvariable=angka_belakang)
belakang_entry.pack(padx=10,fill="x",expand=True)

# 7.tombol
tombol = ttk.Button(frame_input,text="Hitung",command=tombol_fungsi)
tombol.pack(fill='x',expand=True,padx=10,pady=10)

window.mainloop()
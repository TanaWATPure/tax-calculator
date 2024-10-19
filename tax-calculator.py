import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedTk

def calculate_personal_tax(income):
    if income <= 150000:
        return 0
    elif income <= 300000:
        return (income - 150000) * 0.05
    elif income <= 500000:
        return (income - 300000) * 0.1 + 7500
    elif income <= 750000:
        return (income - 500000) * 0.15 + 27500
    elif income <= 1000000:
        return (income - 750000) * 0.2 + 65000
    elif income <= 2000000:
        return (income - 1000000) * 0.25 + 115000
    elif income <= 5000000:
        return (income - 2000000) * 0.3 + 365000
    else:
        return (income - 5000000) * 0.35 + 1265000

def calculate_corporate_tax(income):
    if income <= 300000:
        return 0
    elif income <= 3000000:
        return (income - 300000) * 0.15
    else:
        return (income - 3000000) * 0.2 + 405000

def calculate_tax():
    try:
        income = float(entry_income.get())
        if var.get() == 1:
            tax = calculate_personal_tax(income)
            messagebox.showinfo("ผลลัพธ์", f"ภาษีบุคคลธรรมดาที่ต้องจ่าย: {tax:.2f} บาท")
        elif var.get() == 2:
            tax = calculate_corporate_tax(income)
            messagebox.showinfo("ผลลัพธ์", f"ภาษีนิติบุคคลที่ต้องจ่าย: {tax:.2f} บาท")
        else:
            messagebox.showwarning("ข้อผิดพลาด", "กรุณาเลือกประเภทภาษี")
    except ValueError:
        messagebox.showwarning("ข้อผิดพลาด", "กรุณากรอกจำนวนเงินที่ถูกต้อง")

def change_theme(event):
    selected_theme = theme_var.get()  
    root.set_theme(selected_theme)    

# สร้างหน้าต่างหลัก
root = ThemedTk(theme="breeze")
root.title("โปรแกรมคำนวณภาษี by Tanawat Chitratta")
root.geometry("400x300")

# สร้างตัวเลือกประเภทภาษี
var = tk.IntVar()

ttk.Label(root, text="เลือกประเภทภาษี").pack(anchor=tk.W)
ttk.Radiobutton(root, text="บุคคลธรรมดา", variable=var, value=1).pack(anchor=tk.W)
ttk.Radiobutton(root, text="นิติบุคคล", variable=var, value=2).pack(anchor=tk.W)

# สร้างช่องกรอกเงินได้
ttk.Label(root, text="กรอกเงินได้/รายได้ (บาท):").pack()
entry_income = ttk.Entry(root)
entry_income.pack()

# ปุ่มคำนวณภาษี
ttk.Button(root, text="คำนวณภาษี", command=calculate_tax).pack(pady=10)

# สร้างเมนูเลือกธีม
ttk.Label(root, text="เลือกธีม").pack()

# รับรายการธีมทั้งหมดจาก ttkthemes
all_themes = root.get_themes()

# ตัวแปรสำหรับเก็บธีมที่เลือก
theme_var = tk.StringVar(value=all_themes[0])

# สร้าง dropdown menu สำหรับเลือกธีม
theme_menu = ttk.OptionMenu(root, theme_var, all_themes[0], *all_themes, command=change_theme)
theme_menu.pack()

# ลิขสิทธิ์
ttk.Label(root, text="Created by Tanawat Chitratta", font=("Arial", 8)).pack(pady=10)

# รันหน้าต่าง
root.mainloop()




from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk() # ทีตัวใหญ่
GUI.title(' โปรแกรมคำนวณหน่วยกิตสะสม')
GUI.geometry('550x700')

bg = PhotoImage(file = 'university.png')

BG = Label(GUI, image = bg)
BG.pack()

L = Label(GUI,text = 'กรอกจำนวนวิชาที่เรียน (วิชา)',font = (None,20))
L.pack()

v_quantity = StringVar() # ตัวแปลที่ใช้เก็บข้อคววามเมื่อพิมพ์เสร็จ
E1 = ttk.Entry(GUI, textvariable = v_quantity, font = (None,20))
E1.pack()

def Cal():
	try:
		quan = float(v_quantity.get())
		calc = quan * 3 # วิชาละ 3 หน่วยกิต * จำนวนวิชาที่กรอก
		messagebox.showinfo('หน่วยกิตทั้งหมด','หน่วยกิตทั้งหมด {} หน่วยกิต'.format(calc))
		v_quantity.set('1')
		E1.focus
	except:
		messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
		v_quantity.set('1')
		E1.focus

B = ttk.Button(GUI, text = 'คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20) # ipadx/y ขยายความกว้าง x/y


GUI.mainloop() # เพื่อให้โปรแกรมรันตลอดเวลา
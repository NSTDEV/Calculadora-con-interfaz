from tkinter import *

ventana = Tk()
ventana.title('Calculadora')
ventana.config(bg='#b45f6a')
ventana.geometry("312x430")
ventana.resizable(False,False)
ventana.attributes('-toolwindow', 'True')

i = 0

#Entrada
e_texto = Entry(ventana, font=('Impact', 12, 'bold'), bg='#d29fa6', fg='#65000d', borderwidth=5)
e_texto.grid(row=0, column=0, columnspan=4, padx=50, pady=5)

#Funciones
def click_boton(valor):
	global i
	e_texto.insert(i, valor)
	i += 1

def borrar():
	e_texto.delete(0, END)
	i = 0

def calculo():
	global i
	ecuacion = e_texto.get()
	resultado = str(eval(ecuacion))
	e_texto.delete(0, END)
	e_texto.insert(0, resultado)

class HoverButton(Button):
	def __init__(self, master, **kw):
		Button.__init__(self,master=master,**kw)
		self.defaultBackground = self["background"]
		self.bind("<Enter>", self.on_enter)
		self.bind("<Leave>", self.on_leave)

	def on_enter(self, e):
		self["background"] = self["activebackground"]

	def on_leave(self, e):
		self["background"] = self.defaultBackground

#Botones
boton1 = HoverButton(ventana, text='1', font=('Impact', 12, 'bold'), width=5, height=2, bg='#a53f4d', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(1))
boton2 =HoverButton(ventana, text='2', font=('Impact', 12, 'bold'), width=5, height=2, bg='#a53f4d', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(2))
boton3 =HoverButton(ventana, text='3', font=('Impact', 12, 'bold'), width=5, height=2, bg='#a53f4d', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(3))
boton4 =HoverButton(ventana, text='4', font=('Impact', 12, 'bold'), width=5, height=2, bg='#a53f4d', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(4))
boton5 =HoverButton(ventana, text='5', font=('Impact', 12, 'bold'), width=5, height=2, bg='#a53f4d', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(5))
boton6 =HoverButton(ventana, text='6', font=('Impact', 12, 'bold'), width=5, height=2, bg='#a53f4d', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(6))
boton7 =HoverButton(ventana, text='7', font=('Impact', 12, 'bold'), width=5, height=2, bg='#a53f4d', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(7))
boton8 =HoverButton(ventana, text='8', font=('Impact', 12, 'bold'), width=5, height=2, bg='#a53f4d', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(8))
boton9 =HoverButton(ventana, text='9', font=('Impact', 12, 'bold'), width=5, height=2, bg='#a53f4d', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(9))
boton0 =HoverButton(ventana, text='0', font=('Impact', 12, 'bold'), width=13, height=2, bg='#a53f4d', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(0))

boton_borrar =HoverButton(ventana, text='AC', font=('Impact', 12, 'bold'), width=5, height=2, bg='#65000d', fg='#d29fa6', borderwidth=8, command=lambda: borrar())
boton_parentesis1 =HoverButton(ventana, text='(', font=('Impact', 12, 'bold'), width=5, height=2, bg='#961f2f', fg='#d29fa6', borderwidth=8, command=lambda: click_boton('('))
boton_parentesis2 =HoverButton(ventana, text=')', font=('Impact', 12, 'bold'), width=5, height=2, bg='#961f2f', fg='#d29fa6', borderwidth=8, command=lambda: click_boton(')'))
boton_punto =HoverButton(ventana, text='.', font=('Impact', 12, 'bold'), width=5, height=2, bg='#961f2f', fg='#d29fa6', borderwidth=8, command=lambda: click_boton('.'))

boton_div =HoverButton(ventana, text='/', font=('Impact', 12, 'bold'), width=5, height=2, bg='#961f2f', fg='#d29fa6', borderwidth=8, command=lambda: click_boton('/'))
boton_mult =HoverButton(ventana, text='*', font=('Impact', 12, 'bold'), width=5, height=2, bg='#961f2f', fg='#d29fa6', borderwidth=8, command=lambda: click_boton('*'))
boton_sum =HoverButton(ventana, text='+', font=('Impact', 12, 'bold'), width=5, height=2, bg='#961f2f', fg='#d29fa6', borderwidth=8, command=lambda: click_boton('+'))
boton_rest =HoverButton(ventana, text='-', font=('Impact', 12, 'bold'), width=5, height=2, bg='#961f2f', fg='#d29fa6', borderwidth=8, command=lambda: click_boton('-'))
boton_igual =HoverButton(ventana, text='=', font=('Impact', 12, 'bold'), width=5, height=2, bg='#961f2f', fg='#d29fa6', borderwidth=8, command=lambda: calculo())

#Posicionar Botones
boton_borrar.grid(row=1, column=0, padx=5, pady=5)
boton_parentesis1.grid(row=1, column=1, padx=5, pady=5)
boton_parentesis2.grid(row=1, column=2, padx=5, pady=5)
boton_mult.grid(row=1, column=3, padx=5, pady=5)

boton7.grid(row=2, column=0, padx=5, pady=5)
boton8.grid(row=2, column=1, padx=5, pady=5)
boton9.grid(row=2, column=2, padx=5, pady=5)
boton_div.grid(row=2, column=3, padx=5, pady=5)

boton4.grid(row=3, column=0, padx=5, pady=5)
boton5.grid(row=3, column=1, padx=5, pady=5)
boton6.grid(row=3, column=2, padx=5, pady=5)
boton_sum.grid(row=3, column=3, padx=5, pady=5)

boton1.grid(row=4, column=0, padx=5, pady=5)
boton2.grid(row=4, column=1, padx=5, pady=5)
boton3.grid(row=4, column=2, padx=5, pady=5)
boton_rest.grid(row=4, column=3, padx=5, pady=5)

boton0.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
boton_punto.grid(row=5, column=2, padx=5, pady=5)
boton_igual.grid(row=5, column=3, padx=5, pady=5)

ventana.mainloop()

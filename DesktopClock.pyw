from tkinter import *
from time import strftime

window = Tk()
window.title("Clock")
#window.geometry('280x120+820+0')
window.resizable(False,False)
window.attributes('-topmost', True)
window.config(bg="black")
window.overrideredirect(True)

w = 280
h = 120

ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window.geometry('%dx120+%d+1' % (w, x))

var1 = IntVar()

def time():
#24-Hour Time
	if (var1.get() == 0):
		time_string = strftime('%H%M %S\n%m/%d/%Y')
		label_time.config(text=time_string)
		label_time.after(1000, time)
#12-Hour Time
	if (var1.get() == 1):
		time_string = strftime('%I:%M:%S %p\n%m/%d/%Y')
		label_time.config(text=time_string)
		label_time.after(1000, time)

def exit():
	window.destroy()

def colorpick_Cyan():
	label_time.config(fg="Cyan")
def colorpick_Green():
	label_time.config(fg="Green")
def colorpick_Yellow():
	label_time.config(fg="Yellow")
def colorpick_Red():
	label_time.config(fg="Red")
	

label_time = Label(window,
	fg="white",
	bg="black",
	font=("Buxton Sketch", 32, 'bold'))
label_time.place(x=10, y=15)

exit_button = Button(window,
	text="X",
	fg="white",
	bg="red",
	command=exit)
exit_button.place(x=260,y=1)

colorpicker = Menubutton(window, text="Color")	
colorpicker.place(x=1,y=1)	
colorpicker.menu = Menu(colorpicker)
colorpicker["menu"] = colorpicker.menu

colorpicker.menu.add_command(label='Cyan', 
 	command=colorpick_Cyan)
colorpicker.menu.add_command(label='Green', 
 	command=colorpick_Green)
colorpicker.menu.add_command(label='Yellow', 
 	command=colorpick_Yellow)
colorpicker.menu.add_command(label='Red', 
 	command=colorpick_Red)

timeformat = Menubutton(window, text="Format")
timeformat.place(x=42,y=1)
timeformat.menu = Menu(timeformat)
timeformat["menu"] = timeformat.menu
timeformat.menu.add_checkbutton(label='12-hour',
	variable=var1,
	onvalue=1,
	offvalue=0)







time()

window.mainloop()

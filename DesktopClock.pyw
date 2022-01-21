from tkinter import *
from time import strftime

window = Tk()
window.title("Clock")
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

window.geometry('%dx120+%d+0' % (w, x))

var1 = IntVar()


def time():
#24-Hour Time
	if (var1.get() == 1):
		time_string = strftime('%H:%M:%S\n%m/%d/%Y')
		label_time.config(text=time_string)
		label_time.after(1000, time)
		label_time.place(x=30, y=15)
#12-Hour Time
	if (var1.get() == 0):
		time_string = strftime('%I:%M:%S %p\n%m/%d/%Y')
		label_time.config(text=time_string)
		label_time.after(1000, time)
		label_time.place(x=10, y=15)

def exit():
	window.destroy()

def colorpick_Cyan():
	label_time.config(fg="Cyan")
	colorpicker.config(fg="Cyan")
	timeformat.config(fg="Cyan")
	backgroundchange.config(fg="Cyan")
def colorpick_Green():
	label_time.config(fg="Green")
	colorpicker.config(fg="Green")
	timeformat.config(fg="Green")
	backgroundchange.config(fg="Green")
def colorpick_Yellow():
	label_time.config(fg="Yellow")
	colorpicker.config(fg="Yellow")
	timeformat.config(fg="Yellow")
	backgroundchange.config(fg="Yellow")
def colorpick_Red():
	label_time.config(fg="Red")
	colorpicker.config(fg="Red")
	timeformat.config(fg="Red")
	backgroundchange.config(fg="Red")
def colorpick_Blue():
	label_time.config(fg="Blue")
	colorpicker.config(fg="Blue")
	timeformat.config(fg="Blue")
	backgroundchange.config(fg="Blue")
def colorpick_White():
	label_time.config(fg="White")
	colorpicker.config(fg="White")
	timeformat.config(fg="White")
	backgroundchange.config(fg="White")
	

def backgroundchange_White():
	label_time.config(bg="White")
	colorpicker.config(bg="White")
	timeformat.config(bg="White")
	backgroundchange.config(bg="White")
	window.config(bg="White")
def backgroundchange_Black():
	label_time.config(bg="Black")
	colorpicker.config(bg="Black")
	timeformat.config(bg="Black")
	backgroundchange.config(bg="Black")
	window.config(bg="Black")

label_time = Label(window,
	fg="red",
	bg="black",
	font=("Buxton Sketch", 32, 'bold'))
label_time.place(x=10, y=15)

exit_button = Button(window,
	text="X",
	fg="white",
	bg="red",
	command=exit)
exit_button.place(x=260,y=1)



colorpicker = Menubutton(window, text="Scheme", bg="black", fg="red")	
colorpicker.place(x=1,y=1)	
colorpicker.menu = Menu(colorpicker)
colorpicker["menu"] = colorpicker.menu

colorpicker.menu.add_command(label='Red (Default)', 
 	command=colorpick_Red)
colorpicker.menu.add_command(label='White', 
 	command=colorpick_White)
colorpicker.menu.add_command(label='Cyan', 
 	command=colorpick_Cyan)
colorpicker.menu.add_command(label='Green', 
 	command=colorpick_Green)
colorpicker.menu.add_command(label='Yellow', 
 	command=colorpick_Yellow)
colorpicker.menu.add_command(label='Blue', 
 	command=colorpick_Blue)

timeformat = Menubutton(window, text="Format", bg="black", fg="red")
timeformat.place(x=160,y=1)
timeformat.menu = Menu(timeformat)
timeformat["menu"] = timeformat.menu
timeformat.menu.add_checkbutton(label='12-hour (Default)',
	variable=var1,
	onvalue=0,
	offvalue=1)
timeformat.menu.add_checkbutton(label='24-hour',
	variable=var1,
	onvalue=1,
	offvalue=0)

backgroundchange = Menubutton(window, text="Background Color", bg="black", fg="red")
backgroundchange.place(x=55,y=1)
backgroundchange.menu = Menu(backgroundchange)
backgroundchange["menu"] = backgroundchange.menu
backgroundchange.menu.add_command(label = 'Dark Mode (Default)',
	command=backgroundchange_Black)
backgroundchange.menu.add_command(label = 'Light Mode',
	command=backgroundchange_White) 

time()

window.mainloop()
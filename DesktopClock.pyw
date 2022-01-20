from tkinter import *
from time import strftime

window = Tk()
window.title("Clock")
window.geometry('300x150')
window.resizable(False,False)
window.attributes('-topmost', True)
window.config(bg="black")

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
	
label_time = Label(window,
	fg="red",
	bg="black",
	font=("Buxton Sketch", 40, 'bold'))

#Check button changes from 24-hour to 12-hour format
checkbox = Checkbutton(window,
	text="12-hour",
	variable=var1,
	onvalue=1,
	offvalue=0,
	fg="red",
	bg="black",
	command=time)


label_time.pack()
checkbox.pack()


time()

window.mainloop()


from tkinter.messagebox import *
from tkinter import *
import tkinter as tk

#------------------------------------


class ScrollingFrame( Frame ):

	def __init__(self,parent,scroll_region,X_scroll=False,Y_scroll=True,*args ,**kwargs):
		Frame.__init__(self,parent)

		self.configure(bd=2, relief="groove")

		self.region = scroll_region
		
		if Y_scroll: #if True
			self.y_scroll=Scrollbar(self,orient="vertical")
			self.y_scroll.pack(side="right",fill="y")
		
		if X_scroll:
			self.x_scroll=Scrollbar(self,orient="horizontal")
			self.x_scroll.pack(side="bottom",fill="x", anchor='nw')
		
		self.canvas=Canvas(self,relief="ridge",**kwargs) 
		self.canvas.pack(side="top")

		if Y_scroll:
			self.canvas.configure(yscrollcommand=self.set_scrollbary)
			self.y_scroll.configure( command=self.canvas.yview )
		
		if X_scroll:
			self.canvas.configure(xscrollcommand=self.set_scrollbarx)
			self.x_scroll.configure( command=self.canvas.xview )

		self.container=Frame(self.canvas, height=self.region[0], width=self.region[1]) #wideget continer...
		self.canvas.create_window((0,0),window=self.container,anchor='nw')
		self.container.bind("<Configure>",self.scroll)
		#configure is a event called when there is a change in size of a widgets
		#here <Configure> id called when size of container frame exceeded from specified scroll_region
	def scroll(self,event):
		""" .bbox("all") >> Return a tuple of X1,Y1,X2,Y2 coordinates for a rectangle
        which encloses all items with tags specified as arguments."""
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=self.region[1], height=self.region[0])
	def set_scrollbary(self,first, last):
		self.y_scroll.set(first, last)
		self.update()
	def set_scrollbarx(self,first, last):
		self.x_scroll.set(first, last)
		self.update()

#------------------------------------
class addBox( Frame ):

	def __init__(self, parent):

		Frame.__init__(self, parent)

		self.configure(bd=1, relief="ridge")

		self.my_var1 = StringVar()
		self.my_var2 = StringVar()

		entl =  Label(self, text='What do you want to be reminded of')
		ent = Entry(self, textvariable =  self.my_var1)

		enttl = Label(self, pady = 10, text ="Remind how many minutes after the previous signal?")
		entt = Entry(self, textvariable= self.my_var2)

		entl.grid(row = 0, column = 1, pady = 2, sticky = W)
		ent.grid(row = 0, column = 2, pady = 2, sticky = W)
		
		enttl.grid(row = 1, column = 1, pady = 2, sticky = W)
		entt.grid(row = 1, column = 2, pady = 2, sticky = W)
	
	def get_input_values(self):
		""" Take values from all entry boxes variables and return them as tuple.... """

		return ( self.my_var1.get().strip(), self.my_var2.get().strip() )
  

#------------------------------------

def clicker(label_text):
	global pop
	pop = Toplevel(root)
	pop.title("Reminder")
	rem_label = Label(pop,text = label_text)
	rem_label.pack()
	
	# frame_pop = Frame(pop)
	button_pop = tk.Button(pop, text="Click Me", command=lambda: var.set(1))
	button_pop.pack()
	button_pop.wait_variable(var)
	pop.destroy()
		

#------------------------------------

def removebox():
	if not all_frameinps == []:
		all_frameinps.pop().destroy() 
	else:
		print("first add any frame...")

def addNewBox():
	new = addBox( body.container ) #pass the parent window 
	new.pack()
	all_frameinps.append(new)

#------------------------------------

def check(packed_frames):
	global passed 
	values = packed_frames.get_input_values()
	print(values)

	if values[0] == "" or values[1] == "":
		#check if they are empty
		print("Entry is empty")
		return False

	elif not values[1].isdigit():
		print("Int was required but String Enterred!")
		return False
	else:
		return True

#------------------------------------

def timer( details ):
	
	
	root.after( int( details[1] )*1000*60) 
	clicker(details[0])
	print("You want to be reminded of " +  details[0]  + " after " + details[1] + " minutes")	
	


#------------------------------------

def start():
	
	if startbtn.cget("text") == "start":	
		for packed_frames in all_frameinps:
				print("Validating Inputs for frame", packed_frames)

				#validate entry for every added frames and if any frame has wrong entry stop chekcing for others

				result = check( packed_frames )

				if result:
						
					if startbtn.cget("text") == "start":
						startbtn.configure(text = "stop")
						
					print("correct input data")
						#this frame Entries has no any wrong entries proceed with its data
					print( packed_frames.get_input_values() )

					timer(  packed_frames.get_input_values()  )

				

				else:
					print("Some wrong inputs were given")
					
	elif startbtn.cget("text") == "stop":
		
		startbtn.configure(text = "start")
		print("The button is stop")
	else:
		print("ERROR")

#------------------------------------

all_frameinps = []

root = Tk()
root.title("Timer GUI")
#root.geometry("600x600")
#root.resizable(width=False, height=False)

var = tk.IntVar()

frametop = Frame(root)
frametop.pack(pady = 10,side = "top")

body = ScrollingFrame(root , (500,525), Y_scroll=True)
body.pack()

removeboxButton = Button(frametop, text='Remove Time Input', fg="Red", command=removebox)
removeboxButton.pack(in_=frametop, side=LEFT)

addboxButton = Button(frametop, text='Add Time Input', fg="Red", command=addNewBox)
addboxButton.pack(in_=frametop, side=LEFT)

framebottom = Frame(root)
framebottom.pack(pady = 10,side = "bottom")

startbtn = Button(framebottom, text = "start", command = start)
startbtn.pack(side = "bottom")

root.mainloop()



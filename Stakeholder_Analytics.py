from Tkinter import *
#import pygal
import operator  
import pdb
import FixTk
import os
                                                    
#from pygal.style import DefaultStyle

#from pygal.style import LightGreenStyle

#from pygal.style import BlueStyle


skholder = [[0 for x in xrange(5)] for x in xrange(10)]
nameindex = 0
influenceindex = 1
focusindex = 2
flexindex = 3
positionindex = 4
casename = []
outcomes = []
outcomesnum = []
path = "/Users/rohanpavuluri/Desktop/"
class Transition(Tk):

    def __init__(self, *args, **kwargs):
        
		Tk.__init__(self, *args, **kwargs)
		container = Frame(self)

		container.pack(side="top", fill="both", expand = True)

		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		w = 900 # width for the Tk root
		h = 650 # height for the Tk root

		ws = container.winfo_screenwidth() # width of the screen
		hs = container.winfo_screenheight() # height of the screen

		x = (ws/2) - (w/2)
		y = (hs/2) - (h/2)

		self.geometry('%dx%d+%d+%d' % (w, h, x, y))

		self.frames = {}

		#for loop through pages, set up as classes
		for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, PageFive, PageSix, PageSeven, PageEight): 

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")

		self.show_frame(StartPage)

    def show_frame(self, cont):
		frame = self.frames[cont]
		frame.tkraise()

class StartPage(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		label=Label(self, 
		 text="Welcome to \n Stakeholder Analytics",
		 fg = "white",
		 bg = "OrangeRed4",
		 width=20,
		 font = "Times 60")
		label.place(relx=0.5, rely=0.4, anchor=CENTER)

		self.button = Button(width=15,
		 text="Start New Case",
		 fg = "gray26",
		 font = "Times 14 bold",
		 command= lambda: self.combiner(controller))

		#button.pack()
		self.button.place(relx=0.5, rely=0.57, anchor=CENTER)

		Frame.configure(self,background="gray15")
		
	def combiner(self, controller):
		controller.show_frame(PageOne)
		self.button.destroy()

class PageOne(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.label = Label(self, text="Enter Case Name",font="Times 26",fg="white",bg="gray15",width=25).place(relx=0.5, rely=0.4, anchor=CENTER)
		self.entry = Entry(self, width=25)
		self.entry.place(relx=0.5, rely=0.45, anchor=CENTER)
		self.button1 = Button(self, width=15, text="Complete", fg="gray15", font = "Times 14 bold", command= lambda: self.combiner1(controller))
		self.button1.place(relx=0.5, rely=0.52, anchor=CENTER)
		Frame.configure(self,background="gray15")
	
	def combiner1(self, controller):
		 controller.show_frame(PageTwo)
		 self.button1.destroy()
		 casename.append(self.entry.get()) 

class PageTwo(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		self.myframe=Frame(self, width=50, height=100)
		self.myframe.place(x=0,y=0)
		self.myframe.pack()

		self.canvas=Canvas(self.myframe)
		self.frame=Frame(self.canvas,bg="gray15")
		self.myscrollbar=Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.myscrollbar.set)

		self.myscrollbar.pack(side="right",fill="y")
		self.canvas.pack(side="left")
		x0 = self.frame.winfo_screenwidth()/2
		y0 = self.frame.winfo_screenheight()/2
		#self.canvas.create_window((0,0),window=self.frame,height=1150) 
		self.canvas.create_window((0,0),window=self.frame,anchor='nw')

		self.frame.bind("<Configure>", self.myfunction)
		
		#label = Label(self.frame, text="",font="Times 16 bold",fg="gray15",bg="gray15",width=25).grid(row = 0, column = 0)
		self.names = []
		Label(self.frame,text="",bg="gray15",width=17).grid(row=0,column=0) #ghost label to move Big Label over
		self.bigLabel = Label(self.frame, text="Enter Stakeholders", fg = "white", bg = "OrangeRed4", width=20, font = "Times 60").grid(row=1, column=3, pady = 20)
		count = 0
		for i in xrange(2,22,2):
			Label(self.frame, text="Stakeholder",font="Times 16 bold",fg="white",bg="gray15",width=25).grid(row = i, column = 3)
			skholder[count][nameindex] = Entry(self.frame, width=25)
			skholder[count][nameindex].grid(row = i+1, column = 3, pady=20)
			count += 1
		
		Label(self.frame,text="",bg="gray15",width=17).grid(row=40,column=3)
		self.button = Button(self.frame, width=15, text="Complete", fg="OrangeRed4", font="Times 14 bold", command = lambda: self.combiner(controller))
		self.button.grid(row=43, column=3)
		Frame.configure(self,background="gray15")
		Label(self.frame,text="",bg="gray15",width=30).grid(row=52,column=3)

	
	def combiner(self, controller):
		count = 0
		for i in skholder:
			skholder[count][nameindex] = skholder[count][nameindex].get()
			count += 1
		controller.show_frame(PageThree)
		controller.frames[PageThree].data()
		self.button.destroy()
		
	def myfunction(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=1000,height=1150,bg="gray15")

class PageThree(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		self.myframe=Frame(self,bg="gray15")
		self.myframe.place(x=0,y=0)
		self.myframe.pack()

		#self.canvas=Canvas(self.myframe)
		self.canvas=Canvas(self.myframe, bg="gray15")
		self.frame=Frame(self.canvas,bg="gray15")
		self.myscrollbar=Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.myscrollbar.set)

		self.myscrollbar.pack(side="right",fill="y")
		self.canvas.pack(side="left")
		#self.canvas.pack(side="top",fill="x")
		self.canvas.create_window((0,0),window=self.frame,anchor='nw')
		self.frame.bind("<Configure>", self.myfunction)
		#ghost label
		Label(self.frame,text="",bg="gray15",width=9).grid(row=0,column=0)
		Label(self.frame,text=" Stakeholder Influence ",bg="OrangeRed4",fg="white",font="Times 40").grid(row=1,column=2,pady=20)
		#self.data()
		
		Label(self.frame,text="",bg="gray15",width=30).grid(row=40,column=2)
		self.button = Button(self.frame, width=15, text="Complete", fg="OrangeRed4", font="Times 14 bold", command= lambda: self.combiner(controller))
		self.button.grid(row=43,column=2) 
		Label(self.frame,text="",bg="gray15",width=30).grid(row=52,column=2)

		self.frame.bind("<Configure>", self.myfunction)

	def data(self):
		count = 0
		for i in xrange(3,33,3):
			Label(self.frame, text=skholder[count][nameindex], fg = "white", bg = "OrangeRed4", font = "Times 14 bold").grid(row = i, column = 2, pady=20)
			Label(self.frame, text="No Influence", fg="white", bg="gray15").grid(row = i+1,column=1)
			skholder[count][influenceindex] = Scale(self.frame, from_=0, to=100, tickinterval=10, showvalue=False,length=550, bg="gray15", fg="white", orient=HORIZONTAL)
			skholder[count][influenceindex].grid(row = i + 1, column = 2,pady=40)
			skholder[count][influenceindex].set(50)
			Label(self.frame, text="Only Influence", fg="white", bg="gray15").grid(row = i + 1, column = 3)
			count += 1
	
	def getscales(self):
		for i in skholder:
			i[influenceindex] = i[influenceindex].get()
			
	def myfunction(self,event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=900,height=650)
		
	def combiner(self, controller):
		controller.show_frame(PageFour)
		controller.frames[PageThree].getscales()
		controller.frames[PageFour].data() 
		self.button.destroy()

class PageFour(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		self.myframe=Frame(self,bg="gray15")
		self.myframe.place(x=0,y=0)
		self.myframe.pack()

		#self.canvas=Canvas(self.myframe)
		self.canvas=Canvas(self.myframe, bg="gray15")
		self.frame=Frame(self.canvas,bg="gray15")
		self.myscrollbar=Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.myscrollbar.set)

		self.myscrollbar.pack(side="right",fill="y")
		self.canvas.pack(side="left")
		#self.canvas.pack(side="top",fill="x")
		self.canvas.create_window((0,0),window=self.frame,anchor='nw')
		self.frame.bind("<Configure>", self.myfunction)
		#ghost label
		Label(self.frame,text="",bg="gray15",width=12).grid(row=0,column=0)
		Label(self.frame,text=" Stakeholder Focus ",bg="OrangeRed4",fg="white",font="Times 40").grid(row=1,column=2,pady=10)
		#self.data()
		Label(self.frame,text="",bg="gray15",width=30).grid(row=40,column=2)
		self.button = Button(self.frame, width=17, text="Complete", fg="OrangeRed4", font="Times 14 bold", command= lambda: self.combiner(controller))
		self.button.grid(row=43,column=2) 
		Label(self.frame,text="",bg="gray15",width=30).grid(row=52,column=2)

		self.frame.bind("<Configure>", self.myfunction)

	def data(self):
		count = 0
		for i in xrange(3,33,3):
			Label(self.frame, text=skholder[count][nameindex], fg = "white", bg = "OrangeRed4", font = "Times 14 bold").grid(row = i, column = 2, pady = 20)
			Label(self.frame, text="No Focus", fg="white", bg="gray15").grid(row = i+1,column=1)
			#Sliding Scale
			skholder[count][focusindex] = Scale(self.frame, from_=0, to=100, tickinterval=10, showvalue=False,length=550, bg="gray15", fg="white", orient=HORIZONTAL)
			skholder[count][focusindex].grid(row = i + 1, column = 2,pady=40)
			skholder[count][focusindex].set(50)
			Label(self.frame, text="Only Focus", fg="white", bg="gray15").grid(row = i + 1, column = 3)
			count += 1
	
	def myfunction(self,event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=900,height=650)
	
	def getscales(self):
		for i in skholder:
			i[focusindex] = i[focusindex].get()
	
	def combiner(self, controller):
		controller.show_frame(PageFive)
		controller.frames[PageFour].getscales()
		controller.frames[PageFive].data() 
		self.button.destroy()

class PageFive(Frame):

	x = 0

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		self.myframe=Frame(self,bg="gray15")
		self.myframe.place(x=0,y=0)
		self.myframe.pack()

		#self.canvas=Canvas(self.myframe)
		self.canvas=Canvas(self.myframe, bg="gray15")
		self.frame=Frame(self.canvas,bg="gray15")
		self.myscrollbar=Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.myscrollbar.set)

		self.myscrollbar.pack(side="right",fill="y")
		self.canvas.pack(side="left")
		#self.canvas.pack(side="top",fill="x")
		self.canvas.create_window((0,0),window=self.frame,anchor='nw')
		self.frame.bind("<Configure>", self.myfunction)
		#ghost label
		Label(self.frame,text="",bg="gray15",width=10).grid(row=0,column=0)
		Label(self.frame,text=" Stakeholder Flexibility ",bg="OrangeRed4",fg="white",font="Times 40").grid(row=1,column=2,pady=10)
		#self.data()
		Label(self.frame,text="",bg="gray15",width=30).grid(row=40,column=2)
		self.button = Button(self.frame, width=15, text="Complete", fg="OrangeRed4", font="Times 14 bold", command= lambda: self.combiner(controller))
		self.button.grid(row=43,column=2) 
		Label(self.frame,text="",bg="gray15",width=30).grid(row=52,column=2)

		print("lol let's try this")

		self.frame.bind("<Configure>", self.myfunction)

	def data(self):
		count = 0
		for i in xrange(3,33,3):
			Label(self.frame, text=skholder[count][nameindex], fg = "white", bg = "OrangeRed4", font = "Times 14 bold").grid(row = i, column = 2, pady = 20)
			Label(self.frame, text="Not Flexible", fg="white", bg="gray15").grid(row = i+1,column=1)
			skholder[count][flexindex] = Scale(self.frame, from_=0, to=100, tickinterval=10, showvalue=False,length=550, bg="gray15", fg="white", orient=HORIZONTAL)
			skholder[count][flexindex].grid(row = i + 1, column = 2,pady=40)
			skholder[count][flexindex].set(50)
			Label(self.frame, text="Always Flexibile", fg="white", bg="gray15").grid(row = i + 1, column = 3)
			count += 1
	
	def getscales(self):
		for i in skholder:
			i[flexindex] = i[flexindex].get()
	
	def myfunction(self,event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=900,height=650)
		
	def combiner(self, controller):
		print("My life is depressing")
		controller.frames[PageFive].getscales()
		controller.show_frame(PageSix)
		#controller.frames[PageFive].data() 
		self.button.destroy()

		print("I have lots of problems")
		dictinfluence = {}
		dictfocus = {}
		dictflex = {}
		for i in skholder:
			dictinfluence[i[nameindex]] = i[influenceindex]
			dictfocus[i[nameindex]] = i[focusindex]
			dictflex[i[nameindex]] = i[flexindex]
		
		#Influence
		print("But soft. What light through yonder window breaks")
		sortedinfluence = sorted(dictinfluence.items(), key=operator.itemgetter(1))
		bar_chart = pygal.HorizontalBar(include_x_axis = False, show_x_labels=False, title=casename[0] + "\n Stakeholder Analytics")
		bar_chart.x_labels = [sortedinfluence[x][nameindex] for x in xrange(len(sortedinfluence))]
		bar_chart.add('Influence', [sortedinfluence[x][1] for x in xrange(len(sortedinfluence))])  
		#pdb.set_trace()
		os.path.abspath(path)
		print("Whan that April withe his shoores soote")
		filehandler = open("/Users/rohanpavuluri/Desktop/test.txt", "w+")
		filehandler.write("okay this is a test")
		filehandler.close()	
		print("testing")
		bar_chart.render_to_file(path + 'Influence.svg')
		#bar_chart.render_in_browser()#("Influence.svg")
		print("jkjkjkjk")      
	
		#Focus
		sortedfocus = sorted(dictfocus.items(), key=operator.itemgetter(1))
		bar_chart = pygal.HorizontalBar(include_x_axis = False, style=LightGreenStyle,show_x_labels=False, title=casename[0] + "\n Stakeholder Analytics")
		bar_chart.x_labels = [sortedfocus[x][nameindex] for x in xrange(len(sortedfocus))]
		bar_chart.add("Focus", [sortedfocus[x][1] for x in xrange(len(sortedfocus))])  
		bar_chart.render_to_file(path + 'Focus.svg')


		#Flexibility
		sortedflex = sorted(dictflex.items(), key=operator.itemgetter(1))
		bar_chart = pygal.HorizontalBar(include_x_axis = False, margin_left=100,style=BlueStyle,show_x_labels=False, title=casename[0] + "\n Stakeholder Analytics")
		#sortedflex.xaxis.set_visible(False)
		bar_chart.x_labels = [sortedflex[x][nameindex] for x in xrange(len(sortedflex))]
		bar_chart.add("Flexibility", [sortedflex[x][1] for x in xrange(len(sortedflex))])  
		bar_chart.render_to_file(path + 'Flexibility.svg')
		#bar_chart.render_in_browser()#_to_file(path + 'Flexibility.svg') 

		#Influence vs. Focus
		influenceFocus = [{'value':(dictinfluence[x[nameindex]],dictfocus[x[nameindex]]), 'label': x[0]} for x in skholder]
		xy_chart = pygal.XY(stroke=False,print_labels=True,show_x_labels=False,show_y_labels=False, x_title='Influence', y_title='Focus')
		xy_chart.title = casename[0] + "\n Stakeholder Analytics"
		xy_chart.add("Stakeholders",influenceFocus, dots_size=10)
		xy_chart.render_to_file(path + 'Influence vs. Focus.svg')     

		#Influence vs. Flexibility
		influenceFlex = [{'value':(dictinfluence[x[nameindex]],dictflex[x[nameindex]]), 'label': x[0]} for x in skholder]
		xy_chart = pygal.XY(style=BlueStyle,stroke=False, print_labels=True,show_x_labels=False,show_y_labels=False, x_title='Influence', y_title='Flexibility')
		xy_chart.title = casename[0] + "\n Stakeholder Analytics"
		xy_chart.add("Stakeholders",influenceFlex, dots_size=10)
		xy_chart.render_to_file(path + 'Influence vs. Flexibility.svg')

class PageSix(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		self.myframe=Frame(self, width=50, height=100)
		self.myframe.place(x=0,y=0)
		self.myframe.pack()

		self.canvas=Canvas(self.myframe)
		self.frame=Frame(self.canvas,bg="gray15")
		self.myscrollbar=Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.myscrollbar.set)

		self.myscrollbar.pack(side="right",fill="y")
		self.canvas.pack(side="left")
		x0 = self.frame.winfo_screenwidth()/2
		y0 = self.frame.winfo_screenheight()/2
		#self.canvas.create_window((0,0),window=self.frame,height=1150) 
		self.canvas.create_window((0,0),window=self.frame,anchor='nw')

		self.frame.bind("<Configure>", self.myfunction)
		 
		#label = Label(self.frame, text="",font="Times 16 bold",fg="gray15",bg="gray15",width=25).grid(row = 0, column = 0)
	
		Label(self.frame,text="",bg="gray15",width=17).grid(row=0,column=0) #ghost label to move Big Label over
		self.bigLabel = Label(self.frame, text="Enter Stakeholder \n Postions", fg = "white", bg = "OrangeRed4", width=20, font = "Times 60").grid(row=1, column=3, pady = 40)
		count = 0
		
		for i in xrange(2,8,2):
			Label(self.frame, text="Stakeholder Position",font="Times 16 bold",fg="white",bg="gray15",width=25).grid(row = i, column = 3)
			outcomes.append(Entry(self.frame, width=25))
			outcomes[count].grid(row = i+1,column = 3, pady=20)
			count += 1
		
		Label(self.frame,text="",bg="gray15",width=17).grid(row=10,column=3) 
		self.button = Button(self.frame, bg="gray15", fg="gray15", width=15, text="Complete", font="Times 14 bold", command = lambda: self.combiner(controller))
		self.button.grid(column=3)
		Frame.configure(self)
	
	def getOutcomes(self):
		for i in outcomes:
			i = i.get()
	
	def combiner(self, controller):
		controller.frames[PageSeven].data()
		controller.show_frame(PageSeven)
		self.button.destroy()
			
	def myfunction(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=1000,height=1150,bg="gray15")

class PageSeven(Frame):

	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		self.myframe=Frame(self,bg="gray15")
		self.myframe.place(x=0,y=0)
		self.myframe.pack()

		#self.canvas=Canvas(self.myframe)
		self.canvas=Canvas(self.myframe, bg="gray15")
		self.frame=Frame(self.canvas,bg="gray15")
		self.myscrollbar=Scrollbar(self.myframe,orient="vertical",command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.myscrollbar.set)

		self.myscrollbar.pack(side="right",fill="y")
		self.canvas.pack(side="left")
		self.canvas.create_window((0,0),window=self.frame,anchor='nw')
		self.frame.bind("<Configure>", self.myfunction)
		#ghost label
		Label(self.frame,text="",bg="gray15",width=22).grid(row=0,column=0)
		Label(self.frame,text=" Place Positions on Spectrum ",bg="OrangeRed4",fg="white",font="Times 40").grid(row=1,column=1,pady=20)
		#self.data()
		self.button = Button(self.frame, width=15, text="Complete", fg="OrangeRed4", font="Times 14 bold", command= lambda: self.combiner(controller))
		self.button.grid(row=50,column=1) 
		Label(self.frame,text="",bg="gray15",width=30).grid(row=59,column=1)
		Label(self.frame,text=" Place Stakeholders \n on Position Spectrum ",bg="OrangeRed4",fg="white",font="Times 40").grid(row=11,column=1,pady=30)

		self.frame.bind("<Configure>", self.myfunction)

	def data(self):
	
		count = 0
		for i in xrange(3,10,3):
			Label(self.frame, text=outcomes[count].get(), fg = "white", bg = "OrangeRed4", font = "Times 14 bold").grid(row = i, column = 1, pady=10)
			Label(self.frame, text="           Most Conservative", fg="white", bg="gray15").grid(row = i + 1, column = 0)
			#Sliding Scale
			outcomesnum.append(Scale(self.frame, from_=0, to=100, tickinterval=10, showvalue=False,length=550, bg="gray15", fg="white", orient=HORIZONTAL))
			outcomesnum[count].grid(row = i + 1, column = 1,pady=40)
			outcomesnum[count].set(50)
			count += 1
			Label(self.frame, text=" ", width=10, bg="gray15").grid(row = i + 1, column = 2)
			Label(self.frame, text="Most Liberal", fg="white", bg="gray15").grid(row = i + 1, column = 2, padx = 8)
		
		count = 0
		for i in xrange(12,40,3):
			Label(self.frame, text=skholder[count][nameindex], fg = "white", bg = "OrangeRed4", font = "Times 14 bold").grid(row = i, column = 1, pady=10)
			Label(self.frame, text="           Most Conservative", fg="white", bg="gray15").grid(row = i+1, column=0)
			#Sliding Scale
			skholder[count][positionindex] = Scale(self.frame, from_=0, to=100, tickinterval=10, showvalue=False,length=550, bg="gray15", fg="white", orient=HORIZONTAL)
			skholder[count][positionindex].grid(row = i + 1, column = 1,pady=40)
			skholder[count][positionindex].set(50)
			count += 1
			Label(self.frame, text="Most Liberal", fg="white", bg="gray15").grid(row = i+1, column=2, pady = 8)

	def getScales(self):
		for i in skholder:
			i[positionindex] = i[positionindex].get()
			
	def myfunction(self,event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=900,height=650)
		
	def combiner(self, controller):
		controller.show_frame(PageEight)
		controller.frames[PageSeven].getScales()
		self.button.destroy()		
		#Position vs. Influence
		
		dictinfluence = {}
		dictposition = {}
		
		for i in skholder:
			dictinfluence[i[nameindex]] = i[influenceindex]
			dictposition[i[nameindex]] = i[positionindex]
		
		positionInfluence = [{'value':(dictinfluence[x[nameindex]], dictposition[x[nameindex]]), 'label': x[nameindex]} for x in skholder]
		influencesum = float(sum(x[influenceindex] for x in skholder))
		meanstkholder = sum((x[positionindex] * (x[influenceindex]/influencesum)) for x in skholder)
		
		xy_chart = pygal.XY(stroke=False,print_labels=True,show_x_guides=True, show_y_labels=False, x_title='Stakeholder Positions', y_title='Influence')
		xy_chart.title = casename[0] + '\n Stakeholder Analytics'
		xy_chart.x_labels = ({ 'label': outcomes[0].get(), 'value': outcomesnum[0].get()}, { 'label': outcomes[1].get(), 'value': outcomesnum[1].get()}, { 'label': outcomes[2].get(), 'value': outcomesnum[2].get()})
		xy_chart.add("Stakeholders", positionInfluence, dots_size=10)
		xy_chart.add("Mean Stakeholder",[{'value':(meanstkholder, 50), 'label':""}], dots_size=12)
		#xy_chart.yaxis.set_visible(False)
		xy_chart.render_to_file('Stakeholders Positions vs. Influence.svg') 
			
class PageEight(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.label = Label(self, text="Stakeholder Analytics \n Complete",font="Times 60",fg="Red",bg="gray15",width=25).place(relx=0.5, rely=0.5, anchor=CENTER)
		Frame.configure(self,background="gray15")

app = Transition()

app.title("Stakeholder Analytics")

app.resizable(width=FALSE, height=FALSE)

app.mainloop()


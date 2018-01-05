import tkinter

canvas = tkinter.Canvas()



def upgrade_screen(self):
	self.controls =1
	self.canvas.delete('all')
	for button in self.deletableButtons:
		button.destroy()

	self.canvas.create_rectangle(0,0,605,705,fill='white')

	self.canvas.create_text(50,50, text=['coins:' +str(self.coins)], font='Arial 15 bold',tags='coin_text')
	self.canvas.create_text(300, 50, text='cost of upgrade: 70' , font='Arial 15 bold')

	button = tkinter.Button(width=12, height=1, text='Home_screen', font='Arial 8 bold', command=self.Start)
	button.place(x=300, y=680, anchor="c")
	self.deletableButtons.append(button)

	commands = [
		self.number1,
		self.number2,
		self.number3,
		self.number4,
	]
	for i in range(4):
		self.canvas.create_text(self.buttonXPositions[i], 630, text='locked', tags='locked4')
		button = tkinter.Button(width=8, text='plane' + str(i + 1), font='Arial 8 bold', command=commands[i])
		button.place(x=self.buttonXPositions[i], y=650, anchor="c")

		self.deletableButtons.append(button)

	shield_commands=[
		self.s_number1,
		self.s_number2,
		self.s_number3,
		self.s_number4,
	]

	for i in range(4):
		self.canvas.create_text(self.buttonXPositions[i], 530, text='locked', tags='locked3')
		button = tkinter.Button(width=8, height=1, text='shield' + str(i + 1), font='Arial 8 bold', command=shield_commands[i])
		button.place(x=self.buttonXPositions[i], y=550, anchor="c")
		self.deletableButtons.append(button)

	endurance=[
		self.endurance1,
		self.endurance2,
		self.endurance3,
		self.endurance4,

	]
	for i in range(4):
		self.canvas.create_text(self.buttonXPositions[i], 430, text='locked', tags='locked2')
		button = tkinter.Button(width=8, height=1, text='Endurance', font='Arial 8 bold', command=endurance[i])
		button.place(x=self.buttonXPositions[i], y=450, anchor="c")
		self.deletableButtons.append(button)

	max_number=[
		self.max_number1,
		self.max_number2,
		self.max_number3,
		self.max_number4,
	]

	for i in range(4):
		self.canvas.create_text(self.buttonXPositions[i], 330, text='locked', tags='locked1')
		button = tkinter.Button(width=8, height=1, text='shi. to use', font='Arial 8 bold', command=max_number[i])
		button.place(x=self.buttonXPositions[i], y=350, anchor="c")
		self.deletableButtons.append(button)

	locked1(self)
	locked2(self)
	locked3(self)
	locked4(self)
	highlights1(self)
	highlights2(self)
	highlights3(self)
	highlights4(self)



	createInitPlanes(self)
	createInitShields(self)
	maximal(self)
	endurance_number(self)

def highlights1(self):
	if self.position_locked1 == 1:
		self.max_number1()
	elif self.position_locked1 == 2:
		self.max_number2()
	elif self.position_locked1 == 3:
		self.max_number3()
	elif self.position_locked1 == 4:
		self.max_number4()
def highlights2(self):
	if self.position_locked2 == 1:
		self.endurance1()
	elif self.position_locked2 == 2:
		self.endurance2()
	elif self.position_locked2 == 3:
		self.endurance3()
	elif self.position_locked2 == 4:
		self.endurance4()
def highlights3(self):
	if self.position_locked3 == 1:
		self.s_number1()
	elif self.position_locked3 == 2:
		self.s_number2()
	elif self.position_locked3 == 3:
		self.s_number3()
	elif self.position_locked3 == 4:
		self.s_number4()
def highlights4(self):
	if self.position_locked4 == 1:
		self.number1()
	elif self.position_locked4 == 2:
		self.number2()
	elif self.position_locked4 == 3:
		self.number3()
	elif self.position_locked4 == 4:
		self.number4()
def locked1(self):
	if self.unlock1 >= 4:
		self.canvas.delete('locked1')
		self.canvas.create_text(495, 330, text='unlocked', tags='locked1')
		self.canvas.create_text(104, 330, text='unlocked', tags='locked1')
		self.canvas.create_text(235, 330, text='unlocked', tags='locked1')
		self.canvas.create_text(370, 330, text='unlocked', tags='locked1')
	elif self.unlock1 >= 3:
		self.canvas.delete('locked1')
		self.canvas.create_text(370, 330, text='unlocked', tags='locked1')
		self.canvas.create_text(104, 330, text='unlocked', tags='locked1')
		self.canvas.create_text(235, 330, text='unlocked', tags='locked1')
		self.canvas.create_text(495, 330, text='locked', tags='locked1')
	elif self.unlock1 >= 2:
		self.canvas.delete('locked1')
		self.canvas.create_text(235, 330, text='unlocked', tags='locked1')
		self.canvas.create_text(104, 330, text='unlocked', tags='locked1')
		self.canvas.create_text(370, 330, text='locked', tags='locked1')
		self.canvas.create_text(495, 330, text='locked', tags='locked1')
	elif self.unlock1>=1:
		self.canvas.delete('locked1')
		self.canvas.create_text(104,330, text='unlocked',tags='locked1')
		self.canvas.create_text(235,330, text='locked',tags='locked1')
		self.canvas.create_text(370,330, text='locked',tags='locked1')
		self.canvas.create_text(495,330, text='locked',tags='locked1')



def locked2(self):
	if self.unlock2 >= 4:
		self.canvas.delete('locked2')
		self.canvas.create_text(495,430, text='unlocked',tags='locked2')
		self.canvas.create_text(104,430, text='unlocked',tags='locked2')
		self.canvas.create_text(235,430, text='unlocked',tags='locked2')
		self.canvas.create_text(370,430, text='unlocked',tags='locked2')
	elif self.unlock2 >= 3:
		self.canvas.delete('locked2')
		self.canvas.create_text(370,430, text='unlocked',tags='locked2')
		self.canvas.create_text(104,430, text='unlocked',tags='locked2')
		self.canvas.create_text(235,430, text='unlocked',tags='locked2')
		self.canvas.create_text(495,430, text='locked',tags='locked2')
	elif self.unlock2>=2:
		self.canvas.delete('locked2')
		self.canvas.create_text(235,430, text='unlocked',tags='locked2')
		self.canvas.create_text(104,430, text='unlocked',tags='locked2')
		self.canvas.create_text(370,430, text='locked',tags='locked2')
		self.canvas.create_text(495,430, text='locked',tags='locked2')
	elif self.unlock2>=1:
		self.canvas.delete('locked2')
		self.canvas.create_text(104,430, text='unlocked',tags='locked2')
		self.canvas.create_text(235,430, text='locked',tags='locked2')
		self.canvas.create_text(370,430, text='locked',tags='locked2')
		self.canvas.create_text(495,430, text='locked',tags='locked2')

def locked3(self):
	if self.unlock3 >= 4:
		self.canvas.delete('locked3')
		self.canvas.create_text(104, 530, text='unlocked', tags='locked3')
		self.canvas.create_text(235, 530, text='unlocked', tags='locked3')
		self.canvas.create_text(370, 530, text='unlocked', tags='locked3')
		self.canvas.create_text(495, 530, text='unlocked', tags='locked3')
	elif self.unlock3 >= 3:
		self.canvas.delete('locked3')
		self.canvas.create_text(104, 530, text='unlocked', tags='locked3')
		self.canvas.create_text(235, 530, text='unlocked', tags='locked3')
		self.canvas.create_text(370, 530, text='unlocked', tags='locked3')
		self.canvas.create_text(495, 530, text='locked', tags='locked3')
	elif self.unlock3>=2:
		self.canvas.delete('locked3')
		self.canvas.create_text(104, 530, text='unlocked', tags='locked3')
		self.canvas.create_text(235, 530, text='unlocked', tags='locked3')
		self.canvas.create_text(370, 530, text='locked', tags='locked3')
		self.canvas.create_text(495, 530, text='locked', tags='locked3')
	elif self.unlock3 >= 1:
		self.canvas.delete('locked3')
		self.canvas.create_text(104, 530, text='unlocked', tags='locked3')
		self.canvas.create_text(235, 530, text='locked', tags='locked3')
		self.canvas.create_text(370, 530, text='locked', tags='locked3')
		self.canvas.create_text(495, 530, text='locked', tags='locked3')
def locked4(self):
	if self.unlock4 >= 4:
		self.canvas.delete('locked4')
		self.canvas.create_text(104, 630, text='unlocked', tags='locked4')
		self.canvas.create_text(235, 630, text='unlocked', tags='locked4')
		self.canvas.create_text(370, 630, text='unlocked', tags='locked4')
		self.canvas.create_text(495, 630, text='unlocked', tags='locked4')
	elif self.unlock4 >= 3:
		self.canvas.delete('locked4')
		self.canvas.create_text(104, 630, text='unlocked', tags='locked4')
		self.canvas.create_text(235, 630, text='unlocked', tags='locked4')
		self.canvas.create_text(370, 630, text='unlocked', tags='locked4')
		self.canvas.create_text(495, 630, text='locked', tags='locked4')

	elif self.unlock4>=2:
		self.canvas.delete('locked4')
		self.canvas.create_text(104, 630, text='unlocked', tags='locked4')
		self.canvas.create_text(235, 630, text='unlocked', tags='locked4')
		self.canvas.create_text(370, 630, text='locked', tags='locked4')
		self.canvas.create_text(495, 630, text='locked', tags='locked4')
	elif self.unlock4 >= 1:
		self.canvas.delete('locked4')
		self.canvas.create_text(104, 630, text='unlocked', tags='locked4')
		self.canvas.create_text(235, 630, text='locked', tags='locked4')
		self.canvas.create_text(370, 630, text='locked', tags='locked4')
		self.canvas.create_text(495, 630, text='locked', tags='locked4')
def endurance_number(self):
	for i in range(4):
		self.canvas.create_text(self.buttonXPositions[i],200+200+5,text=[7+i],font='Arial 30 bold')


def maximal(self):
	for i in range(4):
		self.canvas.create_text(self.buttonXPositions[i], 100 + 200 + 5, text=[14 + (i*2)], font='Arial 30 bold')


def createInitPlanes (self) :
	colors = ('black','#1010D2','#70F736','#EF30F6')
	colors_outline=('#C63B3B','#70F736','black','#EF30F6')

	for i in range(len(colors)):
		self.canvas.create_oval(self.buttonXPositions[i]-7,400+210+15,self.buttonXPositions[i]+7,400+210-15,fill=colors[i],outline=colors_outline[i])
		self.canvas.create_oval(self.buttonXPositions[i]-14,400+200+5,self.buttonXPositions[i]+14,400+220-5,fill=colors[i],outline=colors_outline[i])

def createInitShields(self):

	colors = ('black','#1010D2','#70F736','#EF30F6')
	colors_outline=('#C63B3B','#70F736','black','#EF30F6')

	for i in range(len(colors)):
		self.canvas.create_oval(self.buttonXPositions[i]-14,300+200+5,self.buttonXPositions[i]+14,300+220-5,fill=colors[i],outline=colors_outline[i])
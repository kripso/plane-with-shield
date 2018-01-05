import random, time
from upgrade import*

class game():
	def __init__(self):

		self.canvas = tkinter.Canvas(
			width=600,
			height=700,
			bg='white'
			)

		self.canvas.pack()

		self.coins=0
		self.highscore=0
		self.unlock1=0
		self.unlock2=0
		self.unlock3=0
		self.unlock4=0
		self.position_locked1=0
		self.position_locked2=0
		self.position_locked3=0
		self.position_locked4=0
		self.control = 0
		self.controls = 0
		self.lvlmove = 0

		self.shield_upgrade_number=0

		self.shield_number = 0

		self.shield_endurance=6
		self.max_number_shields=12

		self.plane_number = 0
		self.control_bullet = 0
		self.obs_destroyed=0


		self.buttonXPositions = (104, 235, 370, 495)
		self.buttonYpositions = (680, 640, 600, 560)
		self.deletableButtons = []

		self.Start_screen()
		self.obstacles()
		self.point()
		self.lvl()
		self.cycle()

		self.canvas.mainloop()

	def hra(self):
		self.canvas.delete('all')

		for button in self.deletableButtons:
			button.destroy()

#   stred hracieho pola
		self.x=250
		self.y=400
#   sirka lietadla a kridla
		self.r1=7
		self.r2=15
#   dlzka lietadla a kridiel
		self.h1=15
		self.h2=5
#   rychlost akou sa pohybuju prekazky
		self.speed_of_obstacles=0.0005
		self.points_speed=5000
		self.generating_speed=200
		self.lvl_speed=10000
#   posunie zaciatocnu y suroadnicu nad canvas
		self.position=820

		self.lvlmove+=1
#   podmienka aby cykli fungovali ako maju pokym hra este nejde
		self.control=1
#   informacne pole
		self.canvas.create_rectangle(500,0,600,700,fill='black',tags='table')
#   aktualny a najvacsi pocet bodov
		self.points=5
		self.highscore=5
#   pociatocne vypisanie bodov
		self.canvas.create_text(550, 30, text='points: '+str(self.points), fill='#C63B3B',tags='text')
		self.canvas.create_text(550, 15, text='HS: '+str(self.highscore), fill='#C63B3B',tags='text')

#   pohyby
		self.canvas.bind_all('<Left>',self.moveleft)
		self.canvas.bind_all('<Right>',self.moveright)
		self.canvas.bind_all('<Up>',self.moveup)
		self.canvas.bind_all('<Down>',self.movedown)

		self.canvas.bind_all('<space>', self.defense)

		self.plane()
		self.side_buttons()

	def Start_screen(self):
		if self.controls == 0:
			self.Start()
		else:
			self.Start()
			self.canvas.create_text(300, 50, text='Highest Score: '+str(self.highscore),font= 'Arial 30 bold', fill='#C63B3B')
			self.canvas.create_text(300, 450, text='Game over', font='Arial 40 bold', fill='#C63B3B')
			self.canvas.update()

		self.canvas.update()

	def Start(self):
		self.canvas.delete('all')
		for button in self.deletableButtons:
			button.destroy()


		self.canvas.create_text(300, 600, text=['coins:' + str(self.coins)], font='Arial 30 bold', tags='coin_text')

		button = tkinter.Button (width=15, height=3,  text='Start the Game', font='Arial 20 bold', activeforeground='#1010D2', command=self.hra)
		button.place (x=300, y=250, anchor="c")
		self.deletableButtons.append(button)

		button = tkinter.Button(width=12, height=1,  text='Upgrade screen', font='Arial 15 bold', activeforeground='#1010D2', command=self._upgrade_screen)
		button.place (x=300, y=680, anchor="c")
		self.deletableButtons.append(button)

	def _upgrade_screen(self):
		upgrade_screen(self)

	def side_buttons(self):
		button = tkinter.Button (width=9,height=1,  text='Nová hra', font= 'Arial 10 bold', activeforeground= '#1010D2',fg='#C63B3B', command= self.New_game)
		button.place (x=551, y=self.buttonYpositions[0], anchor="c")
		self.deletableButtons.append(button)

		lvls=[
			self.lvl1click,
			self.lvl2click,
			self.lvl3click
		]
		for i in range(3):
			button = tkinter.Button (width=9,height=1,  text='lvl' + str(i+1), font= 'Arial 10 bold', activeforeground= '#1010D2', command = lvls[i])
			button.place(x=551, y=self.buttonYpositions[i+1], anchor="c")
			self.deletableButtons.append(button)
			
	def lvl(self):
		if self.lvlmove>0:
			if self.generating_speed<=160:
				self.lvl2()
				self.canvas.after(self.lvl_speed,self.lvl)

			elif self.generating_speed<=130:
				self.lvl3()
				self.canvas.after(self.lvl_speed,self.lvl)

			else:
				self.lvl1()
				self.canvas.after(self.lvl_speed,self.lvl)

		elif self.lvlmove==0:
			self.canvas.after(200,self.lvl)

	def lvl1(self):
		self.generating_speed=self.generating_speed-10

	def lvl2(self):
		self.generating_speed=self.generating_speed-5

	def lvl3(self):
		self.generating_speed=self.generating_speed-3

	def lvl1click(self):
		self.generating_speed=200
		self.points=5
		self.highscore=5

	def lvl2click(self):
		self.generating_speed=160
		self.points=40
		self.highscore=40


	def lvl3click(self):
		self.generating_speed=130
		self.points=70
		self.highscore=70


	def obstacles(self):
		self.x2=random.randint(0, 500)
		self.y2=random.randint(0, 800)
		self.r1=random.randint(5, 16)

		if self.control==0:
			self.canvas.after(200,self.obstacles)

		elif self.generating_speed<=130:
			self.canvas.create_rectangle(self.x2-self.r1,self.y2-self.position-self.r1,self.x2+self.r1,self.y2-self.position+self.r1,fill='black',outline='#C63B3B',tags='obs')
			self.canvas.after(self.generating_speed, self.obstacles)

		elif self.generating_speed<=160:
			self.canvas.create_rectangle(self.x2-self.r1,self.y2-self.position-self.r1,self.x2+self.r1,self.y2-self.position+self.r1,fill='#C63B3B',outline='#1010D2',tags='obs')
			self.canvas.after(self.generating_speed, self.obstacles)

		else:
			self.canvas.create_rectangle(self.x2-self.r1,self.y2-self.position-self.r1,self.x2+self.r1,self.y2-self.position+self.r1,fill='#1010D2',outline='#70F736',tags='obs')
			self.canvas.after(self.generating_speed, self.obstacles)
		self.canvas.tag_lower ('obs')

		self.canvas.update()

	def plane(self):
		colors = [
			('black', '#C63B3B'),
			('#1010D2', '#70F736'),
			('#70F736', 'black'),
			('#EF30F6', '#EF30F6'),
		]
		color = colors[(self.plane_number)-1] if self.plane_number > 0 else ('black', 'black')

		self.canvas.create_oval(self.x-self.r1,self.y+285+self.h1,self.x+self.r1,self.y+285-self.h1,fill=color[0],outline=color[1],tags='plane')
		x1, y1, x2, y2 = self.canvas.coords('plane')

		self.canvas.create_oval(self.x-self.r2,self.y+275+self.h2,self.x+self.r2,self.y+295-self.h2,fill=color[0],outline=color[1],tags=['plane1', 'plane'])
		x1, y1, x2, y2 = self.canvas.coords('plane1')

		self.canvas.create_oval(self.x-self.r1,self.y+285+self.h1,self.x+self.r1,self.y+285-self.h1,fill=color[0],outline=color[1],tags='shield')
		x1, y1, x2, y2 = self.canvas.coords('shield')
		self.canvas.delete('shield')


	def point(self):
		if self.control==0:
			self.canvas.after(1000,self.point)
		elif self.points>0:
			self.points=self.points+5
			self.canvas.after(self.points_speed,self.point)
		else:
			self.canvas.after(1000,self.point)
		self.canvas.update()

	def high(self):
		if self.highscore<self.points:
			self.highscore=self.points

	def New_game(self):
		self.points=0

	def cycle (self) :
		self.canvas.update()

		if self.control==0:
			self.canvas.after(1000,self.cycle)

		else:
			while self.control>0:
				time.sleep(self.speed_of_obstacles)

				self.canvas.move('obs', 0, +2)
				self.high()
				self.canvas.delete('text')
				self.canvas.create_text(550, 30, text='points: '+str(self.points), fill='#C63B3B',tags='text')
				self.canvas.create_text(550, 15, text='HS: '+str(self.highscore), fill='#C63B3B',tags='text')

				tagged_objects = self.canvas.find_withtag('obs')
				overlapping_objects = self.canvas.find_overlapping(*self.canvas.coords('plane'))

				for item in overlapping_objects:
					if item in tagged_objects:
						if self.points>0:
							self.points=self.points-0.5

				if self.points<=0:
					self.controls=100
					self.control=0
					self.control_bullet=0
					self.coins = self.coins + self.highscore
					self.Start_screen()
					self.canvas.after(20,self.cycle)
					return False

				self.canvas.coords('shield')

				if self.control_bullet>0:
					if self.obs_destroyed<self.shield_endurance-1:

						tagged_objects = self.canvas.find_withtag('obs')
						overlapping_objects = self.canvas.find_overlapping(*self.canvas.coords('shield'))
						for item in overlapping_objects:
							if item in tagged_objects:
								self.canvas.delete(item)
								self.obs_destroyed+=1
					else:
						tagged_objects = self.canvas.find_withtag('obs')
						overlapping_objects = self.canvas.find_overlapping(*self.canvas.coords('shield'))
						for item in overlapping_objects:
							if item in tagged_objects:
								self.canvas.delete(item)
								self.canvas.delete('shield')
								self.control_bullet=0
								self.obs_destroyed=0
				self.canvas.update()

	def max_number1(self):
		if self.unlock1 >= 1:
			self.max_number_shields = 14
			self.canvas.delete('highlight2')
			self.canvas.create_rectangle(104 - 33, 100 + 210 + 40, 104 + 33, 100 + 210 - 40, fill='lightblue',
			                             tags='highlight2')
			maximal(self)
			locked1(self)
			self.position_locked1 = 1

		elif self.coins>=70:
			if self.unlock1==0:
				self.max_number_shields = 14
				self.unlock1=1
				self.position_locked1=1
				self.canvas.delete('highlight2')
				self.canvas.create_rectangle(104 - 33, 100 + 210 + 40, 104 + 33, 100 + 210 - 40, fill='lightblue',
					                             tags='highlight2')
				maximal(self)

				self.coins-=70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50,50, text=['coins:' +str(self.coins)], font='Arial 15 bold',tags='coin_text')
				locked1(self)

	def max_number2(self):
		if self.unlock1>=2:
			self.max_number_shields = 16
			self.canvas.delete('highlight2')
			self.canvas.create_rectangle(235 - 33, 100 + 210 + 40, 235 + 33, 100 + 210 - 40, fill='lightblue',
				                             tags='highlight2')
			maximal(self)
			locked1(self)
			self.position_locked1 = 2

		elif self.coins>=70:
			if self.unlock1==1:
				self.max_number_shields = 16
				self.canvas.delete('highlight2')
				self.canvas.create_rectangle(235 - 33, 100 + 210 + 40, 235 + 33, 100 + 210 - 40, fill='lightblue',
					                             tags='highlight2')
				maximal(self)
				self.coins-=70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50,50, text=['coins:' +str(self.coins)], font='Arial 15 bold',tags='coin_text')
				self.unlock1=2
				locked1(self)
				self.position_locked1 = 2



	def max_number3(self):
		if self.unlock1>=3:
			self.max_number_shields = 18
			self.canvas.delete('highlight2')
			self.canvas.create_rectangle(370 - 33, 100 + 210 + 40, 370 + 33, 100 + 210 - 40, fill='lightblue',
				                             tags='highlight2')
			maximal(self)
			locked1(self)
			self.position_locked1 = 3

		elif self.coins>=70:
			if self.unlock1==2:
				self.max_number_shields = 18
				self.canvas.delete('highlight2')
				self.canvas.create_rectangle(370 - 33, 100 + 210 + 40, 370 + 33, 100 + 210 - 40, fill='lightblue',
					                             tags='highlight2')
				maximal(self)
				self.coins-=70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50,50, text=['coins:' +str(self.coins)], font='Arial 15 bold',tags='coin_text')
				self.unlock1=3
				locked1(self)
				self.position_locked1 = 3


	def max_number4(self):
		if self.unlock1>=4:
			self.max_number_shields = 20
			self.canvas.delete('highlight2')
			self.canvas.create_rectangle(495 - 33, 100 + 210 + 40, 495 + 33, 100 + 210 - 40, fill='lightblue',
				                             tags='highlight2')
			maximal(self)
			locked1(self)
			self.position_locked1 = 4

		elif self.coins>=70:
			if self.unlock1==3:
				self.max_number_shields = 20
				self.canvas.delete('highlight2')
				self.canvas.create_rectangle(495 - 33, 100 + 210 + 40, 495 + 33, 100 + 210 - 40, fill='lightblue',
					                             tags='highlight2')
				maximal(self)
				self.coins-=70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50,50, text=['coins:' +str(self.coins)], font='Arial 15 bold',tags='coin_text')
				self.unlock1=4
				locked1(self)
				self.position_locked1 = 4


	def endurance1(self):
		if self.unlock2>=1:
			self.shield_endurance=7
			self.canvas.delete('highlight3')
			self.canvas.create_rectangle(104 - 33, 200 + 210 + 40, 104 + 33, 200 + 210 - 40, fill='lightblue',
				                             tags='highlight3')
			endurance_number(self)
			locked2(self)
			self.position_locked2=1

		elif self.coins>=70:
			if self.unlock2==0:
				self.shield_endurance=7
				self.canvas.delete('highlight3')
				self.canvas.create_rectangle(104 - 33, 200 + 210 + 40, 104 + 33, 200 + 210 - 40, fill='lightblue',
					                             tags='highlight3')
				endurance_number(self)
				self.coins-=50
				self.canvas.delete('coin_text')
				self.canvas.create_text(50,50, text=['coins:' +str(self.coins)], font='Arial 15 bold',tags='coin_text')
				self.unlock2=1
				locked2(self)
				self.position_locked2=1

	def endurance2(self):
		if self.unlock2>=2:
			self.shield_endurance=8
			self.canvas.delete('highlight3')
			self.canvas.create_rectangle(235 - 33, 200 + 210 + 40, 235 + 33, 200 + 210 - 40, fill='lightblue',
				                             tags='highlight3')
			endurance_number(self)
			locked2(self)
			self.position_locked2=2

		elif self.coins>=70:
			if self.unlock2==1:
				self.shield_endurance=8
				self.canvas.delete('highlight3')
				self.canvas.create_rectangle(235 - 33, 200 + 210 + 40, 235 + 33, 200 + 210 - 40, fill='lightblue',
					                             tags='highlight3')
				endurance_number(self)
				self.coins-=70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50,50, text=['coins:' +str(self.coins)], font='Arial 15 bold',tags='coin_text')
				self.unlock2=2
				locked2(self)
				self.position_locked2=2

	def endurance3(self):
		if self.unlock2>=3:
			self.shield_endurance=9
			self.canvas.delete('highlight3')
			self.canvas.create_rectangle(370 - 33, 200 + 210 + 40, 370 + 33, 200 + 210 - 40, fill='lightblue',
				                             tags='highlight3')
			endurance_number(self)
			locked2(self)
			self.position_locked2=3

		elif self.coins>=70:
			if self.unlock2==2:
				self.shield_endurance=9
				self.canvas.delete('highlight3')
				self.canvas.create_rectangle(370 - 33, 200 + 210 + 40, 370 + 33, 200 + 210 - 40, fill='lightblue',
					                             tags='highlight3')
				endurance_number(self)
				self.coins-=70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50,50, text=['coins:' +str(self.coins)], font='Arial 15 bold',tags='coin_text')
				self.unlock2=3
				locked2(self)
				self.position_locked2=3

	def endurance4(self):

		if self.unlock2>=4:
			self.shield_endurance=10
			self.canvas.delete('highlight3')
			self.canvas.create_rectangle(495 - 33, 200 + 210 + 40, 495 + 33, 200 + 210 - 40, fill='lightblue',
				                             tags='highlight3')
			endurance_number(self)
			locked2(self)
			self.position_locked2=4


		elif self.coins>=70:
			if self.unlock2==3:
				self.shield_endurance=10
				self.canvas.delete('highlight3')
				self.canvas.create_rectangle(495 - 33, 200 + 210 + 40, 495 + 33, 200 + 210 - 40, fill='lightblue',
					                             tags='highlight3')
				endurance_number(self)
				self.coins-=70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50,50, text=['coins:' +str(self.coins)], font='Arial 15 bold',tags='coin_text')
				self.unlock2=4
				locked2(self)
				self.position_locked2=4

	def defense(self,event):
		colors = [
			('black', '#C63B3B'),
			('#1010D2', '#70F736'),
			('#70F736', 'black'),
			('#EF30F6', '#EF30F6'),
		]
		color = colors[(self.shield_upgrade_number) - 1] if self.shield_upgrade_number > 0 else ('black', 'black')

		if self.control_bullet==0:
			x1, y1, x2, y2 = self.canvas.coords('plane1')
			y1-=25
			y2-=25

			if self.shield_number<self.max_number_shields:
				self.canvas.create_oval(x1, y1, x2, y2,fill=color[0],outline=color[1], tags='shield')
				self.canvas.tag_lower('shield')
				self.shield_number+=1
				self.control_bullet=1

	def shields(self):
		colors = [
			('black', '#C63B3B'),
			('#1010D2', '#70F736'),
			('#70F736', 'black'),
			('#EF30F6', '#EF30F6'),
		]
		color = colors[(self.shield_upgrade_number) - 1] if self.shield_upgrade_number > 0 else ('black', 'black')

		self.canvas.create_oval(self.x - self.r1, self.y + 285 + self.h1, self.x + self.r1,
		                        self.y + 285 - self.h1, fill=color[0], outline=color[1], tags='plane')
		x1, y1, x2, y2 = self.canvas.coords('plane')

	def s_number1(self):
		if self.unlock3>=1:
			self.canvas.delete('highlight1')
			self.shield_upgrade_number = 1
			self.canvas.create_rectangle(104 - 33, 300 + 210 + 40, 104 + 33, 300 + 210 - 40, fill='lightblue',
			                             tags='highlight1')
			createInitShields(self)
			locked3(self)
			self.position_locked3 =1

		elif self.coins>=70:
			if self.unlock3==0:
				self.canvas.delete('highlight1')
				self.shield_upgrade_number = 1
				self.canvas.create_rectangle(104 - 33, 300 + 210 + 40, 104 + 33, 300 + 210 - 40, fill='lightblue',
				                             tags='highlight1')
				createInitShields(self)
				self.coins-=70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50,50, text=['coins:' +str(self.coins)], font='Arial 15 bold',tags='coin_text')
				self.unlock3=1
				locked3(self)
				self.position_locked3=1


	def s_number2(self):
		if self.unlock3>=2:
			self.canvas.delete('highlight1')
			self.shield_upgrade_number = 2
			self.canvas.create_rectangle(235 - 33, 300 + 210 + 40, 235 + 33, 300 + 210 - 40, fill='lightblue',
			                             tags='highlight1')
			createInitShields(self)
			locked3(self)
			self.position_locked3 =2

		elif self.coins>=70:
			if self.unlock3>=1:
				self.canvas.delete('highlight1')
				self.shield_upgrade_number = 2
				self.canvas.create_rectangle(235 - 33, 300 + 210 + 40, 235 + 33, 300 + 210 - 40, fill='lightblue',
				                             tags='highlight1')
				createInitShields(self)
				self.coins -= 70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50, 50, text=['coins:' + str(self.coins)], font='Arial 15 bold', tags='coin_text')
				self.unlock3=2
				locked3(self)
				self.position_locked3=2

	def s_number3(self):
		if self.unlock3>=3:
			self.canvas.delete('highlight1')
			self.shield_upgrade_number = 3
			self.canvas.create_rectangle(370 - 33, 300 + 210 + 40, 370 + 33, 300 + 210 - 40, fill='lightblue',
			                             tags='highlight1')
			createInitShields(self)
			locked3(self)
			self.position_locked3 =3

		elif self.coins >= 70:
			if self.unlock3 >= 2:
				self.canvas.delete('highlight1')
				self.shield_upgrade_number = 3
				self.canvas.create_rectangle(370 - 33, 300 + 210 + 40, 370 + 33, 300 + 210 - 40, fill='lightblue',
				                             tags='highlight1')
				createInitShields(self)
				self.coins -= 70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50, 50, text=['coins:' + str(self.coins)], font='Arial 15 bold', tags='coin_text')
				self.unlock3 =3
				locked3(self)
				self.position_locked3=3

	def s_number4(self):
		if self.coins >= 70:
			if self.unlock3 >= 3:
				self.canvas.delete('highlight1')
				self.shield_upgrade_number = 4
				self.canvas.create_rectangle(495 - 33, 300 + 210 + 40, 495 + 33, 300 + 210 - 40, fill='lightblue',
				                             tags='highlight1')
				createInitShields(self)
				self.coins -= 70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50, 50, text=['coins:' + str(self.coins)], font='Arial 15 bold', tags='coin_text')
				self.unlock3=4
				locked3(self)
				self.position_locked3=4

		elif self.unlock3>=4:
			self.canvas.delete('highlight1')
			self.shield_upgrade_number = 4
			self.canvas.create_rectangle(495 - 33, 300 + 210 + 40, 495 + 33, 300 + 210 - 40, fill='lightblue',
			                             tags='highlight1')
			createInitShields(self)
			locked3(self)
			self.position_locked3 =4

	def number1(self):
		if self.unlock4>=1:
			self.canvas.delete('highlight')
			self.plane_number = 1
			self.canvas.create_rectangle(104 - 33, 400 + 210 + 40, 104 + 33, 400 + 210 - 40, fill='lightblue',
			                             tags='highlight')
			createInitPlanes(self)
			locked4(self)
			self.position_locked4 =1

		elif self.coins >= 70:
			if self.unlock4 >= 0:
				self.canvas.delete('highlight')
				self.plane_number = 1
				self.canvas.create_rectangle(104 - 33, 400 + 210 + 40, 104 + 33, 400 + 210 - 40, fill='lightblue',
				                             tags='highlight')
				createInitPlanes(self)
				self.coins -= 70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50, 50, text=['coins:' + str(self.coins)], font='Arial 15 bold', tags='coin_text')
				self.unlock4=1
				locked4(self)
				self.position_locked4=1

	def number2(self):
		if self.unlock4>=2:
			self.canvas.delete('highlight')
			self.plane_number = 2
			self.canvas.create_rectangle(235 - 33, 400 + 210 + 40, 235 + 33, 400 + 210 - 40, fill='lightblue',
			                             tags='highlight')
			createInitPlanes(self)
			locked4(self)
			self.position_locked4 =2

		elif self.coins >= 70:
			if self.unlock4 >= 1:
				self.canvas.delete('highlight')
				self.plane_number = 2
				self.canvas.create_rectangle(235 - 33, 400 + 210 + 40, 235 + 33, 400 + 210 - 40, fill='lightblue',
				                             tags='highlight')
				createInitPlanes(self)
				self.coins -= 70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50, 50, text=['coins:' + str(self.coins)], font='Arial 15 bold', tags='coin_text')
				self.unlock4=2
				locked4(self)
				self.position_locked4=2

	def number3(self):
		if self.unlock4>=3:
			self.canvas.delete('highlight')
			self.plane_number = 3
			self.canvas.create_rectangle(370 - 33, 400 + 210 + 40, 370 + 33, 400 + 210 - 40, fill='lightblue',
			                             tags='highlight')
			createInitPlanes(self)
			locked4(self)
			self.position_locked4 =3

		elif self.coins >= 70:
			if self.unlock4 >= 2:
				self.canvas.delete('highlight')
				self.plane_number = 3
				self.canvas.create_rectangle(370 - 33, 400 + 210 + 40, 370 + 33, 400 + 210 - 40, fill='lightblue',
				                             tags='highlight')
				createInitPlanes(self)
				self.coins -= 70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50, 50, text=['coins:' + str(self.coins)], font='Arial 15 bold', tags='coin_text')
				self.unlock4=3
				locked4(self)
				self.position_locked4=3

	def number4(self):
		if self.unlock4>=4:
			self.canvas.delete('highlight')
			self.plane_number = 4
			self.canvas.create_rectangle(495 - 33, 400 + 210 + 40, 495 + 33, 400 + 210 - 40, fill='lightblue',
			                             tags='highlight')
			createInitPlanes(self)
			locked4(self)
			self.position_locked4 =4

		elif self.coins >= 70:
			if self.unlock4 >= 3:
				self.canvas.delete('highlight')
				self.plane_number = 4
				self.canvas.create_rectangle(495 - 33, 400 + 210 + 40, 495 + 33, 400 + 210 - 40, fill='lightblue',
				                             tags='highlight')
				createInitPlanes(self)
				self.coins -= 70
				self.canvas.delete('coin_text')
				self.canvas.create_text(50, 50, text=['coins:' + str(self.coins)], font='Arial 15 bold', tags='coin_text')
				self.unlock4=4
				locked4(self)
				self.position_locked4=4

	def moveright (self,event):
		x1, y1, x2, y2 = self.canvas.coords('plane')
		x1, y1, x2, y2 = x1+10, y1, x2+10, y2
		self.canvas.coords('plane', x1, y1, x2, y2)
		x1, y1, x2, y2 = self.canvas.coords('plane1')
		x1, y1, x2, y2 = x1+10, y1, x2+10, y2
		self.canvas.coords('plane1', x1, y1, x2, y2)
		if self.control_bullet > 0:
			x1, y1, x2, y2 = self.canvas.coords('shield')
			x1, y1, x2, y2 = x1+10, y1, x2+10, y2
			self.canvas.coords('shield', x1, y1, x2, y2)

	def moveleft (self,event):
		x1, y1, x2, y2 = self.canvas.coords('plane')
		x1, y1, x2, y2 = x1-10, y1, x2-10, y2
		self.canvas.coords('plane', x1, y1, x2, y2)
		x1, y1, x2, y2 = self.canvas.coords('plane1')
		x1, y1, x2, y2 = x1-10, y1, x2-10, y2
		self.canvas.coords('plane1', x1, y1, x2, y2)
		if self.control_bullet > 0:
			x1, y1, x2, y2 = self.canvas.coords('shield')
			x1, y1, x2, y2 = x1-10, y1, x2-10, y2
			self.canvas.coords('shield', x1, y1, x2, y2)

	def moveup(self, event):
		x1, y1, x2, y2 = self.canvas.coords('plane')
		x1, y1, x2, y2 = x1, y1-10, x2, y2-10
		self.canvas.coords('plane', x1, y1, x2, y2)
		x1, y1, x2, y2 = self.canvas.coords('plane1')
		x1, y1, x2, y2 = x1, y1-10, x2, y2-10
		self.canvas.coords('plane1', x1, y1, x2, y2)
		if self.control_bullet > 0:
			x1, y1, x2, y2 = self.canvas.coords('shield')
			x1, y1, x2, y2 = x1, y1-10, x2, y2-10
			self.canvas.coords('shield', x1, y1, x2, y2)

	def movedown(self, event):
		x1, y1, x2, y2 = self.canvas.coords('plane')
		x1, y1, x2, y2 = x1, y1+10, x2, y2+10
		self.canvas.coords('plane', x1, y1, x2, y2)
		x1, y1, x2, y2 = self.canvas.coords('plane1')
		x1, y1, x2, y2 = x1, y1+10, x2, y2+10
		self.canvas.coords('plane1', x1, y1, x2, y2)
		if self.control_bullet > 0:
			x1, y1, x2, y2 = self.canvas.coords('shield')
			x1, y1, x2, y2 = x1, y1+10, x2, y2+10
			self.canvas.coords('shield', x1, y1, x2, y2)

game()

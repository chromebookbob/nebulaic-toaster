import random



class Inventory(object):
#  This class contains code which stores the amount of:
# uranium
# scrap and
# missiles
# a user has.
	uranium = 7
	scrap = 20
	missiles = 7
	
	def uranium_store(self, add, minus):
		self.uranium += add
		self.uranium = self.uranium - minus
		if self.uranium < 4:
			return "DANGER: %d URANIUM REMAINING" % self.uranium
		elif self.uranium >= 4:
			return "%d" % self.uranium	
	
	def scrap_store(self, add, minus):
		self.scrap
		self.scrap += add
		self.scrap -= minus
		return self.scrap
		
	def missile_store(self, add, fire):
		self.missiles
		self.missiles += add
		self.missiles -= fire
		if self.missiles > 0:
			return self.missiles
		else:
			return "NO MISSILES"			


class Random(object):
	def starnear(self, name, computer_name):
		stars = [Stars().star1, Stars().star2, Stars().star3, Stars().star4, Stars().star5]
		random.choice(stars)(name, computer_name)				
		
	def starfar(self, name, computer_name):
		stars = [Stars().stara, stars.starb, stars.starc, stars.stard]
		random.choice(stars)(name, computer_name)	
		
	def coordinates(self):
		ac = random.uniform(-60, 60)
		bc = random.uniform(-60, 60)
		cc = random.uniform(-60, 60)
		return u" %d\xb0 %d' %d\" " % (ac, bc, cc)	
		
	def star(self):
		star_list = ["ACAMAR", "ACHERNAR", "Achird", "ACRUX", "Acubens", "ADARA", "Adhafera", "Adhil", "AGENA", "Ain-al-Rami", "Ain", "Aladfar", "Alathfar", "Albaldah", "Albali", "ALBIREO", "Alchiba", "ALCOR", "ALCYONE", "ALDEBARAN", "ALDERAMIN", "Aldhibah", "Alfecca-Meridiana", "Alfirk", "ALGENIB", "ALGIEBA", "ALGOL", "Algorab", "ALHENA", "ALIOTH", "ALKAID", "Alkalurops", "Alkes", "Alkurhah", "ALMAAK", "ALNAIR", "ALNATH", "ALNILAM", "ALNITAK", "Alniyat", "Alniyat", "ALPHARD", "ALPHEKKA", "ALPHERATZ", "Alrai", "Alrisha", "Alsafi", "Alsciaukat", "ALSHAIN", "Alshat", "Alsuhail", "ALTAIR", "Altarf", "Alterf", "Aludra", "Alula-Australis", "Alula-Borealis", "Alya", "Alzirr", "Ancha", "Angetenar", "ANKAA", "Anser", "ANTARES", "ARCTURUS", "Arkab-Posterior", "Arkab-Prior", "ARNEB", "Arrakis", "Ascella", "Asellus Australis", "Asellus-Borealis", "Asellus-Primus", "Asellus-Secondus", "Asellus-Tertius", "Asterope", "Atik", "Atlas", "Auva", "Avior", "Azelfafage", "Azha", "Azmidiske", "Baham", "Baten Kaitos", "Becrux", "Beid", "BELLATRIX", "BETELGEUSE", "Botein", "Brachium", "CANOPUS", "CAPELLA", "Caph", "CASTOR", "Cebalrai", "Celaeno", "Chara", "Chort", "COR-CAROLI", "Cursa", "Dabih", "DENEB", "DENEBOLA", "Dheneb", "Diadem", "DIPHDA", "Double-Double-(7051)", "Dschubba", "Dsiban", "DUBHE", "Ed-Asich", "Electra", "ELNATH", "ENIF", "ETAMIN", "FOMALHAUT", "Fornacis", "Fum-al-Samakah", "Furud", "Gacrux", "Gianfar", "Gienah-Cygni", "Gienah-Ghurab", "Gomeisa", "Gorgonea-Quarta", "Gorgonea-Secunda", "Gorgonea-Tertia", "Graffias", "Grafias", "Grumium", "HADAR", "Haedi", "HAMAL", "Hassaleh", "Head-of-Hydrus", "Herschel's-Garnet Star", "Heze", "Hoedus-II", "Homam", "Hyadum-I", "Hyadum-II", "IZAR", "Jabbah", "Kaffaljidhma", "Kajam", "KAUS-AUSTRALIS", "Kaus-Borealis", "Kaus-Meridionalis", "Keid", "Kitalpha", "KOCAB", "Kornephoros", "Kraz", "Kuma", "Lesath", "Maasym", "Maia", "Marfak", "Marfak", "Marfic", "Marfik", "MARKAB", "Matar", "Mebsuta", "MEGREZ", "Meissa", "Mekbuda", "Menkalinan", "MENKAR", "Menkar", "Menkent", "Menkib", "MERAK", "Merga", "Merope", "Mesarthim", "Metallah", "Miaplacidus", "Minkar", "MINTAKA", "MIRA", "MIRACH", "Miram", "MIRPHAK", "MIZAR", "Mufrid", "Muliphen", "Murzim", "Muscida", "Muscida", "Muscida", "Nair-al-Saif", "Naos", "Nash", "Nashira", "Nekkar", "NIHAL", "Nodus-Secundus", "NUNKI", "Nusakan", "Peacock", "PHAD", "Phaet", "Pherkad Minor", "Pherkad", "Pleione", "Polaris-Australis", "POLARIS", "POLLUX", "Porrima", "Praecipua", "Prima Giedi", "PROCYON", "Propus", "Propus", "Propus", "Rana", "Ras-Elased-Australis", "Ras-Elased-Borealis", "RASALGETHI", "RASALHAGUE", "Rastaban", "REGULUS", "Rigel-Kentaurus", "RIGEL", "Rijl-al-Awwa", "Rotanev", "Ruchba", "Ruchbah", "Rukbat", "Sabik", "Sadalachbia", "SADALMELIK", "Sadalsuud", "Sadr", "SAIPH", "Salm", "Sargas", "Sarin", "Sceptrum", "SCHEAT", "Secunda-Giedi", "Segin", "Seginus", "Sham", "Sharatan", "SHAULA", "SHEDIR", "Sheliak", "SIRIUS", "Situla", "Skat", "SPICA", "Sterope-II", "Sualocin", "Subra", "Suhail-al-Muhlif", "Sulafat", "Syrma", "Tabit-(1543)", "Tabit-(1544)", "Tabit-(1552)", "Tabit-(1570)", "Talitha", "Tania-Australis", "Tania-Borealis", "TARAZED", "Taygeta", "Tegmen", "Tejat-Posterior", "Terebellum", "Terebellum", "Terebellum", "Terebellum", "Thabit", "Theemim", "THUBAN", "Torcularis-Septentrionalis", "Turais", "Tyl", "UNUKALHAI", "VEGA", "VINDEMIATRIX", "Wasat", "Wezen", "Wezn", "Yed-Posterior", "Yed-Prior", "Yildun", "Zaniah", "Zaurak", "Zavijah", "Zibal", "Zosma", "Zuben-Elakrab, Zuben-Elakribi, Zuben-Elgenubi, Zuben-Elschemali"]
		return random.choice(star_list)
	
	def action(self, name, computer_name):
		actions = [action1, action2, action3, action4]
		random.choice(actions)(name, computer_name)
		
	def alien(self):
		aliens = ["Umgah", "Drej", "Eldila", "Zoni", "Blastaar", "Shoggoths", "Govorom", "Medusan", "Tholian", "Petrosapien", "Oswaft", "Acanti"]
		return random.choice(aliens)
	
class Setup(object):
	
	def begin(self):
		print "-" * 20
		print " ",
		print "*" * 16
		print " NEBULAIC TOASTER"
		print " ",
		print "*" * 16
		print "-" * 20
		print """
	   
   	                    0)__/... \_
   	                   00)__)  .___)
   	  ___              _0__)\_/ OOO/`':.
  	  0)_^'-._    __..-'`:  \\ | / ::  \\ o`:
   	 0)_\ \~_..-': \\ \\   :  \\|/   ::  |   \\
   	     \ /      : | |  :    :  ::  /  _./>-
   	      (__ ))): /_/____.))_____//.-'`
    	      7 7~~'\"\"\"            7 7
    	      L_L                 / /
    	     0) ^'-.__            |_|
    	     0)__.-'             0) ^'-.__
    	                         0)__.-'"""
		print """
		  STARTING
		  """
		print "." * 50

	def start(self):
		name = raw_input("Captain's Name:")
		print "Welcome, %s, you are the ship's captian. \n You will make decisions and guide our ship through space and beyond." % name
		print "A few technicalities first captain. I will give you options to choose from regarding our path.\nAt this moment the ship's computer will only take numbers as answers."
		print "By the way, you can give me a name"
		computer_name = raw_input("What do you want to call me?")
		print "From now on I shall be called %s." % computer_name
		print "Your ship is fuelled by uranium."
		print "One is used every jump."
		print "You currently have %s uranium." % inventory.uranium_store(0, 0)
		print "The currency this ship uses is scrap."
		print "You have %d scrap" % inventory.scrap_store(0, 0)
		print "We have one weapon on this ship: Missile Launcher"
		print "You have %d missiles in the missile_store." % inventory.missile_store(0, 0)
		print " We will now go off, into the abyss..."
		print "If you want to exit at any time just enter 3"
		self.jump(name, computer_name)
		return computer_name, name	
		
	def quit(self):
		print "Are you sure you want to quit?"
		print "1. Yes"
		print "2. No, restart"
		answer = raw_input(">")
		if answer == 1:
			exit(0)
		else:
			game()	
	def game(self):
		self.begin()	
		self.start()
	def jump(self, name, computer_name):

		print """ Do you want to:
		1. Jump to a nearby star
		2. Jump to a far off star
		3. Exit"""
		answer = raw_input(">")
		
		if answer == "1":
			inventory.uranium_store(0, 1)
			random_.starnear(name, computer_name)
		elif answer == "2":
			inventory.uranium_store(0, 1)
			random_.starfar(name, computer_name)
		elif answer == "3":
			self.quit()	
		else:
			print "I dont understand."
			jump(name, computer_name)
		
			
class Stars(object):
	
	def star1(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "We are in orbit around the star %s." % random_.star()
		action(name, computer_name)
	
	def star2(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "I couldn't get us close enough to orbit around %s." % random_.star()
		print "Would you like to jump again?"
		print "1. Yes"
		print "2. No"
		answer = raw_input(">")
		if answer == "1":
			jump() 
		elif answer == "2":
			action(name, computer_name)
		elif answer == "3":
			quit()	
		else:
			print "I couldn't catch that. Jumping anyway..."
			jump()	
	
	def star3(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "We are in orbit around the star %s." % random_.star()
		action(name, computer_name)
	
	def star4(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)	
		print "Our current coordinates are: %s." % random_.coordinates()
		print "There are no stars around here %s." % name
		action(name, computer_name)
	
	def star5(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "We are in orbit around the star %s." % random_.star()
		action(name, computer_name)

	def stara(self, name, computer_name):
		print "REBOOTING INTO SAFE MODE"
		print "-" * 20 
		action(name, computer_name)
		
	def starb(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "We are in orbit around the star %s." % random_.star()
		action(name, computer_name)

	def starc(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "We are in orbit around the star %s." % random_.star()
		action(name, computer_name)
		
	def stard(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "I cant give you any accurate coordinates right now, %s, we are in deep space." % name
		print "I managed to find our nearest star: %s." % random_.star()
		action(name, computer_name)			
			
class Actions(object):
	def action1(name, computer_name):
		print "We are recieving a transmission from a %s ship, %s." % (random.alien(), name)
		print "INCOMING TRANSMISSION: Surrender Your computer to us or we will blast you into oblivion."
		print "You have 4 options, %s, choose wisely." % name
		print "1. Surrender the ships computer"
		print "2. Fire the %d remaining missiles in your missile_store" % missile_store(0, 0)
		print "3. QUIT"
		print "4. Attempt to Jump"
		answer = raw_input(">")
		if answer == "1":
			print "You surrendered the ship's computer."
			print "You drift into space for eternity."
			raw_input(">")
			quit() 	
		elif answer == "2":
			print "How many missiles do you want to fire?"
			print "Please enter a number from 1 - %s" % missiles
			answer = int(raw_input(">"))
			if answer < 2:
				inventory.missile_store(0, answer)
				print "Your missiles did not perform enough damage."
				print "Your ship was destroyed."
				quit()
			elif 2 <= answer:
				missile_store(0, answer)
				number = random.uniform(1, 7)
				print "You destroyed the ship!"
				print "They left %d missiles behind!" % number
				missile_store(number, 0)
			else:	
				print "RESTARTING SEQUENCE"
				action1()
		elif answer == "3":
			print "Quitting..."
			quit()
		elif answer == "4":
			attempt = ["yes", "no"]
			choice = random.choice(attempt)
			if choice == "yes":
				print "Attempt Succesful. Jumping..."
				jump(name, computer_name)
			if choice == "no":		
				print "Jump insuccessful. Rockets locking on."
				print "SHIP DESTROYED"
				quit()
	def action2(name, computer_name):
		print "Captian."
	
	def action3(name, computer_name):
		print "WE HAVE BEEN HIT"
	def action4(name, computer_name):	
		print "You discovered a piece of uranium, do you want to add it to the inventory?"
		print "1. yes"
		print "2. no"
		answer = raw_input(">")
		if answer == "1":
			print "Collecting uranium..."
			uranium_store(1, 0)
			print "You now have %s uranium. Enough for %s more jumps." % (uranium_store(0,0), uranium_store(0,0))
		elif answer == "2":
			print "Uranium not collected."
			jump()
		elif answer == "3":
			quit()
		else:
			print " I didn't catch that, restarting sequence."
			action4(name, computer_name)			
				
inventory = Inventory()	
random_ = Random()
stars = Stars()
actions = Actions()
setup = Setup()
setup.begin()		
print "uranium = %s" % inventory.uranium_store(0, 0)		
print "uranium = %s" % inventory.uranium_store(9, 0)		
print "uranium = %s" % inventory.uranium_store(0, 5)
print "uranium = %s" % inventory.uranium_store(0, 0)
print "you have %s scrap" % inventory.scrap_store(0, 0)		
print "You have %s missiles" % inventory.missile_store(0, 0)
setup.game()
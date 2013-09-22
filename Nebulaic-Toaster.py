import random
from sys import exit
import time
				
	

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
			if self.uranium > 0:
				return "DANGER: %d URANIUM REMAINING" % self.uranium
			elif self.uranium == 0:
				print "You can jump no further."
				setup.quit()
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
			return "NO MISSILES!"			


class Random(object):
	def starnear(self, name, computer_name):
		stars = [Stars().star1, Stars().star2, Stars().star3, Stars().star4, Stars().star5, Shops().shop1]
		random.choice(stars)(name, computer_name)				
		
	def starfar(self, name, computer_name):
		stars = [Stars().stara, Stars().starb, Stars().starc, Stars().stard, Shops().shop1]
		random.choice(stars)(name, computer_name)	
		
	def coordinates(self):
		#FIX DEGREE SIGN PROBLEM
		degree_sign= u'\N{DEGREE SIGN}'
		ac = random.uniform(-60, 60)
		bc = random.uniform(-60, 60)
		cc = random.uniform(-60, 60)
		return u" %d degrees %d' %d\" " % (ac, bc, cc)	
		
	def star(self):
		star_list = ["ACAMAR", "ACHERNAR", "Achird", "ACRUX", "Acubens", "ADARA", "Adhafera", "Adhil", "AGENA", "Ain-al-Rami", "Ain", "Aladfar", "Alathfar", "Albaldah", "Albali", "ALBIREO", "Alchiba", "ALCOR", "ALCYONE", "ALDEBARAN", "ALDERAMIN", "Aldhibah", "Alfecca-Meridiana", "Alfirk", "ALGENIB", "ALGIEBA", "ALGOL", "Algorab", "ALHENA", "ALIOTH", "ALKAID", "Alkalurops", "Alkes", "Alkurhah", "ALMAAK", "ALNAIR", "ALNATH", "ALNILAM", "ALNITAK", "Alniyat", "Alniyat", "ALPHARD", "ALPHEKKA", "ALPHERATZ", "Alrai", "Alrisha", "Alsafi", "Alsciaukat", "ALSHAIN", "Alshat", "Alsuhail", "ALTAIR", "Altarf", "Alterf", "Aludra", "Alula-Australis", "Alula-Borealis", "Alya", "Alzirr", "Ancha", "Angetenar", "ANKAA", "Anser", "ANTARES", "ARCTURUS", "Arkab-Posterior", "Arkab-Prior", "ARNEB", "Arrakis", "Ascella", "Asellus Australis", "Asellus-Borealis", "Asellus-Primus", "Asellus-Secondus", "Asellus-Tertius", "Asterope", "Atik", "Atlas", "Auva", "Avior", "Azelfafage", "Azha", "Azmidiske", "Baham", "Baten Kaitos", "Becrux", "Beid", "BELLATRIX", "BETELGEUSE", "Botein", "Brachium", "CANOPUS", "CAPELLA", "Caph", "CASTOR", "Cebalrai", "Celaeno", "Chara", "Chort", "COR-CAROLI", "Cursa", "Dabih", "DENEB", "DENEBOLA", "Dheneb", "Diadem", "DIPHDA", "Double-Double-(7051)", "Dschubba", "Dsiban", "DUBHE", "Ed-Asich", "Electra", "ELNATH", "ENIF", "ETAMIN", "FOMALHAUT", "Fornacis", "Fum-al-Samakah", "Furud", "Gacrux", "Gianfar", "Gienah-Cygni", "Gienah-Ghurab", "Gomeisa", "Gorgonea-Quarta", "Gorgonea-Secunda", "Gorgonea-Tertia", "Graffias", "Grafias", "Grumium", "HADAR", "Haedi", "HAMAL", "Hassaleh", "Head-of-Hydrus", "Herschel's-Garnet Star", "Heze", "Hoedus-II", "Homam", "Hyadum-I", "Hyadum-II", "IZAR", "Jabbah", "Kaffaljidhma", "Kajam", "KAUS-AUSTRALIS", "Kaus-Borealis", "Kaus-Meridionalis", "Keid", "Kitalpha", "KOCAB", "Kornephoros", "Kraz", "Kuma", "Lesath", "Maasym", "Maia", "Marfak", "Marfak", "Marfic", "Marfik", "MARKAB", "Matar", "Mebsuta", "MEGREZ", "Meissa", "Mekbuda", "Menkalinan", "MENKAR", "Menkar", "Menkent", "Menkib", "MERAK", "Merga", "Merope", "Mesarthim", "Metallah", "Miaplacidus", "Minkar", "MINTAKA", "MIRA", "MIRACH", "Miram", "MIRPHAK", "MIZAR", "Mufrid", "Muliphen", "Murzim", "Muscida", "Muscida", "Muscida", "Nair-al-Saif", "Naos", "Nash", "Nashira", "Nekkar", "NIHAL", "Nodus-Secundus", "NUNKI", "Nusakan", "Peacock", "PHAD", "Phaet", "Pherkad Minor", "Pherkad", "Pleione", "Polaris-Australis", "POLARIS", "POLLUX", "Porrima", "Praecipua", "Prima Giedi", "PROCYON", "Propus", "Propus", "Propus", "Rana", "Ras-Elased-Australis", "Ras-Elased-Borealis", "RASALGETHI", "RASALHAGUE", "Rastaban", "REGULUS", "Rigel-Kentaurus", "RIGEL", "Rijl-al-Awwa", "Rotanev", "Ruchba", "Ruchbah", "Rukbat", "Sabik", "Sadalachbia", "SADALMELIK", "Sadalsuud", "Sadr", "SAIPH", "Salm", "Sargas", "Sarin", "Sceptrum", "SCHEAT", "Secunda-Giedi", "Segin", "Seginus", "Sham", "Sharatan", "SHAULA", "SHEDIR", "Sheliak", "SIRIUS", "Situla", "Skat", "SPICA", "Sterope-II", "Sualocin", "Subra", "Suhail-al-Muhlif", "Sulafat", "Syrma", "Tabit-(1543)", "Tabit-(1544)", "Tabit-(1552)", "Tabit-(1570)", "Talitha", "Tania-Australis", "Tania-Borealis", "TARAZED", "Taygeta", "Tegmen", "Tejat-Posterior", "Terebellum", "Terebellum", "Terebellum", "Terebellum", "Thabit", "Theemim", "THUBAN", "Torcularis-Septentrionalis", "Turais", "Tyl", "UNUKALHAI", "VEGA", "VINDEMIATRIX", "Wasat", "Wezen", "Wezn", "Yed-Posterior", "Yed-Prior", "Yildun", "Zaniah", "Zaurak", "Zavijah", "Zibal", "Zosma", "Zuben-Elakrab, Zuben-Elakribi, Zuben-Elgenubi, Zuben-Elschemali"]
		return random.choice(star_list)
	
	
	def action(self, name, computer_name):
		actions = [Actions().action1, Actions().action2, Actions().action3, Actions().action4]
		choice = random.choice(actions)
		actions.remove(choice)
		choice(name, computer_name)
	
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
		print "You have %d missiles in the missile store." % inventory.missile_store(0, 0)
		print " We will now go off, into the abyss..."
		print "If you want to exit at any time just enter 3"
		self.jump(name, computer_name)
		return computer_name, name	
		
	def quit(self):
		print "Are you sure you want to quit?"
		print "1. Yes"
		print "2. No, restart"
		answer = raw_input(">")
		if answer == "1":
			exit(0)
		elif answer == "2":
			Setup().game()
		else:
			print "QUITTING"
			exit(0)
				
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
			Setup().jump(name, computer_name)
		def jump_attempt(self, name, computer_name):
			print "Attempting jump..."
			randnum = random.choice("1", "2", "3")
			if randnum == "1":
				print "Powering Up"
				print ">", 
				time.sleep(0.3)
				print ">", 
				time.sleep(0.3)
				print ">", 
				time.sleep(0.3)
				print ">", 
				time.sleep(0.3)
				print ">", 
				time.sleep(0.3)
				print ">", 
				time.sleep(0.3)
				print ">", 
				time.sleep(0.3)
            
class Stars(object):
	
	def star1(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "We are in orbit around the star %s." % random_.star()
		random_.action(name, computer_name)
	
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
			Setup().jump(name, computer_name) 
		elif answer == "2":
			random_.action(name, computer_name)
		elif answer == "3":
			Setup().quit()	
		else:
			print "I couldn't catch that. Jumping anyway..."
			Setup().jump(name, computer_name)	
	
	def star3(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "We are in orbit around the star %s." % random_.star()
		random_.action(name, computer_name)
	
	def star4(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)	
		print "Our current coordinates are: %s." % random_.coordinates()
		print "There are no stars around here %s." % name
		random_.action(name, computer_name)
	
	def star5(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "We are in orbit around the star %s." % random_.star()
		random_.action(name, computer_name)

	def stara(self, name, computer_name):
		print "REBOOTING INTO SAFE MODE"
		print "-" * 20 
		random_.action(name, computer_name)
		
	def starb(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "We are in orbit around the star %s." % random_.star()
		random_.action(name, computer_name)

	def starc(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "Our current coordinates are: %s." % random_.coordinates()
		print "We are in orbit around the star %s." % random_.star()
		random_.action(name, computer_name)
		
	def stard(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "Hello %s, it's %s here." % (name, computer_name)
		print "I cant give you any accurate coordinates right now, %s, we are in deep space." % name
		print "I managed to find our nearest star: %s." % random_.star()
		random_.action(name, computer_name)			
	
class Shops(object):

	def shop1(self, name, computer_name):
		print "You have %s uranium left." % inventory.uranium_store(0, 0)
		print "INCOMING TRANSMISSION: DE-SCRAMBLING"
		print "Welcome, you have stumbled upon a pirate trading station."
		print "Feel free to browse our wares, just dont try anything funny."
		self.shop_setup(name, computer_name)
		
			
	def shop_setup(self, name, computer_name):
		print "-" * 20
		print "." * 20
		print "...STOCK LOADING...."
		print "." * 20
		print "-" * 20
		print "1. BUY"
		print "2. SELL"	
		print "3. QUIT"
		print "4. JUMP"
		answer = raw_input(">")	
		if answer == "1":
			self.buy(name, computer_name)
		elif answer == "2":
			self.sell(name, computer_name)
		elif answer == "3":
			Setup().quit()
		elif answer == "4":
			Setup().jump(name, computer_name)	
			
	def buy(self, name, computer_name):
		print "YOUR INVENTORY:"
		print "Scrap: %s" % inventory.scrap_store(0, 0)
		print "Uranium: %s"	% inventory.uranium_store(0, 0)
		print "Missiles: %s" % inventory.missile_store(0, 0)
		shop_uranium = random.randint(0, 15)
		price_uranium = random.randint(2, 5)
		shop_missiles = random.randint(0, 15)
		price_missiles = random.randint(3, 9) 
		print "What would you like to buy?"
		print "1. Uranium (stock: %s),  %s scrap" % (shop_uranium, price_uranium)
		print "2. Missiles (stock: %s), %s scrap" % (shop_missiles, price_missiles)
		answer = raw_input(">")
		if answer == "1":
			print "How many Uranium (stock: %s) ?" % shop_uranium
			ans = int(raw_input(">"))
			if ans > shop_uranium:
				print "You cannot buy that many, only %s available" % shop_uranium
			elif ans * price_uranium > inventory.scrap_store(0, 0):
				print "You don't have enough scrap for that."
				print "Returning to shop..."
				self.shop_setup() 
			else:		
				pay = price_uranium * ans
				shop_uranium -= ans
				inventory.scrap_store(0, pay)
				print "Transaction completed."
				print "You now have %s uranium, and %s scrap" % (inventory.uranium_store(ans, 0), inventory.scrap_store(0, 0))
				print "Do you want to go back to the shop or jump on?"
				print "1. Return to shop"
				print "2. Jump"
				answer = raw_input(">")
				if answer == "1":
					self.shop_setup(name, computer_name)
				elif answer == "2":
					setup.jump(name, computer_name)	
				elif answer == "3":
					setup.quit()
				else:
					print "I do not understand, jumping anyway."
					setup.jump(name, computer_name)		
					
		elif answer == "2":
			print "How many Missiles (stock: %s) ?" % shop_missiles
			ans = int(raw_input(">"))
			if ans > shop_missiles:
				print "You cannot buy that many, only %s available" % shop_missiles
				
			elif ans * price_missiles > inventory.scrap_store(0, 0):
				print "You don't have enough scrap for that."
				print "Returning to shop..."
				self.shop_setup(name, computer_name) 
			else:		
				pay = price_missiles * ans
				shop_missiles -= ans
				inventory.scrap_store(0, pay)
				print "Transaction completed."
				print "You now have %s missiles, and %s scrap" % (inventory.missile_store(ans, 0), inventory.missile_store(0, 0))
				print "Do you want to go back to the shop or jump on?"
				print "1. Return to shop"
				print "2. Jump"
				answer = raw_input(">")
				if answer == "1":
					self.shop_setup(name, computer_name)
				elif answer == "2":
					setup.jump(name, computer_name)	
				elif answer == "3":
					setup.quit()
				else:
					print "I do not understand, jumping anyway."
					setup.jump(name, computer_name)				
					
			
			
	def sell(self, name, computer_name):	
		print "YOUR INVENTORY:"
		print "Scrap: %s" % inventory.scrap_store(0, 0)
		print "Uranium: %s"	% inventory.uranium_store(0, 0)
		print "Missiles: %s" % inventory.missile_store(0, 0)	
		paid_uranium = random.randint(1, 5)
		paid_missiles = random.randint(1, 6)
		print "Prices Paid:"
		print "Uranium: %s scrap"
		print "Missiles: %s scrap"
		print "What would you like to sell?"
		print "1. Uranium"
		print "2. Missiles" 
		print "3. QUIT GAME"
		print "4. Nothing"
		answer = raw_input(">")
		if answer == "1":
			print "How many would you like to sell (%s in inventory)." % inventory.uranium_store(0, 0)
			ans = int(raw_input(">"))
			if ans > inventory.uranium_store(0, 0):
				print "Not enough uranium to sell"
				print "Returning to shop."
				self.shop_setup(name, computer_name)
			else:
				paid = paid_uranium * ans
				inventory.scrap_store(paid, 0)
				inventory.uranium_store(0, ans)
				print "TRANSACTION COMPLETE"
				print "Inventory:"
				print "Uranium: %s" % inventory.uranium_store(0, 0)
				print "Scrap: %s" % inventory.scrap_store(0, 0)
				print "Missiles: %s" % inventory.missile_store(0, 0)
				print "1. Return to shop."
				print "2. Jump"
				print "3. QUIT"
				answ = raw_input(">")
				if answ == "1":
					self.shop_setup(name, computer_name)
				elif answ == "2":
					setup.jump(name, computer_name)
				elif answ == "3":
					setup.quit()
				else:
					print "Does not compute, jumping anyway.."
					setup.jump(name, computer_name)
					
		elif answer == "2":
			print "How many would you like to sell (%s in inventory)." % inventory.missile_store(0, 0)
			ans = int(raw_input(">"))
			if ans > inventory.missile_store(0, 0):
				print "Not enough missiles to sell"
				print "Returning to shop."
				self.shop_setup(name, computer_name)
			else:
				paid = paid_missile * ans
				inventory.scrap_store(paid, 0)
				inventory.missile_store(0, ans)
				print "TRANSACTION COMPLETE"
				print "Inventory:"
				print "Uranium: %s" % inventory.uranium_store(0, 0)
				print "Scrap: %s" % inventory.scrap_store(0, 0)
				print "Missiles: %s" % inventory.missile_store(0, 0)
				print "1. Return to shop."
				print "2. Jump"
				print "3. QUIT"
				answ = raw_input(">")
				if answ == "1":
					self.shop_setup(name, computer_name)
				elif answ == "2":
					setup.jump(name, computer_name)
				elif answ == "3":
					setup.quit()
				else:
					print "Does not compute, jumping anyway.."
					setup.jump(name, computer_name)
									
								
					
				
						
class Actions(object):
	
	def action1(self, name, computer_name):
		print "We are recieving a transmission from a %s ship, %s." % (random_.alien(), name)
		print "INCOMING TRANSMISSION: Surrender Your computer to us or we will blast you into oblivion."
		print "You have 4 options, %s, choose wisely." % name
		print "1. Surrender the ships computer"
		print "2. Fire the %d remaining missiles in your missile store" % inventory.missile_store(0, 0)
		print "3. QUIT"
		print "4. Attempt to Jump"
		answer = raw_input(">")
		if answer == "1":
			print "You surrendered the ship's computer."
			print "You drift into space for eternity."
			raw_input(">")
			Setup().quit() 	
		elif answer == "2":
			print "How many missiles do you want to fire?"
			print "Please enter a number from 1 - %s" % inventory.missile_store(0, 0)
			answer = int(raw_input(">"))
			if answer < 2:
				inventory.missile_store(0, answer)
				print "Your missiles did not perform enough damage."
				print "Your ship was destroyed."
				Setup().quit()
			elif 2 <= answer:
				inventory.missile_store(0, answer)
				number = random.randint(1, 7)
				print "You destroyed the ship!"
				print "They left %d missiles behind!" % number
				inventory.missile_store(number, 0)
				print "There is nothing left here. Just empty space. Jumping..."
				Setup().jump(name, computer_name)
			else:	
				print "RESTARTING SEQUENCE"
				action1()
		elif answer == "3":
			print "Quitting..."
			Setup().quit()
		elif answer == "4":
			attempt = ["yes", "no"]
			choice = random.choice(attempt)
			if choice == "yes":
				print "Attempt Succesful. Jumping..."
				Setup().jump(name, computer_name)
			if choice == "no":		
				print "Jump insuccessful. Rockets locking on."
				print "SHIP DESTROYED"
				Setup().quit()
	def action2(self, name, computer_name):
		print "Captian, a ship has been on our radar for the last three jumps."
		print "I think we are being followed, would you like to take action?"
		print "1. Yes, infiltrate the ship and disable their engines."
		print "2. No, jump on and hope they lose track of us."
		answer = raw_input(">")
		if answer == "1":
			infiltrate.setup(name, computer_name)
			
		elif answer == "2":
			print "They just dissapeared, I guess you were right."
			setup.jump(name, computer_name)	
		elif answer == "3":
			setup.quit()
		else:
			print "I couldn't catch that."
			print "I think it would be best if you take a look at this."
			infiltrate.setup(name, computer_name)	
	
	def action3(self, name, computer_name):
		print "WE HAVE BEEN HIT"
		battle.attacked(name, computer_name)
	def action4(self, name, computer_name):	
		print "You discovered a piece of uranium, do you want to add it to the inventory?"
		print "1. yes"
		print "2. no"
		answer = raw_input(">")
		if answer == "1":
			print "Collecting uranium..."
			inventory.uranium_store(1, 0)
			print "You now have %s uranium. Enough for %s more jumps." % (inventory.uranium_store(0,0), inventory.uranium_store(0,0))
			print "There is nothing else here, Jumping..."
			Setup().jump(name, computer_name)
		elif answer == "2":
			print "Uranium not collected."
			Setup().jump(name, computer_name)
		elif answer == "3":
			Setup().quit()
		else:
			print "I didn't catch that, restarting sequence."
			action4(name, computer_name)			
				
	# this next class is the infiltration series of stuff
class Infiltrate(object):
		
	def setup(self, name, computer_name):
		print "%s, we have a teleporter on board. I have tried to acess their teleporter gate" % name
		print "without them noticing but there is a passcode."
		print "You will have to hack into their computer systems and open the firewall."
		self.hack(name, computer_name)
		
	def hack(self, name, computer_name):
		print "I have managed to get access to an encrypted version of the passcode."
		print "You will have to unscramble the encryption to acess the teleport."
		print "You have 7 guesses."
		elephant = ["e", "l", "e", "p", "h", "a", "n", "t"]
		pirate = ["p", "i", "r", "a", "t", "e"]
		space = ["s", "p", "a", "c", "e"]
		communist = ["c", "o", "m", "m", "u", "n", "i", "s", "t"]
		passwords = [elephant, pirate, space, communist]
		choose = random.choice(passwords)
		password = [ ";", "\\", "1", "9", "*", ">", "/", "#"]
		password.append(choose)
		random.shuffle(password)
		print ''.join([str(item) for item in password])
		real = ''.join(choose)
		guesses = 0
		answer = raw_input(">")
		while answer != real and guesses < 7:
			guesses += 1
			ggs = 7 - guesses
			print "Wrong guess, %d left" % ggs
			answer = raw_input(">")
		if answer == real:
			print "You guessed the password!"
			print "I am teleporting you to the ship now, %s" % name
			self.teleport(name, computer_name)
		elif answer != real:
			print "I am afraid you have guessed the password wrong, we cannot teleport across."
			print "We will just have to hope they don't follow us"
			print "or we could blow them to smithereens..."
			print "1. Jump"
			print "2. Fire Missiles at them"
			ans = raw_input(">")
			if ans == "1":
				Setup().jump(name, computer_name)
			elif ans == "2":
				print "Ok, %s, how many missiles do you want to fire" % name
				
				print "You have %s missiles in the inventory." % inventory.missile_store(0, 0)
				print "Enter a number"
				answer = int(raw_input(">"))
				if answer <= inventory.missile_store(0, 0):
					print "Firing %s missiles" % answer
					if answer >= 4:	
						print "The other ship is no longer a problem."
						randu = random.randint(2, 9)
						randm = random.randint(1, 10)
						print "Their wreckage contains %d uranium and %d missiles." % (randu, randm)
						print "COLlECTING"
						print "We now have %s Uranium and %s missiles" % (inventory.uranium_store(randu, 0), inventory.missile_store(randm, answer))
						print "Prepare to jump"
						Setup().jump(name, computer_name)
					else:
						print "It wasn't enough, their missiles are locking on."
						li = ["1", "2"]
						ra = random.choice(li)
						if ra == "1":
							print "System shutting down."
							print "You drift out of your cabin into the abysss, your head explodes."
						elif ra == "2":
							print "We are hurt but not dead, I can repair this while we jump"		
							Setup().jump(name, computer_name)
			elif ans == "3":
				setup.quit()
			else:
				print "Not valid input."
				print "Jumping..."
				Setup().jump(name, computer_name)					
	def teleport(self, name, computer_name):
		print "We are inside the ship, %s, there are two corridors here."% name			
		print "1. Left, a long corridor	, eerily silent."
		print "2. Right, a grumbling can be heard, there is a door quite close."
		answer = raw_input(">")
		routes = ["1", "2"]		
		real = random.choice(routes)
		if answer == real:
			if answer == "1":
				print "The corridoor lights up as you proceed down it."
				print "%s, this ship has a silent engine, it runs on uranium just like ours." % name
				self.engine_room(name, computer_name)
				
			elif answer == "2":
				print "You walk to the door, the commotion is coming from further down"
				print "the corridoor, the door has a label \"ENGINE ROOM\""
				self.engine_room(name, computer_name)
				
		elif answer != real:
			if answer == "1":
				print "Your footsteps are loud on the composite floor,"
				print "suddenly you hear more footsteps and run for a doorway."
				print "%s, those are the footsteps of the %s." % (name, random_.alien())
				print "I fear that this is our last goodbye..."
				print "FFZZZBBBBAANNGWW"
				print "A light blinds you and you lose all of your senses."
				setup.quit()
			elif answer == "2":
				print "You open the door, the commotion you thought was the engine"
				print "was actually a room full of %s, they draw their weapons" % random_.alien()
				print "before you can turn and run they fire."
				print "You see a blinding light and your life ends."
				setup.quit()		
			elif answer == "3":
				setup.quit()
			else:
				print "you see a blinding light, the % race got to you before you could get to them." % random_.alien() 		
				setup.quit()
		else:
			print "you see a blinding light, the % race got to you before you could get to them." % random_.alien() 		
			setup.quit()	
			
	def engine_room(self, name, computer_name):		
			print "Scanning room for lifeforms."
			print "The room is clear,%s, you can go in." % name
				
class Battle(object):
	def attacked(self, name, computer_name):
		print "There is a %s ship firing at us" % random_.alien()	
		print "What do you want to do?"
		print "1. fire at them"
		print "2. attempt to jump"
		print "3. Quit"
		answer = raw_input(">")
		if answer == "1":
			self.fire(name, computer_name)
		elif answer == "2":
			setup.jump_attempt(name, computer_name)
		elif answer == "3":
			setup.quit()
		else:
			print "I cannot compute that answer..."
			self.attacked(name, computer_name)
        	
	def fire(self, name, computer_name):
			print "How many missiles do you want to fire?"
			print "You have %s missiles." % inventory.missile_store(0, 0)
			answer = int(raw_input(">"))
			number = random.randint(2, 6)
			if answer >= number and answer <= inventory.missile_store(0, 0):
				inventory.missile_store(0, answer)
				print "The ship is no longer locked onto us. They have been destroyed."
				print "They left behind %s missiles, %s uranium and %s scrap" % (inventory.missile_store(random.randint(0, 5), 0), inventory.uranium_store(random.randint(0, 4), 0), inventory.scrap_store(random.randint(0, 15), 0))
				print "Jumping..."
				setup.jump(name, computer_name)
			elif answer > inventory.missile_store(0, 0):
				print "Not enough missiles in your inventory." 
				self.fire(name, computer_name)
			else:
				print "You didn't fire enough missiles."
				print "MISSILES LOCKING ON"
				print "You float into the endless vacuum of space......"
				setup.quit()
battle = Battle()
inventory = Inventory()	
random_ = Random()
stars = Stars()
actions = Actions()
setup = Setup()
infiltrate = Infiltrate()	
		

setup.game()
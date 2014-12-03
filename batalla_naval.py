#coding:utf-8
import os,time,random
from sys import platform
#tablero 1 jugador
tablero = []
#tableros modo 2 jugadores 
barcos_caidos = {}
tableroJugador1 = []
tableroJugador2 = []
tabTirosJ1 = []
tabTirosJ2 = []

#Para limpiar ventanas
def clean ():
	if platform == "linux" or platform == "linux2":    # linux
		limpiar = os.system("clear")
	elif platform == "win32":    # Windows...
		limpiar = os.system("cls")
	return limpiar
#Tablero para  modo de un jugador 
for x in range(0,10):
	tablero.append(["~"] * 10)
def print_tablero(tablero):
	for fila in tablero:
		print " ".join(fila)	
		
#Posiciones de los barcos en Modo para un jugador

def fila_aleatoria(tablero):
  return random.randint(0,len(tablero)-1)
def columna_aleatoria(tablero):
  return random.randint(0,len(tablero[0])-1)

barco_fila = fila_aleatoria(tablero)
barco_col = columna_aleatoria(tablero)

barcof = fila_aleatoria(tablero)
barcoc = columna_aleatoria(tablero)

bf = fila_aleatoria(tablero)
bc =columna_aleatoria(tablero)

bfila = fila_aleatoria(tablero)
bcolumna =   columna_aleatoria(tablero)

ba_fila = fila_aleatoria(tablero)
ba_columna = columna_aleatoria(tablero)



def perdiste ():
	print '''	
	________$$$$$$$$$$________ 
	_____d$$$$$$$$$$$$$b______ 
	_____$$$$$$$$$$$$$$$$_____ 
	____4$$$$$$$$$$$$$$$$F____ 
	____4$$$$$$$$$$$$$$$$F____ 
	____$$$$"_"$$$$"_"$$$$_____ 
	_____$$F___4$$F___4$$_____ 
	_____´$F___4$$F___4$"_____ 
	______$$___$$$$___$P______ 
	______4$$$$$"^$$$$$%_____ 
	_______$$$$F__4$$$$_______ 
	________"$$$ee$$$"________ 
	________._*$$$$F4_________ 
	_________$_____.$_________ 
	_________"$$$$$$"_________ 
	__________^$$$$___________ 
	_4$$c_______""_______.$$r_ 
	_^$$$b______________e$$$"_ 
	_d$$$$$e__________z$$$$$b_ 
	4$$$*$$$$$c____.$$$$$*$$$r 
	_""____^*$$$be$$$*"____^"_ 
	__________"$$$$"__________ 
	________.d$$P$$$b_________ 
	_______d$$P___^$$$b_______ 
	___.ed$$$"______"$$$be.___ 
	_$$$$$$P__________*$$$$$$_ 
	4$$$$$P____________$$$$$$" 
	_"*$$$"____________^$$P___ 
	____""______________^"____ '''


def ganaste (): 
		print '''
		___________oo$$$$$$$$$$$$$$$$$$$$$$$$o 
		_________oo$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o 
		_______o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o 
		_____o$$$$$$$$$____$$$$$$$$$$$$$____$$$$$$$$$o 
		____o$$$$$$$$$______$$$$$$$$$$$______$$$$$$$$$$o 
		___$$$$$$$$$$$______$$$$$$$$$$$______$$$$$$$$$$$$ 
		__$$$$$$$$$$$$$____$$$$$$$$$$$$$____$$$$$$$$$$$$$$ 
		_$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
		o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
		$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
		$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"_"$$$ 
		$$$$$__$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$___o$$$ 
		_$$$$___$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$_____$$$$ 
		__$$$$____"$$$$$$$$$$$$$$$$$$$$$$$$$$$$"______o$$$ 
		__"$$$o_____"""$$$$$$$$$$$$$$$$$$"$$"_________$$$ 
		____$$$o__________"$$""$$$$$$""""___________o$$$ 
		_____$$$$o_________________oo_____________o$$$" 
		______"$$$$o______o$$$$$$o"$$$$o________o$$$$ 
		________"$$$$$oo_____""$$$$o$$$$$o___o$$$$"" 
		___________""$$$$$oooo__"$$$o$$$$$$$$$""" 
		______________""$$$$$$$oo $$$$$$$$$$$ 
		______________________""""$$$v$$$$$$$______________ 
		______________________"""""$$$$$$$$$ _______________'''			


#Inicia Modo Jugador 1 
class Modo1 (object): 
	def __init__(self):
		pass 	
	def play (self):
		turnos = 0 
		Ganados = 0 
		barco_undidos = 0			
		for oportunidades in range (11):
			while (True):
				try: 
					adivina_fila = int(raw_input ("Adivina fila:"))
					adivina_columna = int(raw_input ("Adivina columna:"))
					break
				except (ValueError, NameError):
					print "Lo siento lo que estas ingresando no es valido "
			#clean()
			#Verificaciones de impactos
			if (adivina_fila == barco_fila and adivina_columna == barco_col):
				print "Hundiste uno de mis barcos "
				barco_undidos +=1
				turnos +=1
				print "barcos hundidos : " , barco_undidos
				print "Turnos: ",turnos
				tablero[adivina_fila][adivina_columna] = "*"
				time.sleep(3)
				clean()


			elif (adivina_fila == barcof and adivina_columna == barcoc):
				print " Hundiste uno de mis barcos "
				barco_undidos+=1
				turnos +=1
				print "Barcos hundidos : " , barco_undidos
				print "Turnos: ",turnos
				tablero[adivina_fila][adivina_columna] = "*"
				time.sleep(3)
				clean()

			elif (adivina_fila == bf and adivina_columna == bc):
				print "Hundiste uno de mis barcos "
				barco_undidos+=1
				turnos +=1
				print "Barcos hundidos : " , barco_undidos
				print "Turnos: ",turnos	
				tablero[adivina_fila][adivina_columna] = "*"	
				time.sleep(3)
				clean()	

			elif (adivina_fila == bfila and adivina_columna == bcolumna):
				print "Hundiste uno de mis barcos "
				barco_undidos+=1
				turnos +=1
				print "Barcos hundidos : " , barco_undidos
				print "Turnos: ",turnos	
				tablero[adivina_fila][adivina_columna] = "*"
				time.sleep(3)
				clean()	

			elif (adivina_fila == ba_fila and adivina_columna == ba_columna):
				print "Hundiste uno de mis barcos "
				barco_undidos+=1
				turnos +=1
				print "Barcos hundidos : " , barco_undidos
				print "Turnos: ",turnos	
				tablero[adivina_fila][adivina_columna] = "*"
				time.sleep(3)
				clean()	
				
				#Termina el juego si acierta a todos los barcos
				if  barco_undidos == 5:
					os.system('clear')
					print " Que Bien ya hundiste todos mis barcos "
					Ganados +=1
					print "Llevas los siguientes juegos ganados : ",Ganados
					ganaste()
					break
					print_tablero(tablero)

			else:		
				while(True):
					try:
						if(tablero[adivina_fila][adivina_columna] == "X" or tablero[adivina_fila][adivina_columna] == "*"):
							turnos +=1
							print "Turnos: ",turnos
							print "Ya dijiste esa."
							time.sleep(2)
							clean()
							break
						else:
							print "Upsss creo que tendra que mejorar tu punteria o practicar mas "
							turnos +=1
							print "Turnos: ",turnos
							tablero[adivina_fila][adivina_columna] = "X"
							time.sleep(2)
							clean()
							break
					except (IndexError):
						print "Upps estas tirando en un zona donde no hay barcos"
						time.sleep(2)
						clean()
						break		
			#Si termina el juego y no  a cierta a todos los barcos 
				if oportunidades == 10:	
					Perdidos = 0 
					clean()
					print " Que mal no has hecho que naufragen todos los barcos  "
					Perdidos+=1
					print "Ohhhh estas empezando una mala racha ya llevas los siguientes juegos perdidos ",Perdidos
					print " Mis barcos estaban en:\n","fila :" ,barco_fila,",",barcof,",",bf,"," ,bfila,"\ncolumna",barco_col,",",barcoc,",",bc,",",bcolumna
					perdiste()
					time.sleep(5)
					clean()
			print_tablero(tablero)	



#Empieza Modo Multiplayer
for x in range(0,10):
	tableroJugador1.append(["~"] * 10)
	tableroJugador2.append(["~"] * 10)
	tabTirosJ1.append(["~"] * 10)
	tabTirosJ2.append(["~"] * 10)


def print_tablero1(tableroJugador1):
	for fila in tableroJugador1:
		print " ".join(fila)
def print_tablero2(tableroJugador2):
	for fila in tableroJugador2:
		print " ".join(fila)
def print_tablero3(tabTirosJ2):
	for fila in tabTirosJ2:
		print " ".join(fila)
def print_tablero4(tabTirosJ1):
	for fila in tabTirosJ1:
		print " ".join(fila)				

class Modo2 (object):
	def __init__(self):
		pass

	def Multiplayer(self):	
		#Inicia colocacione de barcos
		print "Bienvenido a la Batalla Naval"
		print """\nTendra 4 barcos de diferentes dimensiones y podra colocarlos en la forma que tu quieras y estan distribuidos de la sguien manera: 
	\n1. BigBoss : Este barco es tu principal y ocupara 4 de tus casillas \n2. Fragatas :Estos barcos ocupan 3 de tus casillas \n3. Lanchas Misileras : Estos lanchas ocupan 2 de tus casillas \n4. Patrullleros : Estos son los mas pequeños pero no menos fuertes y ellos ocupan 1 casilla 
	"""	
		time.sleep(3)
		clean()
		#Ingresos BArcos Jugador1 
		print "Tu eres el jugador 1 "
		jugador1 = raw_input (" Por favor ingresar tu nombre : ")
		clean()
		while (True):
			try:
				respuesta = 0
				while (respuesta==0):				
					fila_B = int(input ("Por favor ingrese la fila en la que desea poner su BigBoss: \n>"))
					if (fila_B < 0 or fila_B >=10):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break
				
				while (respuesta==0):
					columna_B = int (input ("Por favor ingrese la columna en la que desea poner su BigBoss: \n>"))
					if (columna_B < 0 or columna_B >=10):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break					
				while(True):
					
					posicion = int (input ("Por favor indica como quieres tu barco \n1 Vertical  \n2.Horizontal \n>"))
					clean()
					if (posicion >= 1 ) and (posicion<= 2 ):
						n= 0
						while  n <= 3 :
							if posicion == 1 : 
								tableroJugador1 [fila_B + n] [columna_B] = "B"
								n+= 1
							elif posicion == 2 : 
								tableroJugador1 [fila_B ] [columna_B + n] = "B"
								n+=1 
								
						break		
					else:		
						print "Solo puedes ponerlo Vertical U  Horinzontalmente"
							
				break
			except (ValueError, NameError,SyntaxError):
					print "Lo siento lo que estas ingresando no es valido "	
		
		while(True):
			try:
				#Barco De 3 casillas			
				while (respuesta==0):				
					fila_F = int(input ("Por favor ingrese la fila en la que desea poner su Fragata: \n>"))
					if (fila_F < 0 or fila_F >=10) or fila_F == fila_B or fila_F == fila_l or fila_F == fila_p:
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break
				while (respuesta==0):
					columna_f = int (input ("Por favor ingrese la columna en la que desea poner su Fragata: \n>"))
					if (columna_f < 0 or columna_f>=10 or columna_f == columna_B or columna_f == columna_l or columna_f == columna_p):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break					
				while(True):
					
					posicion = int (input ("Por favor indica como quieres tu barco \n1 Vertical  \n2.Horizontal \n>"))
					clean()
					if (posicion>=1)and (posicion<=2):
						n= 0
						while  n <= 2 :
							if posicion == 1 : 
								tableroJugador1 [fila_F + n] [columna_f] = "F"
								n+= 1
							elif posicion == 2 : 
								tableroJugador1 [fila_F ] [columna_f + n] = "F"
								n+=1
						break		
					else:		
						print "Solo puedes ponerlo Vertical U  Horinzontalmente"		
						
				break
			except (ValueError, NameError,SyntaxError):
					print "Lo siento lo que estas ingresando no es valido "	
		while(True):
			try:			
			#barco de 2 casillas 
				while (respuesta==0):				
					fila_l = int(input ("Por favor ingrese la fila en la que desea poner su Lancha Misilera: \n>"))
					if (fila_l < 0 or fila_l >=10 or fila_l == fila_B or fila_l == fila_F or fila_l == fila_p):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break
				while (respuesta==0):
					columna_l = int (input ("Por favor ingrese la columna en la que desea poner su Lancha Misilera: \n>"))
					if (columna_l < 0 or columna_l >=10 or columna_l == columna_B or columna_l == columna_f or columna_l == columna_p  ):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break					
				while(True):
					
					posicion = int (input ("Por favor indica como quieres tu barco \n1 Vertical  \n2.Horizontal \n>"))
					clean()
					if (posicion>=1)and (posicion<=2):
						n= 0
						while  n <= 1:
							if posicion == 1 : 
								tableroJugador1 [fila_l + n] [columna_l] = "L"
								n+= 1
					
							elif posicion == 2 : 
								tableroJugador1 [fila_l ] [columna_l + n] = "L"
								n+=1
						break		
					else:	
						print "Solo puedes ponerlo Vertical U  Horinzontalmente"	
				break
			except (ValueError, NameError,SyntaxError):
					print "Lo siento lo que estas ingresando no es valido "		
				
		while(True):
			try:
				while (respuesta==0):				
					fila_p = int(input ("Por favor ingrese la fila en la que desea poner su Patrulllero: \n>"))
					if (fila_p < 0 or fila_p >=10 or fila_p == fila_B or fila_p == fila_f or fila_p == fila_l):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break
				while (respuesta==0):
					columna_p = int (input ("Por favor ingrese la columna en la que desea poner su Patrulllero: \n>"))
					if (columna_p < 0 or columna_p >=10 or columna_p == columna_B or columna_p == columna_f or columna_p == columna_l):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break					
				while(True):
					
					posicion = int (input ("Por favor indica como quieres tu barco \n1 Vertical  \n2.Horizontal \n>"))
					clean()
					if (posicion>= 1)and (posicion<=2):
						n= 0
						while  n <= 0 :
							if posicion == 1 : 
								tableroJugador1 [fila_p + n] [columna_p] = "P"
								n+= 1
					
							elif posicion == 2 : 
								tableroJugador1 [fila_p ] [columna_p + n] = "P"
								n+=1
							else : 
								print "Solo puedes ponerlo Vertical U  Horinzontalmente"
						break		
					else:		
						print "Solo puedes ponerlo Vertical U  Horinzontalmente"				
				break
			except (ValueError, NameError,SyntaxError):
					print "Lo siento lo que estas ingresando no es valido "	
		clean()
		print "Impriendo tablero..."
		time.sleep(2)
		clean()
		print jugador1+ "'s  Board"
		print_tablero1(tableroJugador1)
		
		#colocacion de los barcos del jugador 2
		time.sleep(3)
		clean()
		print "Tu eres el jugador 2 "
		jugador2 = raw_input (" Por favor ingresar tu nombre : ")
		clean()
		print "Te toca ingresar tu barcos ",jugador2
		while (True):
			try:
				respuesta = 0
				while (respuesta==0):				
					fila_B2 = int(input ("Por favor ingrese la fila en la que desea poner su BigBoss: \n>"))
					if (fila_B2 < 0 or fila_B2 >=10):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break
				
				while (respuesta==0):
					columna_B2 = int (input ("Por favor ingrese la columna en la que desea poner su BigBoss: \n>"))
					if (columna_B2 < 0 or columna_B2 >=10):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break					
				while(True):
	
					posicion = int (input ("Por favor indica como quieres tu barco \n1 Vertical  \n2.Horizontal \n>"))
					clean()
					if(posicion>=1)and (posicion<=2):
						n= 0
						while  n <= 3 :
							if posicion == 1 : 
								tableroJugador2 [fila_B2 + n] [columna_B2] = "B"
								n+= 1
							elif posicion == 2 : 
								tableroJugador2 [fila_B2 ] [columna_B2 + n] = "B"
								n+=1 
						break		
					else:	
						print "Solo puedes ponerlo Vertical U  Horinzontalmente"
							
				break
			except (ValueError, NameError,SyntaxError):
					print "Lo siento lo que estas ingresando no es valido "	
		
		while(True):
			try:
				#Barco De 3 casillas			
				while (respuesta==0):				
					fila_F2 = int(input ("Por favor ingrese la fila en la que desea poner su Fragata: \n>"))
					if (fila_F2 < 0 or fila_F2 >=10 or fila_F2 == fila_B2 or fila_F2 == fila_l2 or fila_F2 == fila_p2  ):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break
				while (respuesta==0):
					columna_f2 = int (input ("Por favor ingrese la columna en la que desea poner su Fragata: \n>"))
					if (columna_f2 < 0 or columna_f2>=10 or columna_f2 == columna_B2  or columna_f2 == columna_l2 or columna_f2 == columna_p2 ):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break					
				while(True):
					
					posicion = int (input ("Por favor indica como quieres tu barco \n1 Vertical  \n2.Horizontal \n>"))
					clean()
					if(posicion>=1)and (posicion<=2):
						n= 0
						while  n <= 2 :
							if posicion == 1 : 
								tableroJugador2 [fila_F2 + n] [columna_f2] = "F"
								n+= 1
							elif posicion == 2 : 
								tableroJugador2 [fila_F2 ] [columna_f2 + n] = "F"
								n+=1
						break		
					else:		
						print "Solo puedes ponerlo Vertical U  Horinzontalmente"		
						
				break
			except (ValueError, NameError,SyntaxError):
					print "Lo siento lo que estas ingresando no es valido "	
		while(True):
			try:			
			#barco de 2 casillas 
				while (respuesta==0):				
					fila_l2 = int(input ("Por favor ingrese la fila en la que desea poner su Lancha Misilera: \n>"))
					if (fila_l2 < 0 or fila_l2 >=10 or fila_l2 == fila_B2 or fila_l2 == fila_F2 or fila_l2 == fila_p2):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break
				while (respuesta==0):
					columna_l2 = int (input ("Por favor ingrese la columna en la que desea poner su Lancha Misilera: \n>"))
					if (columna_l2 < 0 or columna_l2 >=10 or columna_l2 == columna_B2 or columna_l2 == columna_f2 or columna_l2 == columna_p2):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break					
				while(True):
				
					posicion = int (input ("Por favor indica como quieres tu barco \n1 Vertical  \n2.Horizontal \n>"))
					clean()
					if(posicion>=1)and (posicion<=2):
						n= 0
						while  n <= 1:
							if posicion == 1 : 
								tableroJugador2 [fila_2 + n] [columna_2] = "L"
								n+= 1
					
							elif posicion == 2 : 
								tableroJugador2 [fila_l2] [columna_l2 + n] = "L"
								n+=1
						break		
					else:	
						print "Solo puedes ponerlo Vertical U  Horinzontalmente"	
				break
			except (ValueError, NameError,SyntaxError):
					print "Lo siento lo que estas ingresando no es valido "		
				
		while(True):
			try:
				while (respuesta==0):				
					fila_p2 = int(input ("Por favor ingrese la fila en la que desea poner su Patrulllero: \n>"))
					if (fila_p2 < 0 or fila_p2 >=10 or fila_p2 == fila_B2 or fila_p2 == fila_F2 or fila_p2 == fila_l2):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break
				while (respuesta==0):
					columna_p2 = int (input ("Por favor ingrese la columna en la que desea poner su Patrulllero: \n>"))
					if (columna_p2 < 0 or columna_p2 >=10 or columna_p2 == columna_B2 or columna_p2 == columna_f2 or columna_p2 == columna_l2):
						print "Opcion no valida elija nuevamente, recuerda que es del 0 al 10, o de no estar escogiendo donde ya ingresaste un barco"
						respuesta = 0
						time.sleep(2)
					else:
						break					
				while(True):
					
					posicion = int (input ("Por favor indica como quieres tu barco \n1 Vertical  \n2.Horizontal \n>"))
					clean()
					if(posicion>=1)and (posicion<=2):
						n= 0
						while  n <= 0 :
							if posicion == 1 : 
								tableroJugador2 [fila_p2 + n] [columna_p2] = "P"
								n+= 1
					
							elif posicion == 2 : 
								tableroJugador2 [fila_p2 ] [columna_p2 + n] = "P"
								n+=1
							else : 
								print "Solo puedes ponerlo Vertical U  Horinzontalmente"
						break		
					else:		
						print "Solo puedes ponerlo Vertical U  Horinzontalmente"				
				break
			except (ValueError, NameError,SyntaxError):
					print "Lo siento lo que estas ingresando no es valido "
		clean()
		print "Impriendo tablero..."
		time.sleep(2)
		clean()
		print jugador2+ "'s  Board"
		print_tablero2(tableroJugador2)
		time.sleep(3)
		clean()
		print "Que Empiece El Juego"
		print "Es tu turno ",jugador1
		
		# Empieza El Juego 
		barco_hundidoj1 = 0 
		barco_hundidoj2 = 0 
		turnos = 0 
		for oportunidades in range (6):
			while (True):
				try: 
					adivina_fila = int(raw_input ("Adivina fila:"))
					adivina_columna = int(raw_input ("Adivina columna:"))
					break
				except (ValueError, NameError):
					print "Lo siento lo que estas ingresando no es valido "
			#clean()
			#Verificaciones de impactos
			if (adivina_fila == fila_B2 and adivina_columna == columna_B2):
				print " Que Bien le diste al BigBoss "
				barco_hundidoj1 +=1
				oportunidades +=1
				print "barcos hundidos : " , barco_hundidoj1
				print "Turnos: ",turnos
				tabTirosJ2[adivina_fila][adivina_columna] = "*"
				time.sleep(3)
				clean()
		
			elif (adivina_fila == fila_F2 and adivina_columna == columna_f2):
				print " Que Bien A Mi Fragata"
				barco_hundidoj1+=1
				oportunidades +=1
				print "Barcos hundidos : " , barco_hundidoj1
				print "Turnos: ",turnos
				tabTirosJ2[adivina_fila][adivina_columna] = "*"
				time.sleep(3)
				clean()
			
			elif (adivina_fila == fila_l2 and adivina_columna == columna_l2):
				print "Le diste a  mi Lancha Misilera "
				barco_hundidoj1+=1
				oportunidades+=1
				print "Barcos hundidos : " , barco_hundidoj1
				print "Turnos: ",turnos	
				tabTirosJ2[adivina_fila][adivina_columna] = "*"	
				time.sleep(3)
				clean()	
		
			elif (adivina_fila == fila_p2 and adivina_columna == columna_p2):
				print "Hundiste mi Patrulllero"
				barco_hundidoj1+=1
				oportunidades +=1
				print "Barcos hundidos : " , barco_hundidoj1
				print "Turnos: ",turnos	
				tabTirosJ2[adivina_fila][adivina_columna] = "*"
				time.sleep(3)
				clean()

				if  barco_hundidoj1 == 4:
					os.system('clear')
					print " Que Bien ya hundiste todos mis barcos "
					Ganados +=1
					print "Llevas los siguientes juegos ganados : ",Ganados
					ganaste()
					break
					print_tablero3(tabTirosJ2)	

			else:		
				while(True):
					try:
						if(tabTirosJ2[adivina_fila][adivina_columna] == "X" or tabTirosJ2[adivina_fila][adivina_columna] == "*"):
							turnos +=1
							print "Turnos: ",turnos
							print "Ya dijiste esa."
							time.sleep(2)
							clean()
							break
						else:
							print "Upsss creo que tendra que mejorar tu punteria o practicar mas "
							turnos +=1
							print "Turnos: ",turnos
							tabTirosJ2[adivina_fila][adivina_columna] = "X"
							time.sleep(2)
							clean()
							break
					except (IndexError):
						print "Upps estas tirando en un zona donde no hay barcos"
						time.sleep(2)
						clean()
						break	
				if oportunidades == 5:	
					print "Se acabo tu turno "
					break			
			print_tablero1(tableroJugador1)
			print "*"*20
			print_tablero3(tabTirosJ2)				


		
		#Turno 2
		print "Estu turno jugador 2"
		for turno2 in range(6):	
			while (True):
				try: 
					adivina_fila = int(raw_input ("Adivina fila:"))
					adivina_columna = int(raw_input ("Adivina columna:"))
					break
				except (ValueError, NameError):
					print "Lo siento lo que estas ingresando no es valido "

			if (adivina_fila == fila_B and adivina_columna == columna_B):
				print " Que Bien le diste al BigBoss "
				barco_hundidoj2 +=1
				turno2 +=1
				print "barcos hundidos : " , barco_hundidoj2
				print "Turnos: ",turnos
				tabTirosJ1[adivina_fila][adivina_columna] = "*"
				time.sleep(3)
				clean()
			
			elif (adivina_fila == fila_F and adivina_columna == columna_f):
				print " Que Bien A Mi Fragata"
				barco_hundidoj2+=1
				turno2 +=1
				print "Barcos hundidos : " , barco_hundidoj2
				print "Turnos: ",turnos
				tabTirosJ1[adivina_fila][adivina_columna] = "*"
				time.sleep(3)
				clean()

			elif (adivina_fila == fila_l and adivina_columna == columna_l):
				print "Le diste a  mi Lancha Misilera "
				barco_hundidoj2+=1
				turno2 +=1
				print "Barcos hundidos : " , barco_hundidoj2
				print "Turnos: ",turnos	
				tabTirosJ1[adivina_fila][adivina_columna] = "*"	
				time.sleep(3)
				clean()		

			elif (adivina_fila == fila_p and adivina_columna == columna_p):
				print "Hundiste mi Patrulllero"
				barco_hundidoj2+=1
				turno2 +=1
				print "Barcos hundidos : " , barco_hundidoj2
				print "Turnos: ",turnos	
				tabTirosJ1[adivina_fila][adivina_columna] = "*"
				time.sleep(3)
				clean()	
				if  barco_hundidos == 4:
					os.system('clear')
					print " Que Bien ya hundiste todos mis barcos "
					Ganados +=1
					print "Llevas los siguientes juegos ganados : ",Ganados
					ganaste()
					break
					print_tablero4(tabTirosJ1)

			else:		
				while(True):
					try:
						if(tabTirosJ1[adivina_fila][adivina_columna] == "X" or tabTirosJ1[adivina_fila][adivina_columna] == "*"):
							turnos +=1
							print "Turnos: ",turnos
							print "Ya dijiste esa."
							time.sleep(2)
							clean()
							break
						else:
							print "Upsss creo que tendra que mejorar tu punteria o practicar mas "
							turnos +=1
							print "Turnos: ",turnos
							tabTirosJ1[adivina_fila][adivina_columna] = "X"
							time.sleep(2)
							clean()
							break
					except (IndexError):
						print "Upps estas tirando en un zona donde no hay barcos"
						time.sleep(2)
						clean()
						break	
				if turno2 == 5:	
					print "Se acabo tu turno "

				break			
			print_tablero2(tableroJugador2)
			print "*"*20
			print_tablero4(tabTirosJ1)	
		print "El juego termino aqui estan los resultados de la batalla "
		if 	barco_hundidoj1 > barco_hundidoj2:
			clean()
			print "Bien jugador 1,  has ganado"
			print "Que mal jugador 2, tus flotas han naugrado"
			ganaste() 
		elif barco_hundidoj1 < barco_hundidoj2:
			clean()
			print "Bien jugador 2  has ganado"
			print "Que mal jugador 1, tus flotas han naugrado"
			ganaste()			
		elif  barco_hundidoj1 == barco_hundidoj2 : 
		
			clean()
			print "Empate las 2 tripulaciones naufragaron "	
			perdiste()
			time.sleep(2)
	

#menu que manda a llamar a las funciones que estan dentro de un diccionario					
class menu():
	clean()
	menu = {}
	menu['1']="Single player"
	menu['2']="Multiplayer"
	menu['3']="Salir"
	while True:
		options=menu.keys()
		options.sort()
		for entry in options: 
			print entry, menu[entry]
		
		selection=raw_input("Selecciona una opción: ") 
		if selection =='1':
			mi_tablero= Modo1()
			mi_tablero.play()
			
		elif selection == '2':
			
			mi_tablero= Modo2()
			mi_tablero.Multiplayer()
		elif selection == '3':
			break 	
		else: 
			print "Debes seleccionar una de las opciones"
menu()					





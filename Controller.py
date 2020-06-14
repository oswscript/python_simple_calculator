# coding: utf8

import os
import platform

class Controller(object):
    
	def __init__(self):
		self.resultado = ''
		self.num1 = 0
		self.num2 = 0
		self.num2 = 0
		self.type_operation = 0
		self.runAgn = ''
  

	
	def process_main(self,init= True):
     
		print(""" 

		------------------------------------------------------
		|====================================================| 
		|========== Bienvenido al sistema Matemático ========|
		|====================================================|
		------------------------------------------------------

		Seleccione 1 : Para Sumar 
		Seleccione 2 : Para Restar 
		Seleccione 3 : Para Multiplicar 
		Seleccione 4 : Para Dividir
		Seleccione 5 : Para Salir
				
		""")
  
		#MSG INPUT
  
		if init:
			self.type_operation = int(raw_input("Seleccione una operación: ")) #Input Number operation
		else:
			self.type_operation = int(raw_input("***Error. Para dividir, el primer número debe ser mayor al segundo.***\nPor favor, seleccione una operación otra vez: ")) #Input Number operation

   
		#CHECK OPERATION TYPE
		if self.type_operation > 0 and self.type_operation <= 4:

				self.num1 = int(raw_input("Ingrese el valor 1: "))
				self.num2 = int(raw_input("Ingrese el valor 2: "))

				print "\n********** El resultado es: " + str(self.operate()) + " ********** \n"
	
				self.runAgain()

		elif self.type_operation == 5:

				self.runAgain()
								
		else:

			return self.process_main(False)
		
 
  	def operate(self):

		try:
			
			if self.type_string() == 'sumar':
       
				self.resultado = self.num1 + self.num2
			
			elif self.type_string()  == 'restar':
       
				self.resultado = self.num1 - self.num2
			
			elif self.type_string()  == 'multiplicar':
       
				self.resultado = self.num1 * self.num2
		
			elif self.type_string()  == 'dividir':
				
				if not self.check_value_numbers():
        
					return self.process_main(False)
 
				else:
        
					self.resultado = self.num1 / self.num2

			else:
				
				self.resultado = False
    
			return self.resultado

		except NameError:
     
			print "Error general"

	def check_value_numbers(self):
		
		if self.num1 < self.num2:
			return False
		else:
			return True

	def type_string(self):
		
		if self.type_operation == 1:
			return 'sumar'

		elif self.type_operation == 2:
			return 'restar'

		elif self.type_operation == 3:
			return 'multiplicar'

		elif self.type_operation == 4:
			return 'dividir'

	def runAgain(self): #Making Runable Problem1353
		self.runAgn = raw_input("Desea continuar usando el sistema? N/S: ")
		
		if self.runAgn == 's':
			if platform.system() == "Windows": #Checking User OS For Clearing The Screen
				print os.system('cls') 
			else:
				print os.system('clear')
			self.process_main()
			self.runAgain()
		else:
      
			quit("Adios") #Print GoodBye Message And Exit The Program
   
   
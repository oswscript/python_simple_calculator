# coding: utf8

import os
import platform

#Main Class
class Controller(object):
    
	def __init__(self):
		self.result = ''
		self.num1 = 0
		self.num2 = 0
		self.num2 = 0
		self.type_operation = 0
		self.runAgn = ''
  
  #data capture process
	def process_main(self,init= True):
     
		print(""" 

		------------------------------------------------------
		|====================================================| 
		|========= Welcome to the mathematical system =======|
		|====================================================|
		------------------------------------------------------

		Choose 1 : To Add 
		Choose 2 : To Subtract 
		Choose 3 : To Multiply 
		Choose 4 : To Divide
		Choose 5 : To Leave
				
		""")
		#Check if selected for the first time, or multiple times
		if init:
			self.type_operation = int(raw_input("Choose an operation: ")) 
		else:
			self.type_operation = int(raw_input("***Error. To divide, the first number must be greater than the second.***\nPlease choose an operation again: "))
   
		if self.type_operation > 0 and self.type_operation <= 4:#if the selection is between 1 and 4
				self.num1 = int(raw_input("Ingrese el valor 1: "))#Input first number
				self.num2 = int(raw_input("Ingrese el valor 2: "))#Input second number
				print "\n********** El resultado es: " + str(self.operate()) + " ********** \n"#show result of the operation
				self.runAgain()#ask if I want to use the system again
		elif self.type_operation == 5:#if the selection is 5
				self.runAgain()#ask if I want to use the system again		
		else:
			#If the selected process number is different from the existing ones, repeat the process automatically
			return self.process_main(False)
		 
  	#data capture process
  	def operate(self):

			try:
				
				#if it is add
				if self.type_string() == 'add':
				
					self.result = self.num1 + self.num2
				
				#if it is subtract
				elif self.type_string()  == 'subtract':
				
					self.result = self.num1 - self.num2
				
				#if it is multiply
				elif self.type_string()  == 'multiply':
				
					self.result = self.num1 * self.num2
			
				#if it is divide
				elif self.type_string()  == 'divide':
      
					#check if the first number is greater than the second
					if not self.check_value_numbers():
					
						return self.process_main(False)#if the first is less, repeat "choose process"
	
					else:
					
						self.result = self.num1 / self.num2#if everything is correct divide

				else:
					
					self.result = "General error"
			
				return self.result

			except NameError:
			
				print "General error"
    
	#function to check if the first number is greater than the second
	def check_value_numbers(self):
		
		if self.num1 < self.num2:
			return False
		else:
			return True
 
	#function to check the String of the operation
	def type_string(self):
		
		if self.type_operation == 1:
			return 'add'

		elif self.type_operation == 2:
			return 'subtract'

		elif self.type_operation == 3:
			return 'multiply'

		elif self.type_operation == 4:
			return 'divide'

	#function to repeat the process or exit the system
	def runAgain(self): #
		self.runAgn = raw_input("You want to continue using the system? N/Y: ")
		
		if self.runAgn == 's':
			if platform.system() == "Windows": #Checking User OS For Clearing The Screen
				print os.system('cls') 
			else:
				print os.system('clear')
			self.process_main()
			self.runAgain()
		else:
      
			quit(""" 

			-----------------------
			|===================| 
			|======= Bye =======|
			|===================|
			-----------------------
				
		""") #Print BYE Message And Exit The Program
   
   
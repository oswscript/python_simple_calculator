#call external file
execfile('Controller.py')

#daughter class
class FirstController(Controller):
	
	def __init__(self):
		
		#Option 1: start the init class of the parent method
		#super(FirstController,self).__init__()
    
		#Option 2: start the init class of the parent method
  		Controller.__init__(self)


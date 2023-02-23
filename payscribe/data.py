from payscribe import Payscribe

class Data(Payscribe):
	
	def dataLookup(self, network):
		'''
			Lookup data plans
			:params network : The network you want to check data plans for
			:type network : string
			:return : Data plans for each or all network
			:rtype : string
		'''
		#pre = sender(path, network)
		return self.sender('data/lookup', {'network': network})
		
	def vendData(self, plan, recipient, network):
		'''
			Vend data for a given plan, recipient and network
			:params plan: Data plan of your choice
			:type plans: string
			:params recipient: Recipient's mobile number
			:type recipient: string
			:params network: Network provider of your choice
			:type network: string
			:return: 
		'''
		return self.sender('data/vend', {'plan': plan, 'recipient':recipient, 'network':network})

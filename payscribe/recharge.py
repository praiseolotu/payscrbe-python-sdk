
from Payscribe import Payscribe

class Recharge(Payscribe):
	
	def recharge(self, qty, amount, display_name):
		'''
			Print Recharge Card pins
			:params qty: Quantity of Recharge Card
			:type qty: int
			:params amount: Amount of Recharge Card
			:type amount: int
			:params display_name: Name of network provider
			:return: 
		'''
		return self.sender('rechargecard', {'qty': qty, 'amount':amount, 'display_name':display_name})
		
	def getCardPins(self, trans_id):
		'''
			Fetch Generated Recharge Card Pin
			:params trans_id: Transaction id used to fetch generated recharge pins
			:type trans_id: string
			:rtype: 
		'''
		return self.get_sender('cards', {'trans_id':trans_id})
		

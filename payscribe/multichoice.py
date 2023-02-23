
from payscribe import Payscribe

class Multichoice(Payscribe):
	def cardValidate(self, cardType, account):
		'''
			Validate Multichoice smart card number to get bouquet and customer details before vending
			:params cardType : 
			:params account : Validate card number
			:type  cardType : string
			:type account : string
		'''
		return self.sender('multichoice/validate', {'type': cardType, 'account':account})
		
	def vendMultiChoice(self, plan, code, phoneNum, token, trans_id):
		'''
			Make payment for GOTV - DSTV
			:type plan: string
			:type code: string
			:type phoneNum: string
			:type token: string
			:type trans_id: string
			
		'''
		return self.sender('multichoice/vend', {'plan': plan, 'productCode':code, 'phone':phoneNum, 'productToken':token, 'trans_id':trans_id})
		

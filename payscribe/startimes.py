
from payscribe import Payscribe

class Startimes(Payscribe):
	def validateStartimes(self, account, amount):
		
		return self.sender('startimes/validate', {'account': account, 'amount':amount})
		
	def vendStartimes(self, numStartimes, amount, product_code, productCode, phone,customer_name,trans_id):
		return self.sender('startimes/vend', {'smart_card_no': numStartimes, 'amount':amount, 'product_code':product_code, 'productCode':productCode, 'phone_number':phone, 'customer_name':customer_name, 'transaction_id':trans_id})
		

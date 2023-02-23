
from payscribe import Payscribe

class AirtimeToWallet(Payscribe):
	
	def airtimeToWallet(self):
		return self.sender('airtime_to_wallet', {})
		
	def atwProcess(self, network, amount, phone, sender):
		return self.sender('airtime_to_wallet/vend', {'network': network, 'amount':amount,'phone_number':phone, 'from':sender})

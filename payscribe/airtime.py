
from payscribe import Payscribe

class Airtime(Payscribe):
	def vendAirtime(self, network, amount, recipient, ported):
		return self.sender('airtime', {'network': network, 'amount':amount, 'recipent':recipient, 'ported':ported})
		

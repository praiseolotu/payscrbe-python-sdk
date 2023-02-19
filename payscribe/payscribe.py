import requests
from requests.exceptions import HTTPError, Timeout

class Payscribe:
	'''
			Instantiate HTTP fetch operations on the API endpoints
			:params key : API test key
			:type key: string
		'''
	def __init__(self, key):
		self.__key = key
		
	def dataLookup(self, network):
		'''
			Lookup data plans
			:params network : The network you want to check data plans for
			:type network : string
			:return : Data plans for each or all network
			:rtype : string
		'''
		
		API_ENDPOINT = "https://www.payscribe.ng/api/lookup/data"
		headers = {
			'Authorization':'Bearer %s'%self.__key,
			'Cache-Control':'no-cache',
		}
		if network.lower() == 'all':
			data = {}
			# data = {'network':}
		if network.lower() == 'mtn' or network.lower() == 'airtel' or network.lower() == 'glo' or network.lower() == '9mobile': 
			data = {'network':network}
		try:
			response = requests.post(url=API_ENDPOINT, headers=headers, data=data)
			response.raise_for_status()
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			print(response.text)
		
		
	def vendData(self, plans, recipient, network):
		
		'''
			:params plan: Data plan of your choice
			:type plans: string
			:params recipient: Recipient's mobile number
			:type recipient: string
			:params network: Network provider of your choice
			:type network: string
			:return: 
		'''
		
		API_ENDPOINT = "https://www.payscribe.ng/api/v1/data/vend"
		
		headers = {
			'Authorization':'Bearer %s'%self.__key,
			'Cache-Control':'no-cache',
		}
		
		data = {
			'plan':plans,
			'recipient':recipient,
			'network': network
		}
		
		try:
			response = requests.post(url=API_ENDPOINT, headers=headers, data=data)
			response.raise_for_status()
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			print(response.text)
		
		
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
		
		API_ENDPOINT = "https://www.payscribe.ng/api/rechargecard"
		
		headers = {
			'Authorization':'Bearer %s'%self.__key,
			'Cache-Control':'no-cache',
		}
		
		data = {
			'qty':qty,
			'amount':amount,
			'display_name': display_name
		}
		
		try:
			response = requests.post(url=API_ENDPOINT, headers=headers, data=data)
			response.raise_for_status()
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			print(response.text)
		
		
	def getCardPins(self, trans_id):
	
		'''
			Fetch Generated Recharge Card Pin
			:params trans_id: Transaction id used to fetch generated recharge pins
			:type trans_id: string
			:rtype: 
		'''
		
		API_ENDPOINT = "https://www.payscribe.ng/api/rechargecardpins"
		
		headers = {
			'Authorization':'Bearer %s'%self.__key,
			'Cache-Control':'no-cache',
		}
		
		try:
			response = requests.get(url=API_ENDPOINT, headers=headers, params={'trans_id':trans_id}, timeout=(3, 5))
			response.raise_for_status()
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Timeout:
			print("The request timed out")
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			print(response.text)
			
	# subject to change		
	def cardValidate(self, cardType, account):
		
		'''
			Validate Multichoice smart card number to get bouquet and customer details before vending
			:params cardType : 
			:params account : Validate card number
			:type  cardType : string
			:type account : string
		'''
		
		API_ENDPOINT = "https://www.payscribe.ng/api/v1/multichoice/validate"
		
		headers = {
			'Authorization':'Bearer %s'%self.__key,
			'Cache-Control':'no-cache',
		}
		
		data = {
			'type': cardType, 
			'account': account
		}
		
		try:
			response = requests.post(url=API_ENDPOINT, headers=headers, data=data)
			response.raise_for_status()
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			print(response.text)
	#change
	def vendMultiChoice(self, plan, code, phoneNum, token, trans_id):
		
		'''
			Make payment for GOTV - DSTV
			:type plan: string
			:type code: string
			:type phoneNum: string
			:type token: string
			:type trans_id: string
			
		'''
		
		API_ENDPOINT = "https://www.payscribe.ng/api/v1/multichoice/vend"
		
		headers = {
			'Authorization':'Bearer %s'%self.__key,
			'Cache-Control':'no-cache',
		}
		
		data = {
			'plan': plan, 
			'productCode': code,
			'phone': phoneNum,
			'productToken': token,
			'trans_id': trans_id
		}
		
		try:
			response = requests.post(url=API_ENDPOINT, headers=headers, data=data)
			response.raise_for_status()
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			print(response.text)
	#change		
	def validateStartimes(self, account, amount):
		'''
			Validate startimes smart card number to get bouquet and customer details before vending
			:type plan: string
			:type code: string
		'''
		API_ENDPOINT = "https://www.payscribe.ng/api/v1/startimes/validate"
		
		headers = {
			'Authorization':'Bearer %s'%self.__key,
			'Cache-Control':'no-cache',
		}
		
		data = {
			'amount': amount, 
			'account': account
		}
		
		try:
			response = requests.post(url=API_ENDPOINT, headers=headers, data=data)
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			print(response.text)
	#change
	def vendStartimes(self, plan, cycle, productCode, phone, productToken, trans_id):
		
		API_ENDPOINT = "https://www.payscribe.ng/api/v1/startimes/vend"
		
		headers = {
			'Authorization':'Bearer %s'%self.__key,
			'Cache-Control':'no-cache',
		}
	
		
		try:
			response = requests.post(url=API_ENDPOINT, headers=headers, data=data)
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			print(response.text)
	
	def airtimeToWallet(self):
		API_ENDPOINT = "https://www.payscribe.ng/api/airtime_to_wallet/lookup"
		
		headers = {
			'Authorization':'Bearer %s'%self.__key,
			'Cache-Control':'no-cache',
		}
		
		try:
			response = requests.post(url=API_ENDPOINT, headers=headers)
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			print(response.text)
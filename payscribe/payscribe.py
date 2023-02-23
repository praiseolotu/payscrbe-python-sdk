import requests
from requests.exceptions import HTTPError, Timeout
class Payscribe:
	'''
			Instantiate HTTP fetch operations on the API endpoints
			:params key : API test key
			:type key: string
			:params type : Environment type
			:type type: string
		'''
	LIVE_URL ="https://www.payscribe.ng/api/v1/"
	SANDBOX_URL="https://www.payscribe.ng/sandbox/"
	def __init__(self, key, type):
		self._key = key
		self._type = type
		'''
			Serialize api endpoint
		'''
	def api(self, path):
		if self._key.startswith("ps_test") and self._type == 'sandbox': 
			return self.SANDBOX_URL + path
		else:
			return self.LIVE_URL + path
		'''
			Handle HTTP post request
		'''
	def sender(self, path, data):
		headers = {
			'Authorization':'Bearer %s'%self._key,
			'Cache-Control':'no-cache',
		}
		'''
		url = self.api(path)
		data = data
		return url, data, headers
		'''
		url = self.api(path)
		try:
			response = requests.post(url=url, headers=headers, data=data)
			print(response)
			response.raise_for_status()
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			return response.json()
		
		
	def get_sender(self, path, data):
		headers = {
			'Authorization':'Bearer %s'%self._key,
			'Cache-Control':'no-cache',
		}
		'''
		url = self.api(path)
		data = data
		return url, data, headers
		'''
		url = self.api(path)
		try:
			response = requests.get(url=url, headers=headers, data=data, timeout=(3, 5))
			response.raise_for_status()
		except HTTPError as http_err:
			print(f'HTTP error: {http_err}')
		except Timeout:
			print("The request timed out")
		except Exception as err:
			print(f'Other error occured: {err}')
		else:
			return response.json()
	
	

import pickle

class SavingsAccount(object):
	"""This class represents a savings account with the owner's name, PIN and balance."""
	
	RATE = 0.02
	
	def __init__(self, name, pin, balance = 0.0):
		self._name = name
		self._pin = pin
		self._balance = balance
		
	def __str__(self):
		result =  'Name:    ' + self._name + '\n'
		result += 'PIN:     ' + self._name + '\n'
		result += 'Balance: ' + str(self._balance)
		return result
		
	def getBalance(self):
		return self._balance
	
	def getName(self):
		return self._name
		
	def getPin(self):
		return self._pin
	
	def deposit(self, amount):
		"""Deposits the given amount and returns the new balance."""
		self._balance += amount
		return self._balance
		
	def withdraw(self, amount):
		"""Withdraws the given amount. Return 'None' if successful, or an error message if unsuccessful."""
		if amount < 0:
			return 'Amount must be >= 0'
		elif self._balance < amount:
			'INSUFFICIENT FUNDS, AMOUNT CANNOT BE WITHDRAWN FROM ACCOUNT'
		else:
			self._balance -= amount
			return None
			
	def computeInterest(self):
		"""Computes, deposits, and returns the interest."""
		interest = self._balance * SavingsAccount.RATE
		self.deposit(interest)
		return interest
		
		
class Bank(object):
	
	def __init__(self, fileName = None):
		"""Creates a new dictionary to hold the accounts. If a filename is provided, loads the accounts from a file of pickled accounts."""
		self._accounts = {}
		self._fileName = fileName
		if fileName != None:
			fileObj = open(fileName, 'rb')
			while True:
				try:
					account = pickle.load(fileObj)
					self.add(account)
				except EOFError:
					fileObj.close()
					break
				
	def __str__(self):
		"""Returns the string rep of the entire bank"""
		return '\n'.join(map(str, self._accounts.values()))
		
	def add(self, account):
		"""Inserts an account using its PIN as a key."""
		self._accounts[account.getPin()] = account
		
	def remove(self, pin):
		return self._accounts.pop(pin, None)
		
	def get(self, pin):
		return self._accounts.get(pin, None)
		
	def computeInterest(self):
		"""Computes interest for each account and returns the total"""
		total = 0.0
		for account in self._accounts.values():
			total += account.computeInterest()
		return total
		
	def save(self, fileName = None):
		"""Saves pickled accounts to a file. The parameter allows the user to change filenames."""
		if fileName != None:
			self._filename = fileName
		elif fileName == None:
			return 
		fileObj = open(self._fileName, 'wb')
		for account in self._accoutns.values():
			pickle.dumb(account, fileObj)
		fileObj.close()
class Account:
	def __init__(self, account_name: str, account_balance=0):
		self.account_name = account_name
		self.account_balance = account_balance

	def deposit(self, temp_amount):
		temp_amount = temp_amount
		if temp_amount > 0:
			self.account_balance = self.account_balance + temp_amount
			return True
		else:
			return False

	def withdraw(self, temp_amount):
		if temp_amount > 0:
			self.account_balance = self.account_balance - temp_amount
			if self.account_balance >= 0:
				return True
			else:
				self.account_balance = self.account_balance + temp_amount
				return False
		else:
			return False

	def get_balance(self):
		return self.account_balance

	def get_name(self):
		return self.account_name

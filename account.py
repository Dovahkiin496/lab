class Account:
	"""
	A class representing details for an account object.
	"""

	def __init__(self, account_name: str, account_balance=0) -> None:
		"""
		Constructor to create initial values for an account object.
		:param account_name: The account's name.
		:param account_balance: The account's initial balance.
		"""
		self.account_name = account_name
		self.account_balance = account_balance

	def deposit(self, temp_amount):
		"""
		Method to add a specified amount to the account_balance variable.
		:param temp_amount: A temporary variable that stores the amount to be added or subtracted from the account balance.
		:return: Returns true or false depending on if the transaction occurred properly. (balance does not drop below 0.)
		"""
		temp_amount = temp_amount
		if temp_amount > 0:
			self.account_balance = self.account_balance + temp_amount
			return True
		else:
			return False

	def withdraw(self, temp_amount):
		"""
		Method to subtract a specified amount from the account_balance variable
		:param temp_amount: A temporary variable that stores the amount to be added or subtracted from the account balance.
		:return: Returns true or false depending on if the transaction occurred properly. (balance does not drop below 0.)
		"""
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
		"""
		Method to retrieve the balance linked to the account object.
		:return: Returns the balance of the account.
		"""
		return self.account_balance

	def get_name(self):
		"""
		Method to retrieve the name linked to the account object.
		:return: Returns the name of the account.
		"""
		return self.account_name


# ---------------------------------------------------------------------
A1 = Account("John")  # John - 0
A2 = Account("Jane", 50)  # Jane - 50

A1.deposit(100)  # 100
A2.withdraw(50)  # 0
A1.get_name()  # John
A2.get_balance()  # 0

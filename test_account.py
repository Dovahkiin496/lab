from account import *


class Test:
	def setup(self):
		self.B1 = Account("John")

	def teardown(self):
		del self.B1

	def test_deposit(self):
		assert self.B1.deposit(30) is True
		assert self.B1.get_balance() == 30

		assert self.B1.deposit(-30) is False
		assert self.B1.get_balance() == 30

		assert self.B1.deposit(0) is False
		assert self.B1.get_balance() == 30

	def test_withdraw(self):
		assert self.B1.withdraw(30) is False
		assert self.B1.get_balance() == 0

		assert self.B1.withdraw(-30) is False
		assert self.B1.get_balance() == 0

		assert self.B1.withdraw(0) is False
		assert self.B1.get_balance() == 0

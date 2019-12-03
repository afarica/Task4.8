# Create function dollarize() that takes Float and returns dollarized format:
# dollarize(123456.78901) -> "$123,456.80"
# dollarize(-123456.7801) -> "-$123,456.78"
# dollarize(1000000) -> "$1,000,000"

# Convert this function into useful class MoneyFmt. MoneyFmt contains single data value(the
# amount) and 4 methods.
# "init" //constructor initializes the data value
# "update" //method replaces data value with new one
# "repr" //methods returns Float value
# "str" //method, that implements logic of dollarize() method

# //The output will look like this:

class MoneyFmt:
	def __init__(self,number=0,money=0):
		self.number=number
		self.money=money

	def update(self):
		self.number = input('Enter the number:')

	def repr(self):
		self.money= float(self.number)

	def str(self):
		print('$' + format(self.money, ',.2f'))

cash=MoneyFmt()
cash.update()
cash.repr()
cash.str()
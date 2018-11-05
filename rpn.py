import logging
import sys

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

def calculate(arg):
	stack = []
	tokens = arg.split()

	for token in tokens:
		try:
			if token == 'quit':
				exit(0)
			stack.append(int(token))
		except ValueError:
			val1 = stack.pop()
			val2 = stack.pop()
			if token == '+':
				result = val1 + val2
			elif token == '-':
				result = val2 - val1
			'''elif token == '^':
				result = val2 ** val1
			elif token == '/':
				result = val2 / val1
			elif token == '%':
				result = val2 % val1'''
			stack.append(result)
		logging.debug(stack)
	if len(stack) > 1:
		raise ValueError('Too many arguments on the stack')
	return stack[0]

def main():
	'''while True:
		try:
			result = calculate(input("rpm calc> "))
			print(result)
		except ValueError:
			pass'''
	result = calculate("5 5 +")
	print(result)

if __name__ == '__main__':
	main()

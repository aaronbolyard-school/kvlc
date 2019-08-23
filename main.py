import kvlc.model.calculator as calculator

def get_integer(prompt):
	while True:
		print(prompt + " ", end="")

		value = input()
		try:
			return int(value)
		except:
			print("Please enter an integer.")

OPERATION_ACTION_REPEAT    = 1
OPERATION_ACTION_MAIN_MENU = 2

def should_repeat():
	while True:
		print("1. Repeat")
		print("2. Main Menu")

		action = get_integer("Enter a number:")
		if action == OPERATION_ACTION_REPEAT:
			return True
		elif action == OPERATION_ACTION_MAIN_MENU:
			return False
		else:
			print("Please select a valid option.")

def perform_operation(operation, name):
	while True:
		print()
		print(name)

		lhs = get_integer("Enter a number:")
		rhs = get_integer("Enter a number:")

		result = operation(lhs, rhs)

		if result != False:
			print(lhs, "+", rhs, "=", int(result))
		else:
			print("Bad input. Did you divide by zero?")

		if not should_repeat():
			break

ACTIONS = {
	1: calculator.add,
	2: calculator.sub,
	3: calculator.div,
	4: calculator.mul,
	5: False
}

ACTION_NAMES = {
	1: "Add",
	2: "Subtract",
	3: "Divide",
	4: "Multiply"
}

def main_menu():
	action = None
	while action != False:
		print('Welcome to the calculator program.')
		print('1. Add')
		print('2. Subtract')
		print('3. Divide')
		print('4. Multiply')
		print('5. Exit')
		index = get_integer("Enter a number:")
		action = ACTIONS.get(index, None)

		if action == None:
			print("Please select a valid option.")
		elif action != False:
			perform_operation(action, ACTION_NAMES[index])

	print("Goodbye.")

if __name__ == "__main__":
	main_menu()

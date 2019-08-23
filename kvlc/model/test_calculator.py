import calculator

def test_addition_positive_numbers():
	assert calculator.add(1, 1) == 2

def test_addition_negative_number():
	assert calculator.add(1, -1) == 0
	assert calculator.add(-1, 1) == 0
	assert calculator.add(-1, -1) == -2

def test_subtraction_positive_numbers():
	assert calculator.sub(1, 1) == 0

def test_subtraction_negative_number():
	assert calculator.sub(1, -1) == 2
	assert calculator.sub(-1, 1) == -2
	assert calculator.sub(-1, -1) == 0

def test_multiplication_positive_numbers():
	assert calculator.mul(2, 2) == 4

def test_multiplication_negative_number():
	assert calculator.mul(2, -2) == -4
	assert calculator.mul(-2, 2) == -4
	assert calculator.mul(-2, -2) == 4

def test_divide_positive_numbers():
	assert calculator.div(4, 2) == 2

def test_divide_negative_number():
	assert calculator.div(4, -2) == -2
	assert calculator.div(-4, 2) == -2
	assert calculator.div(-4, -2) == 2

def test_divide_zero():
	assert calculator.div(1, 0) == False

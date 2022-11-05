def calculator(s):
	s = s.replace(' ', '')
	stack = []

	for char in reversed(s):
		stack.append(char)

	while len(stack) > 1:
		first = stack.pop()
		if first == '(':
			result = getParenthesis(stack)
			stack.append(result)
		else:
			stack.append(first)
			num1 = getNum(stack)
			operation = getOperation(stack)
			next = stack.pop()
			num2 = ''
			if next == '(':
				num2 = getParenthesis(stack)
				stack.append(calculate(float(num1), operation, float(num2)))
			else:
				stack.append(next)
				num2 = getNum(stack)
				stack.append(calculate(float(num1), operation, float(num2)))
	return float(stack.pop())

def getOperation(stack):
	operation = stack.pop()
	next = stack.pop()
	if(operation == next):
		return operation + next
	else:
		stack.append(next)
		return operation

def getParenthesis(stack):
	num1 = getNum(stack)
	operation = getOperation(stack)
	num2 = getNum(stack)
	stack.pop()
	return calculate(float(num1), operation, float(num2))

def getNum(stack):
	num = ''
	current = stack.pop()
	while (current.replace('.','',1).isdigit() or current == '.'):
		num += current
		if len(stack) >= 1:
			current = stack.pop()
		else:
			return num
	stack.append(current)
	return num

def calculate(num1, operation, num2):
	match operation:
		case '+':
	 		return str(num1+num2)
		case '-':
			return str(num1-num2)
		case '*':
			return str(num1*num2)
		case '/':
			return str(num1/num2)
		case '**':
			return str(num1**num2)
		case '//':
			return str(num1//num2)


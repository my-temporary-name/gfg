# Infix to Prefix using stack

# 1. Create an empty stack st.
# 2. Reverse the input string exp.
# 3. Replace ( with ) and vice-versa.
# 4. Do infix to postfix conversion.
# 5. Reverse the postfix expression.


# -------------------- OR --------------------

# 1. create an empty stack st.
# 2. Create an empty string prefix.
# 3. Do the following for every character C from right to left:
# 4. If C is:
#     1. An operand: add it to prefix.
#     2. A closing parenthesis: push it to stack. " ) "
#    3. An opening parenthesis: pop from stack and add it to prefix until a closing parenthesis is encountered.
#    4. An operator: if st is empty push C to st. else compare with st top.
#        i) Higher Precedence ( than st top): push C to st.
#       ii) Lower Precedence: pop from st and add it to prefix until a higher precedence operator is found( or st become empty) and then push C to st.
#      iii) Equal precedence: use associativity rule.
# 5. Pop everything from stack and add to prefix.
# 6. Reverse the prefix.

# Python3 program to convert infix to prefix.

def isOperator(c):
	return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))

def getPriority(C):
	if (C == '-' or C == '+'):
		return 1
	elif (C == '*' or C == '/'):
		return 2
	elif (C == '^'):
		return 3
	return 0

def infixToPrefix(infix):
	operators = []

	operands = []

	for i in range(len(infix)):
		if (infix[i] == '('):
			operators.append(infix[i])

		elif (infix[i] == ')'):
			while (len(operators)!=0 and operators[-1] != '('):
				op1 = operands[-1]
				operands.pop()

				op2 = operands[-1]
				operands.pop()

				op = operators[-1]
				operators.pop()

				tmp = op + op2 + op1
				operands.append(tmp)

			operators.pop()

		elif (not isOperator(infix[i])):
			operands.append(infix[i] + "")

		else:
			while (len(operators)!=0 and getPriority(infix[i]) <= getPriority(operators[-1])):
				op1 = operands[-1]
				operands.pop()

				op2 = operands[-1]
				operands.pop()

				op = operators[-1]
				operators.pop()

				tmp = op + op2 + op1
				operands.append(tmp)
			operators.append(infix[i])

	while (len(operators)!=0):
		op1 = operands[-1]
		operands.pop()

		op2 = operands[-1]
		operands.pop()

		op = operators[-1]
		operators.pop()

		tmp = op + op2 + op1
		operands.append(tmp)

	return operands[-1]

s = "(A-B/C)*(A/K-L)"
print( infixToPrefix(s))


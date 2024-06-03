# Evaluate prefix expression
# Example: + * 2 10 3 = 23

def is_operand(c):
    return c.isdigit()

def evaluate(expr):
    stack = []
    for c in expr[::-1]:
        if is_operand(c):
            stack.append(int(c))
        else:
            o1 = stack.pop()
            o2 = stack.pop()

            if c == "+":
                stack.append(o1 + o2)
            elif c =="-":
                stack.append(o1 - o2)
            elif c == "*":
                stack.append(o1 * o2)
            elif c == "/":
                stack.append(o1 / o2)
    return stack.pop()


# Driver code
if __name__ == "__main__":
	test_expression = "+*213"
	print(evaluate(test_expression))
# Infix to postfix conversion

# Example: a+b*(c^d-e)^(f+g*h)-i
# Output: abcd^e-fgh*+^*+i-

# 1. create an empty stack: st = []
# 2. Do the following for every character x from left to right:
# 3. if x is:
#     a. an operand: print(x)
#     b. '(' : st.append(x)
#     c. ')' : pop and print all the elements from the stack until '(' is found
#     d. an operator: if st is empty push x to st, else compare the with st top.
#       i. Higher precedence (than st top): push x to st
#       ii. Equal precedence: use associativity
#       iii. Lower precedence: pop and print all the elements from the stack until x has higher precedence than st top
# 4. pop and print all the elements from the stack until it is empty

class conversion:
    def __init__(self,capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    
    def isEmpty(self):
        return True if self.top == -1 else False
    
    def peek(self):
        return self.array[-1]
    
    def pop(self):
        if not self.isEmpty():
            self.top-=1
            return self.array.pop()
        else:
            return "$"
        
    def push(self, op):
        self.top += 1
        self.array.append(op)
    
    def isOperand(self, ch):
        return ch.isalpha()
    
    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a<=b else False
        except KeyError:
            return False
    
    def infixToPostfix(self,exp):

        for i in exp:
            if self.isOperand(i):
                self.output.append(i)
            
            elif i == "(":
                self.push(i)
            
            elif i ==")":
                while ((not self.isEmpty()) and self.peek() != "(" ):
                    a= self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek()!="("):
                    return -1
                else:
                    self.pop()
            else:
                while(not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
        while not self.isEmpty():
            self.output.append(self.pop())
        
        print("".join(self.output))

# Driver's code
if __name__ == '__main__':
	exp = "a+b*(c^d-e)^(f+g*h)-i"
	obj = conversion(len(exp))

	# Function call
	obj.infixToPostfix(exp)
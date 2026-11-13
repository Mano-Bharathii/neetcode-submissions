class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == '-':
                n = stack.pop()
                stack.append(stack.pop() - n)    
            elif i == '*':
                stack.append(stack.pop() * stack.pop())    
            elif i == '/':
                n = stack.pop()
                stack.append(int(stack.pop() / n))    
            else:
                stack.append(int(i))
        return stack.pop()
                

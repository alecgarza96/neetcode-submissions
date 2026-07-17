class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        stack = []

        for char in s:
            if char in "({[":
                stack.append(char)
            elif len(stack) > 0 and self.checkChars(char, stack[-1]):
                stack.pop()
            else:
                return False
        
        print(stack)

        return len(stack) == 0
    
    def checkChars(self, currentChar, openChar):
        return currentChar == "]" and openChar == "[" or \
             currentChar == "}" and openChar == "{" or \
             currentChar == ")" and openChar == "("
        
# python3

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    # Define object by Bracket Class
    b_01 = Bracket()
    
    stack = []
    for key, char in enumerate(text):
        if char == '(' or char == '[' or char == '{':
            # Process opening bracket, write your code here
            
            stack.append(b_01(char, key)) # stack.push(char, key)
            pass # do nothing

        if char == ')' or char == ']' or char == '}':
            # Process closing bracket, write your code here
            if not stack: # if stack.Empty()
                return key
            top = stack.pop()
            if not top.match(char):
                return key
            pass
    if stack:
        top = stack.pop()
        return top.key
    
    # Printing answer, write your code here
    return "Success"

def checker(text):
    stack = []
    for key, char in enumerate(text, start=1):

        if char in ("[", "(", "{"):
            stack.append(Bracket(char, index))

        elif next in ("]", ")", "}"):
            if not stack:
                return index

            top = stack.pop()
            if not top.match(char):
                return index
    if stack:
        top = stack.pop()
        return top.key

    return "Success"
    

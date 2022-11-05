# Write here the code challenge solution
class Node:

    """
    Function to initialise the node Class
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """
    a class that implements the Stack Data structure
    """

    def __init__(self):
        self.top = None

    def push(self, value):
        """
         to add an item to the top of stack
        """
        node = Node(value)
        if self.top:
            node.next = self.top

        self.top = node

    def pop(self):
        """
         to remove an item from the top
        """

        if self.is_empty():
            raise Exception("This stack is empty")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value


    def peek(self):

        """
         to know the top value
        """
        if self.is_empty():
            raise Exception("This stack is empty")
        return self.top.value

    def is_empty(self):
        """
        To check if the stack is empty or not
        """
        return self.top == None
    def __str__(self):
        """
        method to print and display the   values added
        """
        output = "top -> "
        if self.top is None:
            output += None
        else:
            current = self.top
            while(current):

                output += ("["+str(current.value)+"]"+" -> ")
                current = current.next
            output += "None"
            return output

def validate_brackets(brackets):
    """
    Function to check validate brackets to be balanced in closed in right order
    """
    stack = Stack()
    i=0
    while  i < len (brackets):
        if brackets[i] in ["(", "{", "["]:
            stack.push(brackets[i])

        elif brackets[i] in [")", "}", "]"]:
            if stack.is_empty():
                return False
            item = stack.pop()
            if item == '(':
                if brackets[i] != ")":
                    return False
            if item == '{':
                if brackets[i] != "}":
                    return False
            if item == '[':
                if brackets[i] != "]":
                    return False
        i+=1

    return True

print (validate_brackets("(g)"))


print (validate_brackets("{}{Code}[Fellows](())"))

print (validate_brackets("{(})"))
print (validate_brackets("({)"))
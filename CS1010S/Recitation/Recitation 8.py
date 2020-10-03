##d = {}
##string = "sassasasasasaassaassasasasasaklsaklklaslksalksalskaslaksalkasklkal"
##for char in string:
##    if char not in d:
##        d[char] = 1
##    else:
##        d[char] += 1

# To calculate number of letters in a string

#To check a memeber in dictionary, time complexity is O(1)
#Check for existence, O(1)
#Getting value from key, O(1)
#You can modify the dictionary but you cannot modify the size of the dictionary.

# Question 2
def make_stack():
    stack = []
    def inner(message):
        if message == "is_empty":
            return not stack
        elif message == "clear":
            stack.clear()
        elif message == "peek":
            if stack:
                return stack[0]
            else:
                return None
        elif message == "push":
            def helper(item):
                stack.insert(0, item)
            return helper
        elif message == "pop":
            if stack:
                return stack.pop(0)
            else:
                return None
        else:
            #throw in error message
            raise Exception(message + "is unknown")
    return inner

s = make_stack()
print(s("is_empty")) # True
s("push")(1)
s("push")(2)
print(s("peek")) # 2
print(str (s("pop"))) # 2
print(str (s("pop"))) # 1
print(str (s("pop"))) # None

# Question 3
def push_all(stack, seq):
    for ele in seq:
        stack("push")(ele)
    return stack

# Question 4
def pop_all(stack):
    result = []
    while not stack("is_empty"):
        result.append(stack("pop"))
    return result

#Question 5
def make_calculator ():#an RPN calculator
    stack = make_stack ()
    ops = {'+': lambda x, y: x + y,
           '-': lambda x, y: x - y,
           '*': lambda x, y: x * y,
           '/': lambda x, y: x / y}
    def oplookup (msg, *arg): #arg is a tuple
        if msg == "ANSWER":
            if stack("is_empty"):
                return "empty_stack"
            else:
                return stack("peek")
        elif msg == "NUMBER_INPUT":
            num = arg[0]
            stack("push")(num)
            return "pushed"
        elif msg == "OPERATION_INPUT":
            op_string = arg[0]
            op = ops[op_string]
            num2 = stack("pop")
            num1 = stack("pop")
            res = op(num1, num2)
            stack("push")(res)
            return "pushed"
        elif msg == "CLEAR":
            stack("clear")
            return "cleared"
        else :
            raise Exception ("calculator does not " + msg )
    return oplookup

c = make_calculator ()
print(c('ANSWER')) # empty_stack
print(c('NUMBER_INPUT',4)) # pushed
print(c('ANSWER')) # 4
print(c('NUMBER_INPUT',5)) # pushed
print(c('ANSWER')) # 5
print(c('OPERATION_INPUT','+')) # pushed
print(c('ANSWER')) # 9
print(c('NUMBER_INPUT',7)) # pushed
print(c('OPERATION_INPUT','-')) # pushed
print(c('ANSWER')) # 2
print(c('CLEAR')) # cleared
print(c('ANSWER')) # empty_stack

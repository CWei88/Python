    # Recitation 5

## Question 2
def contains(x,tpl):
    for i in tpl:
        if x is i:
            return True
    return False

def deep_contains(x,tpl):
    for i in tpl:
        if x is i:
            return True
        elif type(i) == tuple:
            if deep_contains(x,i) == True: #finding nested tuple is always recursive
                return True
    return False

def deep_contains_recursive(x,tpl):
    if tup == ():
        return False
    elif tup[0] is x:
        return True
    elif type(tup[0]) == tuple:
        if deep_contains_recursive(x, tup[0]) == True:
            return True
    else:
        return deep_contains_recursive(x, tup[1:])

## Question 3
def accumulate(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0], accumulate(fn,initial,seq[1:]))

def fold_left(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(fold_left(fn, initial, seq[:-1]),seq[-1])

def fold_right(fn, initial, seq):
    if seq == ():
        return initial
    else:
        return fn(seq[0],fold_left(fn, initial, seq[1:]))

def pair(a,b):
    return (a, b)

def divide(a, b):
    return a/b

# Question 4

def empty_queue():
    return ()

def enqueue(x, q):
    return q + (x,)

def dequeue(q):
    return q[1:]

def qhead(q):
    return q[0]

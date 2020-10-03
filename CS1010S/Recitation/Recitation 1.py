#Question 3

def biggie_size(x):
    return x + 4


def unbiggie_size(x):
    return x - 4


def is_biggie_size(x):
    return x>=5

def combo_price(x):
    patty=1.17
    if is_biggie_size(x):
        x = unbiggie_size(x)
        return x * patty + 0.5
    else:
        return x * patty

def empty_order():
    return 0

def add_to_order(x,y):
    return int(str(x)+str(y))























    
    
    

#Question 1a
def order_size(n):
    if n == 0:
        return 0
    else:
        return 1 + order_size(n//10)

#time: O(n), where n is number of digits
#space: O(n)


#Question 1b
def order_size2(n):
    x = 0
    while n > 0:
        n = n//10
        x = x + 1
    return x
#time: O(n), where n is number of digits
#space: O(1)

#Question 1c
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


def order_cost(n):
    x = 0
    if n <= 0:
        return 0
    else:
        return combo_price(n%10) + order_cost(n//10)

#time: O(n)
#space: O(n)

#Question 1d
def order_cost2(n):
    total_cost = 0
    for i in range(order_size(order)):
        total_cost = total_cost + combo_price(order%10)
        order = order//10
    return total_cost

#time: O(n), where n is the number of digits
#space: O(1)

#Question 1e
def add_orders(n1,n2):
    

# Question 4
def fact(n):
    p,c = 1,1
    while c <= n:
        p = p * c
        c = c + 1
    return p
#time: O(n)
#space: O(1)

#Question 5
def find_e(n):
    if n == 0:
        return 1
    else:
        return 1/fact(n) + find_e(n-1)

def is_divisible(n,x):
    total = 0
    for i in range(n):
        total += 1
        if total == x:
            total = 0
    return total == 0



#Question 7
def find_e2(n):
    c,x = 1,1
    while c <= n:
        x = x + 1/fact(c)
        c = c + 1
    return x

#fib memoization
#store: when not in table
#retrieve from table
def fib(n):
    if n < 2:
        return n
    if n not in fib_table:
        result = fib(n - 1) + fib(n-2) # calc
        fib_table[n] = result # store
    return fib_table[n] #retrieve

# time: O(n) calculate each fib once
# space: O(n)

# fib dynamic programming
def fib_dp(n):
    #create table
    table = [0] * (n + 1)
    #set initial values
    table[0] = 0
    table[1] = 1
    #populate table
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i-2]

    #return target
    return table[n]


#Question 1a
coin_denominations = (1,5,10,20,50,100)
cc_table = {}
def cc(amount, num_coins):
    if num_coins == 0 or amount < 0: #no coints to give or negative value
        return 0
    elif amount == 0:
        return 1
    key = (amount, num_coins)
    if key not in cc_table:
        #calculate and store in table
        coin_value = coin_denominations[num_coins - 1]
        case1 = cc(amount - coin_value, num_coins)
        case2 = cc(amount, num_coins - 1)
        result = case1 + case2
        cc_table[key] = result
    
    #retrieve from table
    return cc_table[key]

#Question 1b
def count_change(amount, num_coins):
    table = []
    num_rows = amount + 1
    num_cols = num_coins + 1
    for i in range(num_rows):
        row = [0] * num_cols
        table.append(row)
    # initalize seed values
    for j in range(1, num_cols):
        table[0][j] = 1
    # populate rest of the table
    for k in range(1, num_rows):
        for l in range(1, num_cols):
            coin_value = coin_denominations[l - 1]
            if k - coin_value < 0:
                case1 = 0
            else:
                case1 = table[k - coin_value][l]
            case2 = table[k][l-1]
            table[k][l] = case1 + case2

    #return target value
    return table[amount][num_coins]

# time: O(n*d)
# space: O(n*d)

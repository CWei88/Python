# Question 2
def my_sum(n):
    x = 0
    for i in range(1,n+1):
        x = i * (i+1) + x
    return x

my_sum(5)

#Question 4
def my_sum_recursive(n):
    if n==1:
        return 2
    else:
        return n * (n + 1) + my_sum_recursive(n - 1)


#Question 7
def sum_iterative(term,a,con,b):
    x = 0
    while a <= b:
        x = x + term(a)
        a = con(a)
    return x

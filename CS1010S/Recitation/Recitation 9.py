# Question 1
class Food(object): #inherit from (object)
    def __init__ (self, name, nutrition, good_until):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0

    def sit_there(self, time):
        self.age += time

    def eat(self):
        if self.age < self.good_until:
            return self.nutrition
        else:
            return 0


# Question 2
class AgedFood(Food):
    def __init__(self, name, nutrition, good_until, good_after):
        super().__init__(name, nutrition, good_until) #reference the parent __init__ method
        self.good_after = good_after

    def sniff(self): #by default, the object is passed to the method itself as the first argument
        if self.age > self.good_after: #aged enough
            return True
        return False

    def eat(self):
        if self.sniff():
            return super().eat() #reference to parent.eat 
        else:
            return 0

#Question 3
class VendingMachine(object):
    # cannot inherit from Food as some functions in food cannot be applied to Vending Machine
    # Even though both may use the same argument, we cannot inherit unless there is
    # a meaningful relationship on the two
    def __init__ (self, name, nutrition, good_until):
        self.name = name
        self.nutrition = nutrition
        self.good_until = good_until
        self.age = 0
    
    def sit_there(self, time):
        self.age += time/2

    def sell_food(self):
        return Food(self.name, self.nutrition, self.good_until - self.age)

# if cannot find method in current class,
# then look in parent, all the way up to base object class

# Question 4
def mapn(fn, lsts):
    result = () #type(lsts) is a constructor
    num_cols = len(lsts[0])
    for i in range(num_cols):
        new_col = map(lambda x: x[i], lsts)
        curr_result = tuple(fn(*new_col))
        result += (curr_result,)
    return result
    
        
    

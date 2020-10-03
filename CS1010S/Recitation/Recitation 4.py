# Recitation 4

##Given code##
def make_module(course_code,units):
    return (course_code,units)

def make_units(lecture,tutorial,lab,homework,prep):
    return (lecture,tutorial,lab,homework,prep)

def get_module_code(course):
    return course[0]

def get_module_units(course):
    return course[1]

def get_module_total_units(units):
    return units[0] + units[1] + units[2] + units[3] + units[4]

## Question 4a
def make_empty_schedule():
    return ()

## Question 4b
def add_class(course,schedule):
    return (course,) + schedule

## Question 4c
def total_scheduled_units(schedule):
    total = 0
    for module in schedule:
        module_units = get_module_units(module)
        total += get_module_total_units(module_units)
    return total

## Question 4d
def drop_class(schedule,course):
    i = 0
    for old_module in schedule:
        if old_module != module:
            return schedule[:i] + schedue[i+1:]
        i = i + 1


## Question 4e
def credit_limit(schedule, max_credits):
    x = total_scheduled_units(schedule)
    while x > max_credits:
        schedule = schedule[1:]
        x = total_scheduled_units(schedule)
    return schedule
        

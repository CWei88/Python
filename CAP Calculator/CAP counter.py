Y1S1 = [("A", 4),("A", 4),("A+", 4),("A+",4),("A+",4)]

grade_dict ={"NUS":{"A+":5.0, "A":5.0, "A-":4.5,
                    "B+":4.0, "B":3.5, "B-":3.0,
                    "C+":2.5, "C":2.0, "D+":1.5,
                    "D":1.0, "F":0.0, "S":0.0, "U":0.0},
             "NTU":{"A+":5.0, "A":5.0, "A-":4.5,
                    "B+":4.0, "B":3.5, "B-":3.0,
                    "C+":2.5, "C":2.0, "D+":1.5,
                    "D":1.0, "F":0.0, "S":0.0, "U":0.0},
             "SMU":{"A+":4.3, "A":4.0, "A-": 3.7,
                    "B+": 3.3, "B":3.0, "B-":2.7,
                    "C+":2.3, "C":2.0, "C-":1.7,
                    "D+":1.3, "D":1.0, "F":0.0,
                    "S":0.0, "U":0.0}}

def grade_count(uni, *grades):
    curr_grades = []
    for grade in grades:
        for i in range(len(grade)):
            if 'S' in grade[i]:
                grade.pop(i)
                grade.insert(i,('S', 0))
            elif 'U' in grade[i]:
                grade.pop(i)
                grade.insert(i, ('U', 0))

    for grade in grades:
        curr_grades.extend(grade)
    total_points = list(map(lambda x:grade_dict[uni][x[0]], curr_grades))
    mcs = list(map(lambda x: x[1], curr_grades))
    total_mc = 0

    for pt, mc in zip(total_points, mcs):
        total_mc += pt * mc
    result = total_mc/sum(mcs)
    if uni == "SMU":
        if result > 4.0:
            return 4.0
    return result

def sem_input(uni):
    sem_res = input("Please input your grades with commas: ")
    sem_res = sem_res.split(",")
    if is_int(sem_res) or is_int(sem_res) == None:
        print("Results input cannot be integers. Please try again.")
        return sem_input()
    sem_res = tuple(map(lambda x: x.upper(), sem_res))

    for grade in sem_res:
        if grade not in grade_dict[uni].keys():
            print("You have entered an invalid grade. Please try again.")
            return sem_input() 
    
    
    ##Find MCs##
    sem_mc = input("Please input your MC with commas: ")
    sem_mc = sem_mc.split(",")
    if not is_int(sem_mc) or is_int(sem_mc) == None:
        print("MC input cannot be strings. Please try again.")
        return sem_input()
    sem_mc = tuple(map(lambda x: int(x), sem_mc))

    ##Checking if the number of results given is more than MCs##
    if len(sem_res) > len(sem_mc): 
        print("You have more grades than MCs. Please reinput.")
        return sem_input()
    
    ##Checking if the number of MCs given is more than result##
    elif len(sem_mc) > len(sem_res):
        print("You have more MC than the grades given. Please reinput.")
        return sem_input()
    
    ##Combining them into a list##
    res = []
    for grad, mc in zip(sem_res, sem_mc):
        res.append((grad, mc))
    return res

##Check whether string is an integer##
def is_int(string):
    vale = 0
    for char in string:
        try:
            int(char)
        except ValueError:
            vale += 1
            continue
    if vale == len(string):
        return False
    elif vale == 0:
        return True
    else:
        return None


    

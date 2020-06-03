grade_dict ={"NUS":{"A+":5.0, "A":5.0, "A-":4.5,
                    "B+":4.0, "B":3.5, "B-":3.0,
                    "C+":2.5, "C":2.0, "D+":1.5,
                    "D":1.0, "F":0.0, "S":0.0, "U":0.0},
             "NTU":{"A+":5.0, "A":5.0, "A-":4.5,
                    "B+":4.0, "B":3.5, "B-":3.0,
                    "C+":2.5, "C":2.0, "D+":1.5,
                    "D":1.0, "F":0.0, "S":0.0, "U":0.0},
             "SMU":{"A+":4.3, "A":4.0, "A-":3.7,
                    "B+":3.3, "B":3.0, "B-":2.7,
                    "C+":2.3, "C":2.0, "C-":1.7,
                    "D+":1.3, "D":1.0, "F":0.0,
                    "S":0.0, "U":0.0}}

def grade_count(uni, grades):
    curr_grades = []
    for grade in grades:
        for i in range(len(grade)):
            ## Making S grade to be 0 MC
            if 'S' in grade[i] or 'CS' in grade[i]:
                grade.pop(i)
                grade.insert(i,('S', 0))
            ## Making U grade to be 0 MC
            elif 'U' in grade[i] or 'CU' in grade[i]:
                grade.pop(i)
                grade.insert(i, ('U', 0))

    ## Adding grades to curr_grades
    for grade in grades:
        curr_grades.extend(grade)
        
    total_points = list(map(lambda x:grade_dict[uni][x[0]], curr_grades))
    mcs = list(map(lambda x: x[1], curr_grades))
    total_mc = 0

    ##Calculating total MC
    for pt, mc in zip(total_points, mcs):
        total_mc += pt * mc
    result = round(total_mc/sum(mcs),2)
    
    
    print(f"Your estimated CAP is: {result}")

def sem_grades(uni, i):
    if i == 0:
        msg = f"Please input your grades for the {i+1}st semester, seperated by commas: "
    elif i == 1:
        msg = f"Please input your grades for the {i+1}nd semester, seperated by commas: "
    else:
        msg = f"Please input your grades for the {i+1}th semester, seperated by commas: "
    
    sem_res = input(msg)
    sem_res = sem_res.strip()
    sem_res = sem_res.split(",")
    if is_int(sem_res) or is_int(sem_res) is None:
        print("Results input cannot be integers. Please try again.")
        return sem_grades(uni, i)
    sem_res = tuple(map(lambda x: x.upper(), sem_res))

    for grade in sem_res:
        if grade not in grade_dict[uni]:
            print("You have entered an invalid grade. Please try again.")
            return sem_grades(uni, i) 
    
    
    ## Find number of credits
    if i == 0:
        mc_msg = f"Please input the number of credits for the {i+1}nd semester per module in order, seperated by commas: "
    elif i == 1:
        mc_msg = f"Please input the number of credits for the {i+1}nd semester per module in order, seperated by commas: "
    else:
        mc_msg = f"Please input the number of credits for the {i+1}th semester per module in order, seperated by commas: "
        
    sem_mc = input(mc_msg)
    sem_mc = sem_mc.strip()
    sem_mc = sem_mc.split(",")
    if not is_int(sem_mc) or is_int(sem_mc) is None:
        print("Credit input cannot be strings. Please try again.")
        return sem_grades(uni)
    sem_mc = tuple(map(lambda x: int(x), sem_mc))

    ## Checking if the number of results given is more than the number of credits
    if len(sem_res) > len(sem_mc): 
        print("You have more grades given than the number of credited modules. Please try again.")
        return sem_grades(uni, i)
    
    ##Checking if the number of credits given is more than the number of results
    elif len(sem_mc) > len(sem_res):
        print("You have more number of credited modules than the grades given. Please try again.")
        return sem_grades(uni, i)
    
    ## Combining them into a list
    res = []
    for grad, mc in zip(sem_res, sem_mc):
        res.append((grad, mc))
    return res

## Checks whether string is an integer
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

## Asks for university
def uni_qn():
    uni = input("Please enter the university that you are from: ")
    uni = uni.upper()
    uni = uni.strip()
    if uni not in grade_dict:
        print('Sorry, you have entered an unsupported university. This calculator only supports NUS, NTU and SMU. Please try again.')
        ans = input('Do you still want to continue? Y/N: ')
        if ans == "Y":
            return uni_qn()
        else:
            print('Goodbye')
    return uni

def how_many_sems(uni):
    noOfSems = input("How many semesters of results do you want to calculate? ")
    noOfSems = int(noOfSems)

    sem_results = []
    for i in range(noOfSems):
        res = sem_grades(uni, i)
        sem_results.append(res)

    return grade_count(uni, sem_results)

uni = uni_qn()
how_many_sems(uni)

    

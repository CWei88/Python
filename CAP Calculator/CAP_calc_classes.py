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

class university:
    def __init__(self, uni):
        self.uni = uni


class CAPCalc(university):
    def __init__(self, uni):
        super().__init__(uni)

    def get_uni(self):
        return self.uni

    def sem_grades(self, grades, credit):
        if is_int(grades) or is_int(grades) is None:
            print("Results input cannot be integers. Please try again.")
            return self.sem_grades(grades, credit)
        sem_res = tuple(map(lambda x: x.upper(), grades))

        for grade in sem_res:
            if grade not in grade_dict[self.uni]:
                print("You have entered an invalid grade. Please try again.")
                return self.sem_grades(grades, credit) 
        
        
        ## Find number of credits
        if not is_int(credit) or is_int(credit) is None:
            print("Credit input cannot be strings. Please try again.")
            return self.sem_grades(grades, credit)
        sem_mc = tuple(map(lambda x: int(x), credit))

        ## Checking if the number of results given is more than the number of credits
        if len(sem_res) > len(sem_mc): 
            print("You have more grades given than the number of credited modules. Please try again.")
            return self.sem_grades(grades, credit)
        
        ##Checking if the number of credits given is more than the number of results
        elif len(sem_mc) > len(sem_res):
            print("You have more number of credited modules than the grades given. Please try again.")
            return self.sem_grades(grades, credit)
        
        ## Combining them into a list
        res = []
        for grad, mc in zip(sem_res, sem_mc):
            res.append((grad, mc))
        return res

    def grade_count(self, grades):
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
            
        total_points = list(map(lambda x:grade_dict[self.uni][x[0]], curr_grades))
        mcs = list(map(lambda x: x[1], curr_grades))
        total_mc = 0

        ##Calculating total MC
        for pt, mc in zip(total_points, mcs):
            total_mc += pt * mc
        result = round(total_mc/sum(mcs),2)
        
        
        return result


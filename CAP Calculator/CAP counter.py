def grade_count(*grades):
    grade_dict ={"A+":5.0, "A":5.0, "A-":4.5,
                 "B+":4.0, "B":3.5, "B-":3.0,
                 "C+":2.5, "C":2.0, "D+":1.5,
                 "D":1.0, "F":0.0, "S":0.0, "U":0.0}
    
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
    total_points = list(map(lambda x:grade_dict[x[0]], curr_grades))
    mcs = list(map(lambda x: x[1], curr_grades))
    total_mc = 0

    for pt, mc in zip(total_points, mcs):
        total_mc += pt * mc
    return total_mc/sum(mcs)

    

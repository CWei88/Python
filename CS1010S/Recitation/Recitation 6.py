# Question 2
# stable sort
def bubble_sort(lst):
    n = len(lst)
    # repeat n - 1 times
    for j in range(n - 1):
        # One pass O(n)
        for i in range(n - 1 - j):
            if ls[i] > ls[i+1]:
                ls[i],ls[i+1] = ls[i+1],ls[i]


# Time: O(n**2)
# Space: O(1)


#Question 3
# unstable sort
def selection_sort(lst):
    n = len(lst)
    for anch in range(n-1):
        for other in range(anch+1,n):
            if lst[other] < lst[anch]:
                lst[other], lst[anch] = lst[anch], lst[other]
    return ls


#Time: O(n**2)
#Space: O(1)


#Question 4
students = [('tiffany','A',15),
            ('jane','B',10),
            ('ben','C',8),
            ('simon','A',21),
            ('john','A',15),
            ('jimmy','F',1),
            ('charles','C',9),
            ('freddy','D',4),
            ('dave','B',12)]

# a)
# students.sort(reverse = True)
# print(students)

# b)
students.sort(key = lambda t: (t[1], t[0])) # by grade then by name
# Or
students.sort(key = lambda x: x[0]) # by name
students.sort(key = lambda x: x[1]) # by grade (priority)
print(students)


#c)
def names_less_than_6(lst):
    tup = ()
    for students in lst:
        if len(students[0]) < 6:
            tup = tup + (students[0],)
    return tup

#OR

tuple(student[0] for student in students if len(students[0]) < 6)

#OR

tuple(filter(lambda name: len(name) < 6,
       map(lambda stud: stud[0], students)))

#d)
def number_of_grades(lst):
    tup = ()
    grades = ['A','B','C','D','F']
    i = 0
    while i < len(grades):
        count = 0
        for students in lst:
            if students[1] == grades[i]:
                count = count + 1
        tup = tup + ((grades[i],count),)
        i = i + 1
    return tup

def better_count(lst):
    all_grades = list(map(lambda s: s[1], students))
    unique_grades = []
    for grade in all_grades:
        if grade not in unique_grades:
            unique_grades.append(grade)

    result = ()
    for grade in unique_grades:
        count = all_grades.count(grade)
        pair = (grade,count)
        result += (pair,)
    return result

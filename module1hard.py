grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
sort_students = sorted(students)

import statistics
grades[0] = statistics.mean(grades[0])
grades[1] = statistics.mean(grades[1])
grades[2] = statistics.mean(grades[2])
grades[3] = statistics.mean(grades[3])
grades[4] = statistics.mean(grades[4])
flt_grades = [float(i) for i in grades]

my_dict = {}
for i in range(len(flt_grades)):
    my_dict[sort_students[i]] = flt_grades[i]
    
print('Средний балл: ', my_dict)



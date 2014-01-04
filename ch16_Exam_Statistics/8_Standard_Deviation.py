grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def print_grades(grades):
    for grade in grades:
        print grade

def grades_sum(grades):
    total = 0
    for grade in grades:
        total += grade
    return total

def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades * 1.0/ len(grades)
    return average

def grades_variance(grades, average):
    variance = 0.0
    for grade in grades:
        variance += (grade - average) ** 2
    return variance / len(grades)

def grades_std_deviation(variance):
    return variance ** 0.5

print grades_std_deviation(grades_variance(grades, grades_average(grades)))

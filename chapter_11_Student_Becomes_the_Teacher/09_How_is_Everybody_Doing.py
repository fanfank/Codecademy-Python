lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(lst):
    ans = 0.0
    cnt = 0
    for e in lst:
        ans += e
        cnt += 1
    return ans / cnt

def get_average(student):
    return (average(student["homework"]) * 0.1 + average(student["quizzes"]) * 0.3 + average(student["tests"]) * 0.6)

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def get_class_average(students):
    ans = 0.0
    cnt = 0
    for student in students:
        ans += get_average(student)
        cnt += 1
    return ans / cnt

students = [lloyd, alice, tyler]
avg = get_class_average(students)
print avg
print get_letter_grade(avg)
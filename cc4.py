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
students = ["lloyd", "alice", "tyler"]
# Add your function below!
def get_class_average(students):
    results = []
    class_total = 0
    for x in students:
        results += get_average(x)
  

def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    return "F"

def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    return total

def get_average(students):
    homework = average(students["homework"])
    quizzes = average(students["quizzes"])
    tests = average(students["tests"])
    return homework * 0.1 + quizzes * 0.3 + tests * 0.6

get_class_average(students)
    

    
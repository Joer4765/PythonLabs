def get_score(student, home_work, exam):
    hw_average = sum(home_work) / len(home_work)
    grade = round(0.4 * hw_average + 0.6 * exam)
    return f"Студент {student} – ваша підсумкова оцінка за іспит {grade}"


print(get_score('Melnyk', (90, 85, 88, 92, 86, 87), 91))

def grading(grade):
    a = ""
    if 2 <= grade <= 2.99:
        a = "Fail"
    elif 3 <= grade <= 3.49:
        a = "Poor"
    elif 3.5 <= grade <= 4.49:
        a = "Good"
    elif 4.5 <= grade <= 5.49:
        a = "Very Good"
    elif 5.5 <= grade <= 6:
        a = "Excellent"
    return a


print(grading(float(input())))

#!/bin/python3
import os


def gradingStudents(grades):

    for i in range(len(grades)):
        grade = grades[i]
        if grade >=38:
            difrence = ((grade-(grade%5))+5)-grade
            if difrence < 3:
                grades[i] = grade+difrence
    return grades



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

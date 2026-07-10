# collection_namedtuple_function.py

from collections import namedtuple

if __name__ == "__main__":
    num_of_student = int(input().strip())

    columns = input().split()

    Student = namedtuple('Student', columns)

    total_marks = 0

    for _ in range(num_of_student):
        student_data = Student(*input().split())

        total_marks += int(student_data.MARKS)
    print(f"{total_marks / num_of_student:.2f}")


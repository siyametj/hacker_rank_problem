# nested_loop_problem.py

if __name__ == "__main__":
    all_student = []
    scores = set()

    for _ in range(int(input())):
        name = input()
        score = float(input())

        all_student.append([name, score])
        scores.add(score)

    second_lowest = sorted(scores)[1]

    desired_students = [student[0] for student in all_student if student[1] == second_lowest]

    for n in sorted(desired_students):
        print(n)

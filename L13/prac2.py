from collections import deque

# xep hang doi lay banh -> dem so nguoi k lay duoc banh


def count_students_unable_to_eat(sandwiches, students):
    # ep kieu -> dqueue
    students = deque(students)
    sandwiches = deque(sandwiches)

    count = 0
    while students and sandwiches:
        # lay phan tu o dau 2 danh sach
        if students[0] == sandwiches[0]:
            students.popleft()
            sandwiches.popleft()
            count = 0
        else:
            # neu khong trung khop -> day student xuong cuoi
            std = students.popleft()
            students.append(std)
            count += 1
            # neu xoay het 1 lan -> dung
            if count == len(students):
                break

    return len(students)
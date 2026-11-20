from student import *

grades = [20, 15, 17, 18]

name = input("Enter student name: ")

avg = get_avg(grades)

print("student:", name)
print("Avg =", avg)
print("max =", get_max(grades))
print("min =", get_min(grades))
print("status =", get_status(avg))

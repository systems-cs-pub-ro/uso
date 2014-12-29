#!/usr/bin/env python

import string

input_filename="../students.txt"

# Initialize grades.
# grades is a dictionary. Each item in the dictionary belongs to a group.
# Each item is a dictionary itself with each subtitem belonging to a grade
# from 1 to 10.
grades = {}
for group in ['311CC', '312CC', '313CC', '314CC', '315CC']:
    arr = {}
    for grade in range(1, 11):
        arr[grade] = 0
    grades[group] = arr

# Parse file and increment values in the grades dictionary.
for line in open(input_filename):
    (name, group, final_grade, test_grade, practical_grade) = string.split(line.strip(), '\t')
    grades[group][int(final_grade)] += 1

# Print grades.
for grade in range(1, 11):
    print grade,
    for group in ['311CC', '312CC', '313CC', '314CC', '315CC']:
        print grades[group][grade],
    print ""

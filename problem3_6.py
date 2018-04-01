# -problem3_6.py *- coding: utf-8 -*-

import sys

# add your code here
first_file_name = sys.argv[1]
second_file_name = sys.argv[2]
first_file = open(first_file_name)
second_file = open(second_file_name, 'w')
for line in first_file:
    line = line.strip("\n")
    second_file.write(str(len(line)))
    second_file.write("\n")
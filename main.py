"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""

# class CFGStudent:
#
#     def __init__(self, name, surname, age, email, student_id=None):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.email = email
#         self.student_id = student_id or self.generate_id()
#
#
#     @staticmethod
#     def generate_id():
#         def generate_id():
#         return str(random.randrange(1000, 1000))
#
#     def get_id(self):
#         return self.student_id


#     def get_id(self):
#         class NanoStudent(CFGStudent):
#
#             def __init__(self, stream, name, surname, age, email, student_id=None ):
#                 super().__init__(self, name, surname, age, email, student_id=None)
#                 self.specialization = stream
#                 self.course_grades = dict()
#
#     def get_fullname(self):
#         return "{} {}".format(self.name, self.surname)
#
#
#
# class NanoStudent(CFGStudent):

# def __init__(self, 'self, name, surname, age, email, student_id=None'):
#     r = CFGStudent('rabia', 'tanweer', 20, 'random101@gmail')
#     print(r.get_fullname())
#     print(r.student_id)
#
#
# @staticmethod
# def generate_id():
#     cfg_s = NanoStudent('SQL', name='Rabia', surname='Tanweer', age=20, email='random@gmail.com')
#     print(cfg_s.get_fullname())
#     print(cfg_s.get_id())
#
#

# def add_new_grade(self, 'your code goes here'):
#     cfg_s.add_new_grade('theory', 95)
#     cfg_s.add_new_grade('project', 78)
#     print(cfg_s.get_course_grades())
#
#
# def get_course_grades(self):
#     def add_new_grade(self, task, mark):
#         self.course_grades[task] = mark
#
#     def get_course_grades(self):
#         return self.course_grades

# TASK 2
#
# Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence
# and return the sum of all even Fibonacci numbers. See more details in the task description in
# your assessment paper.
# """


##### TESTS ####

# print(even_fibonacci_sum(limit=10))  # should be 44
# print(even_fibonacci_sum(limit=15))  # should be 188
# print(even_fibonacci_sum(limit=1))   # should be 0



# def even_fibonacci_sum(limit):
#     if (limit < 2):
#         return 0
#
#     ef1 = 0
#     ef2 = 2
#     sm = ef1 + ef2
#
#
#     while (ef2 <= limit):
#         ef3 = 4 * ef2 + ef1
#         if (ef3 > limit):
#             break
#             ef1 = ef2
#             ef2 = ef3
#             sm = sm + ef2
#             return sm
#             limit = 6765
#
#             def even_fibonacci_sum(limit):
#                 indexes = [x for x in range(limit)]
#              print('indexes: ', indexes)
#
#             even_fibs = [fibonacci(i) for i in indexes if fibonacci(i) % 2 == 0]
#             print('even Fib numbers: ', even_fibs)
#
#             return sum(even_fibs)
#

"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""



#### TESTS ####

# array1 = [5,1,22,25,6,-1,8,10]
# sequence1 = [1,6,-1,-2]
#
# print(is_valid_subsequence(array1, sequence1))  # FALSE
#
#
# array2 = [5,1,22,25,6,-1,8,10]
# sequence2 = [1,6,-1, 10]
#
# print(is_valid_subsequence(array2, sequence2))  # TRUE
#
#
# array3 = [5,1,22,25,6,-1,8,10]
# sequence3 = [25]
#
# print(is_valid_subsequence(array3, sequence3))  # TRUE

def is_valid_subsequence(array, sequence):
    seq_idx = 0
    for value in array:
        if seq_idx == len(sequence):
            break
        if sequence[seq_idx] == value:
            seq_idx += 1
    return seq_idx == len(sequence)


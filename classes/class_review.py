# class_review.py

class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []


    # Add an .add_grade() method to Student that takes a parameter, grade.
    # .add_grade() should verify that grade is of type Grade and if so, add it to the Student‘s .grades.
    # If grade isn’t an instance of Grade then .add_grade() should do nothing.

    def add_grade(self, grade):
        if type(grade) == Grade:
            self.grades.append(grade)

# Create three instances of the Student class:

# Roger van der Weyden, year 10
# Sandro Botticelli, year 12
# Pieter Bruegel the Elder, year 8
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade:
    minimum_passing = 65

    def __init__(self, score):
        self.score = score


pieter.add_grade(Grade(100))

# Challenges

# Write a Grade method .is_passing() that returns whether a Grade has a passing .score.
# Write a Student method get_average() that returns the student’s average score.
# Add an instance variable to Student that is a dictionary called .attendance, with dates as keys and booleans as values that indicate whether the student attended school that day.
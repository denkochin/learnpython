'''
# Работа со строками
phrase = "Giraffe Academy"
print(phrase.lower())  # giraffe academy
print(phrase.upper())  # GIRAFFE ACADEMY
print(phrase.islower())  # False
print(phrase.isupper())  # False
print(len(phrase))  # 15
print(phrase[0])  # G
print(phrase.index("Acad"))  # 8
print(phrase.replace("Giraffe", "Elephant"))  # Elephant Academy

# Working with numbers
print(2)
print(2.0987)
print(-2.0987)
print(3 + 4)
print(3 - 4)
print(3 / 4)
print(3 / 4)
print(3 % 2)
my_num = 5
print(my_num)
print(str(my_num))
print(abs(-5))
print(pow(2, 16))
print(max(4, 6))
print(min(4, 6))
print(round(3.4), round(3.5), round(3.6), round(-0.4), round(-0.5), round(-0.6))
from math import *
print(ceil(3.1))
print(floor(3.7))
print(sqrt(64))

# Getting Input From Users
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

# Building a Basic Calculator
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
print(result)

# Mad Libs Game
color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")
print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

# Lists ...
# List Functions ...
# Tuples
# Functions
# Return
# If statement
# If and conditions
# Upgrading calculator
# Dictionaries
# While
# Guessing game
# For
# Exponential function
# 2D-lists and nested lists
# Translator
# Comments
# Try / Except

# Read files
file = open("prestuplenie-i-nakazanie.txt", "r")
# print(file.readline())
# print(file.readlines()[2])
for line in file.readlines():
     if line != "\n":
         print(line.strip())
file.close()

# Writting a file
def append_to_file(filename, newtext):
    """Добавляет текст в конец указанного файла
    :param filename: имя файла в корневой папке
    :param newtext: добавляемый текст"""
    file = open(filename, "a")
    file.write(newtext)
    file.close()
append_to_file("prestuplenie-i-nakazanie.txt", "New line appended to a file")

def create_file(filename, text):
    """Создать новый файл с указанным текстом
    :param filename: имя файла в корневой папке
    :param text: добавляемый текст"""
    file = open(filename, "w", encoding="UTF-8")
    file.write(text)
    file.close()
create_file("file1", "Текст, добавленный в новый файл")


# Modules and pip
import imp
import useful_tools

print(useful_tools.roll_dice(10))

# list of all python native modules https://docs.python.org/3/py-modindex.html


# Classes and Objects
from Student import Student


student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
print(student1.name, student2.gpa)


# Building a Multiple Choice Quiz
from Question import Question


question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)


# Object Functions
from Student2 import Student2

student1 = Student2("Oscar", "Accounting", 3.1)
student2 = Student2("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
'''

# Inheritance
from Chef import Chef
from ChineseChef import ChineseChef


myChef = Chef()
myChef.make_chicken()
myChef.make_salad()
myChef.make_special_dish()
print()
myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_salad()
myChineseChef.make_special_dish()
myChineseChef.make_fried_rice()

import random

# class student:
#     educational_platform = 'Udemy'

#     def __init__(self, name, age = 10):
#         self.s_name = str(name)
#         self.s_age = age

#     def greet(self):
#         greet = ["Hi, I'm ", "Hey there, my name is ", "Hi. Oh, my name is "]
#         print(random.choice(greet), self.s_name)


# s1 = student('Abhishek',30)
# for i in range(4):
#     s1.greet()


class Student:
    educational_platform = 'Udemy'

    def __init__(self, name, age = 30):
        self.name = name
        self.age = age

    def greet(self):
        _greetings = [
            "Hi, I'm {}",
            "Hey there, my name is {}",
            "Hi. Oh, my name is {}"
        ]

        greetings = random.choice(_greetings)

        return greetings.format(self.name)
    
#helper function
def class_create(student_name):
    return [Student(name) for name in student_name]

#whether name of this file is main
if __name__ == "__main__":
    names= ['Abhishek','Raj', 'Rahul','Dhiraj', 'Ajit']

    for student in class_create(names):
        print(student.greet())

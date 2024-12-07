class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_grade = 0

    def rate_hw(self, lecture, course, grade):
        if isinstance(lecture, Lecture) and course in lecture.courses_attached and course in self.courses_in_progress:
            if course in lecture.grades:
                lecture.grades[course] += [grade]
            else:
                lecture.grades[course] = [grade]
            sum_of_grades = sum([sum(grades_list) for grades_list in lecture.grades.values()])
            raiting_count = sum(len(grades_list) for grades_list in lecture.grades.values())
            lecture.average_grade = round(sum_of_grades / raiting_count, 1)
            return lecture.average_grade
        else:
            return 'Ошибка'

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашнее задание: {self.average_grade}\n'
            f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
            f'Завершённые курсы: {', '.join(self.finished_courses)}\n'
        )

    def __eq__(self, other):
        return self.average_grade == other.average_grade

    def __lt__(self, other):
        return self.average_grade < other.average_grade


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecture(Mentor):
   def __init__(self, name, surname):
       super().__init__(name, surname)
       self.grades = {}
       self.average_grade = 0

   def __str__(self):
       return (
           f'Имя: {self.name}\n'
           f'Фамилия: {self.surname}\n'
           f'Средняя оценка за лекции: {self.average_grade}\n'
       )

   def __eq__(self, other):
       return self.average_grade == other.average_grade

   def __lt__(self, other):
       return self.average_grade < other.average_grade

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            sum_of_grades = sum([sum(grades_list) for grades_list in student.grades.values()])
            raiting_count = sum(len(grades_list) for grades_list in student.grades.values())
            student.average_grade = round(sum_of_grades / raiting_count, 1)
            return student.average_grade
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
        )

def average_student_grade(students:list, course:str):
    sum_of_grades, raiting_count = 0, 0
    for student in students:
        if isinstance(student, Student) and course in student.courses_in_progress:
            sum_of_grades += sum(student.grades[course])
            raiting_count += len(student.grades[course])
    return round(sum_of_grades / raiting_count, 1)

def average_lecture_grade(lecturs:list, course:str):
    sum_of_grades, rating_count = 0, 0
    for lecture in lecturs:
        if isinstance(lecture, Lecture) and course in lecture.courses_attached:
            sum_of_grades += sum(lecture.grades[course])
            rating_count += len(lecture.grades[course])
    return round(sum_of_grades / rating_count, 1)


student1 = Student('Антон', 'Городецкий', 'Муж')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['Java']
student1.finished_courses += ['SQL']

student2 = Student('Алиса', 'Селезнёва', 'Жен')
student2.courses_in_progress += ['Python']
student2.courses_in_progress += ['SQL']
student2.finished_courses += ['Java']

lecture1 = Lecture('Сергей', 'Лукьяненко')
lecture1.courses_attached += ['Python']
lecture1.courses_attached += ['SQL']

lecture2 = Lecture('Кир', 'Булычёв')
lecture2.courses_attached += ['Python']
lecture2.courses_attached += ['Java']

reviewer1 = Reviewer('Аркадий', 'Стругацкий')
reviewer1.courses_attached += ['Java']
reviewer1.courses_attached += ['Python']

reviewer2 = Reviewer('Владислав', 'Крапивин')
reviewer2.courses_attached += ["Python"]
reviewer2.courses_attached += ["SQL"]

student1.rate_hw(lecture1, 'Python', 6)
student1.rate_hw(lecture1, 'Python', 9)
student1.rate_hw(lecture2, 'Java', 10)
student2.rate_hw(lecture1, 'Python', 5)
student2.rate_hw(lecture1, 'SQL', 7)
student2.rate_hw(lecture2, 'Python', 6)

reviewer1.rate_hw(student1, 'Java', 5)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'SQL', 7)
reviewer2.rate_hw(student1, 'Python', 5)

print(student1, end='\n')
print(student2, end='\n')
print(lecture1, end='\n')
print(lecture2, end='\n')
print(reviewer1, end='\n')
print(reviewer2, end='\n')

print(student1 < student2)
print(lecture1 > lecture2, end='\n\n')

print(average_student_grade([student1, student2], 'Python'))
print(average_lecture_grade([lecture1, lecture2], 'Python'))



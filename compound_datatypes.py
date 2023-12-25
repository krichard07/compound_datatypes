# Exercise 1: List Manipulation:

fruits = ["apple", "banana", "cherry", "date"]

fruits.append("elderberry")
fruits.pop(1)
fruits.sort()

print(fruits)
print()

# Exercise 2: Dictionary Basics:

students = {"name": "John Doe", "age": 25, "major": "Computer Science"}

students["major"] = "Electrical Engineering"
students["year"] = "Senior"
print(students.keys())
print(students.values())
print()

# Exercise 3: List of Dictionaries:

books = [
    {"title": "The Lord of the Rings", "author": "J. R. R. Tolkien", "year": 2003,},
    {"title": "A Song of Ice and Fire", "author": "George R. R. Martin", "year": 1996,},
    {"title": "Witcher", "author": "Andrzej Sapowski", "year": 1986}
]

print("The title of the second book:", books[1]["title"])
print("Year of publication of the third book:", books[2]["year"])
print()

for book in books:
    print("Title:", book["title"])
    print("Author:", book["author"])
    print()

# Exercise 4: Dictionary containing a List:

def add_student(course_dict, course_name, new_students):
     course_dict[course_name].extend(new_students)

def remove_sudents(course_dict, course_name, index):
     del course_dict[course_name][index]

def print_students(course_dict, course_name):
     print(f"The students in {course_name}: {', '.join(course_dict[course_name])}")

def add_course(course_dict, new_course, new_students):
     course_dict[new_course] = new_students


courses = {
    "math": ["Mike", "Frank", "Kevin", "Richard", "Grant"],
    "history": ["Alice", "Bob", "Alfred", "David"],
    "chemistry": ["Emma", "Grace", "Henry", "Ivy", "Bruce"]
}

add_student(courses, "math", ["Jane", "Mark", "Peter", "John", "Hugo"])
remove_sudents(courses, "history",2)
print_students(courses, "chemistry")
add_course(courses, "physics",["Adam", "Eddie", "Gwen", "Miles"])

for course, students in courses.items():
    print(f"{course}: {', '.join(students)}")
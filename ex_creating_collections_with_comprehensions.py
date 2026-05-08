words = ["bib", "bias", "dad", "eye", "deed", "tooth"]
colors = ["blue", "yellow", "red"]
toys = ["bike", "doll", "car"]
numbers = [-2, 3, 4, 6, 7, 99, 45]
NUM_SQUARES = 10*1000*1000


def is_palindrome(s: str) -> bool:
    return s == s[::-1]


def is_mult_of_2_or_3(num: int) -> bool:
    return (num % 2 == 0) or (num % 3 == 0)


palindroms_with_comprehensions = [word for word in words if is_palindrome(word)]
print(palindroms_with_comprehensions)

multiple_toys = [f"{color} {toy}" for color in colors for toy in toys]
print(multiple_toys)

numbers_2_or_3 = [n for n in numbers if is_mult_of_2_or_3(n)]
print(numbers_2_or_3)

many_squares = (n * n for n in range(NUM_SQUARES))
print(f"{type(many_squares)=}")


class Student:
    def __init__(self, name, gpa, major):
        self.name = name
        self.gpa = gpa
        self.major = major


students = [Student('John Doe', 3.9, 'Computer Science'),
            Student('Elize Johns', 4.2, 'Economics'),
            Student('Alan Parker', 4.0, 'Economics')
            ]

# Dict comprehension
dict_comp = {student.name: student.major for student in students}
print(f"{dict_comp=}")

# Set comprehension
set_comp = {student.name for student in students}
print(f"{set_comp=}")

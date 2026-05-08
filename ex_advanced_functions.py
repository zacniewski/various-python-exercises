from operator import attrgetter


def foo(a, b, x=2, y=3):
    return (a+b) / (x+y)


def takes_any_args(*args):
    print(f"The args are: {args}")
    print(f"Type of args is: {type(args)}")


some_foo = foo(b=4, x=3, a=5)
print(f"{some_foo=}")

print(takes_any_args(1, 2))
print(takes_any_args([1, 2]))


def normal_function(a, b, c):
    print(f"{a=}, {b=}, {c=}")


some_numbers = (3, 6, 7)
normal_function(*some_numbers)


# args and kwargs together
def addup(a, b, c=1, d=2, e=3):
    return a + b + c + d + e


nums = (3, 4)
extras = {'d': 55, 'e': 66}

print(addup(*nums, **extras))

some_items = [3, -5, 1, -23, 2, 4]


def max_by_key(items, key):
    biggest = items[0]
    for item in items[1:]:
        if key(item) > key(biggest):
            biggest = item
    return biggest


print(max_by_key(some_items, abs))


class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def __repr__(self):
        return f"{self.name}: {self.gpa}"


student_objs = [
    Student("John Doe", "CS", 4.2),
    Student("Adam Smith", "Physics", 3.8),
    Student("Betty Boo", "Economics", 3.9)
]

sorted_by_gpa = sorted(student_objs, key=attrgetter('gpa'))
print(sorted_by_gpa)

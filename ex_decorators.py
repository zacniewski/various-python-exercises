# Decorators

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


person = Person("John", "Doe")
print(person.full_name)


# Ex 2
def printlog(func):
    def wrapper(*args, **kwargs):
        print(f"CALLING {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


# Class - based version of the "add " decorator above
class Add:
    def __init__(self, increment):
        self . increment = increment

    def __call__(self,func):
        def wrapper(n):
            return func(n) + self . increment
        return wrapper


@Add(4)
def bar(n):
    return n * 2


print(f"{bar(77)=}")


@printlog
def foo(x):
    print(f"{x + 2 = }")


foo(8)


class Printlog:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f"CALLING {self.func.__name__}")
        return self.func(*args, **kwargs)


@Printlog
def foo2(x):
    print(f"{x + 3 = }")


foo2(11)

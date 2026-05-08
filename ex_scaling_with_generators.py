# Iteration with iter()
print("Powerful Python has just started!")

numbers = [7, 4, 11, 3]
numbers_iter = iter(numbers)

# Checking __iter__ magic method
print(f"{list(numbers_iter)=}")
print(f"{id(numbers)=}")
print(f"{id(numbers_iter)=}")
print(f"{numbers.__iter__=}")
print(f"{numbers_iter.__iter__=}")

names = ["Tom", "Shelly", "Garth"]
names_iter = iter(names)
print(f"{next(names_iter)=}")

print(f"{next(names_iter)=}")

print(f"Squares numbers with generator")


def gen_squares(max_num: int):
    for num in range(max_num):
        yield num ** 2


MAX = 50
for square in gen_squares(MAX):
    print(f"{square=}")


def lines_from_file (path):
    with open(path) as handle:
        for line in handle:
            yield line.rstrip('\n')


def matching_lines(lines, pattern):
    for line in lines:
        if pattern in line:
            yield line


lines = lines_from_file('poem.txt')
matching = matching_lines(lines, 'with')
for line in matching:
    print(line)


def house_records(lines):
    record = {}
    for line in lines:
        if line == '':
            yield record
            record = {}
            continue
        key, value = line.split(': ', 1)
        record[key] = value
    yield record


def house_records_from_file(path):
    lines = lines_from_file(path)
    for house in house_records(lines):
        yield house


for house in house_records_from_file('housedata.txt'):
    print(house["address"])

# Recap built-in functions with generators
numbers = [1, 2, 3, 4]
bigger_numbers = [1000, 1200, 2000, 5000]


def even(number: int) -> bool:
    return number % 2 == 0


# mapping
even_numbers = map(even, numbers)
for en in even_numbers:
    print(en)


# filtering
filtered_numbers = filter(lambda x: x > 1500, bigger_numbers)
for fn in filtered_numbers:
    print(fn)

# zipping
zipped = zip(numbers, bigger_numbers)
for z in zipped:
    print(z)

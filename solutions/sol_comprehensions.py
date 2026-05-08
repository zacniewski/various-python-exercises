nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flattened = [item for sublist in nested_list for item in sublist]

text = "comprehensions are powerful"
char_freq = {char: text.count(char) for char in set(text) if char.strip()}

if __name__ == "__main__":
    print("Flattened:", flattened)
    print("Char Freq:", char_freq)

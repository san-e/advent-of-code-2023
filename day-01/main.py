#https://stackoverflow.com/a/4665027
def find_all(a_str, sub, overlap = False):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        if overlap:
            start += 1
        else:
            start += len(sub)

def main_p1(input: str) -> int:
    digits = ["".join([char for char in line if char.isnumeric()]) for line in input]
    digits = [int("".join([digit[0], digit[-1]])) for digit in digits]

    return sum(digits)

def main_p2(input: str):
    digit_map = {
        "one": "o1ne",
        "two": "tw2o",
        "three": "thr3ee",
        "four": "fo4ur",
        "five": "fi5ve",
        "six": "s6ix",
        "seven": "sev7en",
        "eight": "eig8ht",
        "nine": "ni9ne"
    }
    new_input = []

    for line in input:
        temp = line
        for d_name, d_replacement in digit_map.items():
            temp = temp.replace(d_name, d_replacement)
            
        new_input.append(temp)

    return main_p1(new_input)

def get_input(path: str) -> list:
    with open(path, "r") as f:
        input = f.read().split("\n")
    return input

def get_test_input(path: str) -> tuple:
    input = get_input(path)

    test_answer = int(input[-1:][0])
    test_input = input[:-2]

    return test_input, test_answer 

if __name__ == "__main__":
    test_input, test_answer = get_test_input("./test-input-p1.txt")
    assert main_p1(test_input) == test_answer
    print("Test 1 passed")

    test_input, test_answer = get_test_input("./test-input-p2.txt")
    assert main_p2(test_input) == test_answer
    main_p2(test_input)
    print("Test 2 passed")


    input = get_input("./input.txt")
    answer1 = main_p1(input)
    answer2 = main_p2(input)

    print(f"Answer 1: {answer1}\nAnswer 2: {answer2}")
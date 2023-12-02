import sys
sys.path.append("..")
from aoc_common import get_input, get_test_input

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

if __name__ == "__main__":
    test_input, test_answer = get_test_input("./test-input-p1.txt")
    assert main_p1(test_input) == int(test_answer)
    print("Test 1 passed")

    test_input, test_answer = get_test_input("./test-input-p2.txt")
    assert main_p2(test_input) == int(test_answer)
    main_p2(test_input)
    print("Test 2 passed")


    input = get_input("./input.txt")
    answer1 = main_p1(input)
    answer2 = main_p2(input)

    print(f"Answer 1: {answer1}\nAnswer 2: {answer2}")
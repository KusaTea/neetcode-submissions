from typing import List


def sort_words(words: List[str]) -> List[str]:
    el_idx = 0
    while el_idx < len(words):

        if el_idx > 0 and len(words[el_idx - 1]) < len(words[el_idx]):
            words[el_idx - 1], words[el_idx] = words[el_idx], words[el_idx - 1]
            el_idx -= 1

        elif el_idx < len(words) - 1 and len(words[el_idx]) < len(words[el_idx + 1]):
            words[el_idx], words[el_idx + 1] = words[el_idx + 1], words[el_idx]

        else:
            el_idx += 1
            
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    el_idx = 0
    while el_idx < len(numbers):

        if el_idx > 0 and abs(numbers[el_idx - 1]) > abs(numbers[el_idx]):
            numbers[el_idx - 1], numbers[el_idx] = numbers[el_idx], numbers[el_idx - 1]
            el_idx -= 1

        elif el_idx < len(numbers) - 1 and abs(numbers[el_idx]) > abs(numbers[el_idx + 1]):
            numbers[el_idx], numbers[el_idx + 1] = numbers[el_idx + 1], numbers[el_idx]

        else:
            el_idx += 1
            
    return numbers


# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))

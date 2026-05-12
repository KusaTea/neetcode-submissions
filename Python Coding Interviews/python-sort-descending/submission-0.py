from typing import List


def sort_words(words: List[str]) -> List[str]:
    el_idx = 0
    while el_idx < len(words):

        if el_idx > 0 and words[el_idx - 1] < words[el_idx]:
            words[el_idx - 1], words[el_idx] = words[el_idx], words[el_idx - 1]
            el_idx -= 1

        elif el_idx < len(words) - 1 and words[el_idx] < words[el_idx + 1]:
            words[el_idx], words[el_idx + 1] = words[el_idx + 1], words[el_idx]

        else:
            el_idx += 1
            
    return words


def sort_numbers(numbers: List[int]) -> List[int]:
    el_idx = 0
    while el_idx < len(numbers):

        if el_idx > 0 and numbers[el_idx - 1] < numbers[el_idx]:
            numbers[el_idx - 1], numbers[el_idx] = numbers[el_idx], numbers[el_idx - 1]
            el_idx -= 1

        elif el_idx < len(numbers) - 1 and numbers[el_idx] < numbers[el_idx + 1]:
            numbers[el_idx], numbers[el_idx + 1] = numbers[el_idx + 1], numbers[el_idx]
        
        else:
            el_idx += 1
    
    return numbers

def sort_decimals(numbers: List[float]) -> List[float]:
    el_idx = 0
    while el_idx < len(numbers):

        if el_idx > 0 and numbers[el_idx - 1] < numbers[el_idx]:
            numbers[el_idx - 1], numbers[el_idx] = numbers[el_idx], numbers[el_idx - 1]
            el_idx -= 1

        elif el_idx < len(numbers) - 1 and numbers[el_idx] < numbers[el_idx + 1]:
            numbers[el_idx], numbers[el_idx + 1] = numbers[el_idx + 1], numbers[el_idx]
        
        else:
            el_idx += 1
    
    return numbers



# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))

from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        combinations = []
        self.generate_combinations(digits, 0, '', digit_to_letters, combinations)    
        return combinations    
    
    def generate_combinations(self, digits, index, current, digit_to_letters, combinations):
        if index == len(digits):
            combinations.append(current)
            return

        digit = digits[index]
        letters = digit_to_letters[digit]
        for letter in letters:
            self.generate_combinations(digits, index+1, current+letter, digit_to_letters,combinations)
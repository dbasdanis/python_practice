class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        if num == num[::-1]:
            return True
        else:
            return False


if __name__ == "__main__":
    solution = Solution()
    print(solution.isPalindrome(-121))
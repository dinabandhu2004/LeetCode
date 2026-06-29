class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = x
        reverse = 0
        while temp>0:
            rem = temp%10
            reverse = reverse*10+rem
            temp = temp//10
        if reverse ==x:
            return True
        else:
            return False
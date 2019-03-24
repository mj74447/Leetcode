class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        print(x)
        rev = x[::-1]
        print(rev)
        if rev == x :
                     return True
        else:
                     return False

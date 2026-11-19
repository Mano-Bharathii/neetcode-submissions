class Solution:
    def isPalindrome(self, s: str) -> bool:
        sen = []
        for c in s:
            if c.isalnum():
                sen.append(c.lower())
        
        for i in range(math.ceil(len(sen)/2)):
            print(sen[i], sen[-(i+1)])
            if sen[i] != sen[-(i+1)]:
                return False

        return True
#time taken to solve: 1 hr [Idea and implementation completed within 30 mins. but one "if" logic makes me an headache ]
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 0


        def expand_around_center(l,r):
            nonlocal left
            nonlocal right
            while  l >= 0 and r < len(s) and s[l] == s[r]:
                if right - left < r - l:
                    left = l
                    right = r
                l -= 1
                r += 1   

        for i in range(len(s)):
            #odd
            l = i - 1
            r = i + 1
            expand_around_center(l,r) 
            #even 
            l = i
            r = i + 1
            expand_around_center(l,r)
        return s[left: right + 1]
    
    # def longestPalindrome(self, s: str) -> str:
    #     left = 0
    #     right = 0
    #     for i in range(len(s)):
    #         #odd
    #         l = i - 1
    #         r = i + 1
    #         flag = False
    #         if(i == 1):
    #             print(i,"Before odd l ", l, r)
    #         while  l >= 0 and r < len(s) and s[l] == s[r]:
    #             l -= 1
    #             r += 1
    #             flag = True
    #         if(i == 1):
    #             print(i,"After odd while ", l, r)
    #         if flag and right - left < r - l:
    #             left = l + 1
    #             right = r - 1
    #             print(i, left, right)
    #         if(i == 1):
    #             print(i," Odd com l ", left, right)
                
    #         #even 1
    #         l = i
    #         r = i + 1
    #         if(i == 1):
    #             print(i,"Before even l ", l, r)
    #         flag = False
    #         while  l >= 0 and r < len(s) and s[l] == s[r]:
    #             l -= 1
    #             r += 1
    #             flag = True
    #         if(i == 1):
    #             print(i,"After odd while ", l, r)
    #         if flag and right - left < r - l:  #######logic issue instead of (right - left < r - 1 + l +1 ), i used wrong logic
    #             left = l + 1
    #             right = r - 1
    #             if(i == 1):
    #                 print(i," Even com l ", left, right)
    #     if left == 0 and right == 0:
    #         return s[0]
    #     return s[left: right+1] 
    #     #return "";
s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
print(s.longestPalindrome("ajithanagram"))
print(s.longestPalindrome("abc"))
print(s.longestPalindrome("ccc"))
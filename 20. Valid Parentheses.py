class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        map = {'(' : ')', '{' : '}', '[' : ']'}
        for i in s:
            if i in map:
                l.append(i)
            else:
                if not l or map[l.pop()] != i:
                    return False
        return True if not l else False
s =Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid('{'))
print(s.isValid("(("))
print(s.isValid("))"))
print(s.isValid("[]"))
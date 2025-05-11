class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        stored = set()
        res = 0
        for r,ch  in enumerate(s):
   
            while ch in stored:
                stored.remove(s[l])
                l += 1
            stored.add(ch)                
            res = max(res, r - l + 1)
        return res
        
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("tmmzuxt"))
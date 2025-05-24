#time taken to solve: 5 mins
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)
        for i in ransomNote:
            if ransomNote[i] > magazine[i]:
                return False
        return True
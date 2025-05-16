from typing import List
from collections import defaultdict
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # l = []
        # map = defaultdict(list)
        # for str in strs:
        #     map[tuple(sorted(Counter(str).items()))].append(str)
        # for item in map.values():
        #     l.append(item)
        # return l
        map = defaultdict(list)
        for str in strs:
            map[tuple(sorted(str))].append(str)
        return [x for x in map.values()]
        
            
           
    def print(self, strs: List[List[str]]):
        for l in strs:
            print('')
            for str in l:
                print(str, end=" ")
            
s = Solution()
s.print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
s.print(s.groupAnagrams([""]))

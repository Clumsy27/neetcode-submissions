from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map=defaultdict(list)
        for word in strs:
            alp=[0]*26
            for ch in word:
                    alp[ord(ch)-ord('a')]+=1

            map[tuple(alp)].append(word)
        return list(map.values())
        


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map={}
        for i in range(len(nums)):
            more_needed=target-nums[i]
            if more_needed in map:
                return [map[more_needed],i]
            
            map[nums[i]]=i
        
        return [-1,-1]
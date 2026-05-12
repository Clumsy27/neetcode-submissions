class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=1
        suf=1
        prefix=[]
        suffix=[]
        res=[]
        for i in range(len(nums)):
            prefix.append(pre)
            pre*=nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            suffix.append(suf)
            suf*=nums[i]
        suffix.reverse()
        for i in range(len(nums)):
            res.append(prefix[i]*suffix[i])
        return res
        


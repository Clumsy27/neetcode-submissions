class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        map={}
        for i in range (len(nums)):
            map[i]=nums[i]
        arr=[]
        key=0
        for i in range (len(nums)):
            product=1
            for j in range(len(nums)):
                if j==i:
                    continue
                else:
                    product=product*nums[j]
            arr.append(product)
        return arr



            
        
        
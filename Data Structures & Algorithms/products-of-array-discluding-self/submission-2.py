class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            prefix=1
            arr=[]
            for i in range(len(nums)):
                arr.append(prefix)
                prefix*=nums[i]
            postfix=1
            print(arr)
            for i in range(len(nums)-1,-1,-1):
                arr[i]*=postfix
                postfix*=nums[i]
            return arr

            
        
        
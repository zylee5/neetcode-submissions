class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefixProd = 1
        for i in range(0, len(nums)):
            result[i] *= prefixProd
            prefixProd *= nums[i]
        
        suffixProd = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= suffixProd
            suffixProd *= nums[i]

        return result

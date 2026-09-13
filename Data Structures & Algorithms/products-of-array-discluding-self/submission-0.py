class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        non_zero_product = 1

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                non_zero_product *= num
        
        result = []

        for num in nums:
            if zero_count > 1:
                # more than one zeros, everywhere is zero
                result.append(0)
            elif zero_count == 1:
                if num == 0:
                    # exactly one zero and this is the zero
                    result.append(non_zero_product)
                else:
                    result.append(0)
            else:
                result.append(non_zero_product // num)
        
        return result
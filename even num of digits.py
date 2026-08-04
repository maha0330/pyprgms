class Solution:
    def findNumbers(self, nums):
        count = 0

        for num in nums:
            digits = len(str(num))

            if digits % 2 == 0:
                count += 1

        return count


# Example
nums = [12, 345, 2, 6, 7896]

obj = Solution()
print(obj.findNumbers(nums))
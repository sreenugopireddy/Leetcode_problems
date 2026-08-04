class Solution:
    def findMissingElements(self, nums):

        nums.sort()

        answer = []

        for i in range(len(nums)-1):

            current = nums[i]
            next_num = nums[i+1]

            while next_num - current > 1:
                current += 1
                answer.append(current)

        return answer
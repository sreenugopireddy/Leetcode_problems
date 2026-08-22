class Solution:
    def topKFrequent(self, nums, k):
        
        
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        buckets = []

        for i in range(len(nums) + 1):
            buckets.append([])

        for num in frequency:
            count = frequency[num]
            buckets[count].append(num)

        answer = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                answer.append(num)

                if len(answer) == k:
                    return answer
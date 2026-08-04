class Solution:
    def topKFrequent(self, nums, k):
        
        # Step 1: Count the frequency of each number
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # Step 2: Create buckets
        # bucket[i] will store all numbers that appear i times
        buckets = []

        for i in range(len(nums) + 1):
            buckets.append([])

        # Step 3: Put each number into its correct bucket
        for num in frequency:
            count = frequency[num]
            buckets[count].append(num)

        # Step 4: Collect the top k frequent numbers
        answer = []

        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                answer.append(num)

                if len(answer) == k:
                    return answer
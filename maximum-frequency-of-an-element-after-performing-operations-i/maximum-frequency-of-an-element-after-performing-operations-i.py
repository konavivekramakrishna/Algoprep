class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        nums.sort()

        freqMap = defaultdict(int)
        minVal = float('inf')
        maxVal = -1

        for num in nums:
            freqMap[num] += 1
            minVal = min(minVal, num)
            maxVal = max(maxVal, num)


 
        maxFreq = 0
        n = len(nums)

        for num in range(minVal, maxVal + 1):



            leftMost = bisect.bisect_left(nums, num - k)
            rightMost = bisect.bisect_left(nums, num + k + 1) - 1

            currLenOfSameNum = freqMap[num]
            totalLen = rightMost - leftMost + 1

            toChange = max(0, totalLen - currLenOfSameNum)
            toChange = min(toChange, numOperations)

            maxFreq = max(maxFreq, currLenOfSameNum + toChange)
 
            
    
        return maxFreq


        
"""

Approch
This kind of problems which require cnt of less than or greater than with some sorting techinuq

involves
1. N ^ 2
2. BST
3. BIT
4. Merge Sort

if overall simple cnt variable is enough
since we requrie for each element and also while sorting order changes
we have to maintain indexArr

TC : O(2nlogn)
SC : O(n)


"""


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [0] * n

        indexArr = list(range(n))

        self.mergeSort(nums, 0, n-1, ans, indexArr)
        return ans
    
    def mergeSort(self, nums, low, high, ans, indexArr):
        if low >= high:
            return

        mid = (low + high) >> 1
        self.mergeSort(nums, low, mid, ans, indexArr)
        self.mergeSort(nums, mid+1, high, ans, indexArr)
        self.merge(nums, low, mid, high, ans, indexArr)

    def merge(self, nums, low, mid, high, ans, indexArr):

        i = low
        j = mid + 1
        temp = []
        rightCnt = 0
        # the above represents the numbers of elements in the right side which are less than value

        while i <= mid and j <= high:
            if nums[indexArr[i]] > nums[indexArr[j]]:
                temp.append(indexArr[j])
                rightCnt += 1
                j += 1
            else:
                ans[indexArr[i]] += rightCnt
                temp.append(indexArr[i])
                i += 1
        
        while i <= mid:
            temp.append(indexArr[i])
            ans[indexArr[i]] += rightCnt
            i += 1
        while j <= high:
            temp.append(indexArr[j])
            j += 1
        
        for i in range(len(temp)):
            indexArr[low + i] = temp[i]


                

        
        
        




    


        
        
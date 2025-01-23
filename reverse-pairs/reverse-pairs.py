class Solution:
    def reversePairs(self, nums: List[int]) -> int:

        return self.mergeSort(nums, 0, len(nums)-1)

        # Merge
    
    def mergeSort(self, arr, low, high):

        if low < high:
            mid = (low + high) >> 1

            cnt = 0

            cnt += self.mergeSort(arr, low, mid)
            cnt += self.mergeSort(arr, mid+1, high)

            cnt += self.merge(arr, low, mid, high)

            return cnt
        else:
            return 0
    
    def merge(self, arr, low, mid, high):
        ans = 0
        right = mid + 1
        for left in range(low, mid + 1):
            while right <= high and arr[left] > 2 * arr[right]:
                right += 1
            ans += (right - mid - 1)
    
        # Merging process
        temp = []
        i, j = low, mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                temp.append(arr[i])
                i += 1
            else:
                temp.append(arr[j])
                j += 1
        
        while i <= mid:
            temp.append(arr[i])
            i += 1
        
        while j <= high:
            temp.append(arr[j])
            j += 1
        
        # Place sorted elements back into the original array
        for i in range(len(temp)):
            arr[low + i] = temp[i]
    
        return ans
    
    
    
    
    
    
        
    
            
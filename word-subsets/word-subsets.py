class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        freq2 = [0] * 26

        for word in words2:

            currFreq = [0] * 26
            for char in word:

                index = ord(char) - ord('a')
                currFreq[index] += 1
            
            for i in range(26):
                freq2[i] = max(freq2[i], currFreq[i])
        
        ans = []

        for word in words1:

            currFreq = [0] * 26

            for char in word:
                index = ord(char) - ord('a')
                currFreq[index] += 1

            isValid = True
            for i in range(26):
                if currFreq[i] < freq2[i]:
                    isValid = False
                    break
            
            if isValid:
                ans.append(word)
        
        return ans



        
        
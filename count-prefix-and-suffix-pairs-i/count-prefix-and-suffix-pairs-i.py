class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        #words.sort(key = lambda x:(len(x)))
        n = len(words)
        ans = 0

        for i in range(n):
            for j in range(i+1, n):

                if self.isPrefixAndSuffix(words[i], words[j]):
                    ans += 1
        
        return ans

    def isPrefixAndSuffix(self, str1, str2):

        n = len(str1)

        if len(str2) < n:
            return False

        print(str1)
        print(str2)

        print(str2[:n])
        print(str2[-n:])
        
        cond1 = str1 == str2[:n]
        cond2 = str1 == str2[-n:]

        if cond1 and cond2:
            return True
        return False
        

        

        
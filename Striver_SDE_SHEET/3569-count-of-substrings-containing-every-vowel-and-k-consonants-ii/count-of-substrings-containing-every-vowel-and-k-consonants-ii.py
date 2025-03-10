class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        n = len(word)
        checkset = {'a','e','i','o','u'}
        def countsub(k):
            vowel,consonants,l,count = {},0,0,0
            for r in range(n):
                if word[r] in checkset: vowel[word[r]] = vowel.get(word[r],0)+1
                else: consonants+=1
                while len(vowel)==5 and consonants>=k:
                    count+= n-r
                    if word[l] in checkset:vowel[word[l]]-=1
                    else: consonants-=1
                    if word[l] in checkset and vowel[word[l]]==0: vowel.pop(word[l])
                    l+=1
            return count

        return countsub(k)-countsub(k+1)
                


            


            
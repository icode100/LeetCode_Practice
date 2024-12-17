class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int,version1.split(".")))
        version2 = list(map(int,version2.split(".")))
        sum1,sum2 = sum(version1),sum(version2)
        i,j = 0,0
        while i<len(version1) and j<len(version2):
            if version1[i]<version2[j]:
                return -1
            elif version1[i]>version2[j]:
                return 1
            i+=1
            j+=1
        while i<len(version1):
            if version1[i]!=0: return 1
            i+=1
        while j<len(version2):
            if version2[j]!=0: return -1
            j+=1
        return 0
            

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        startswith = defaultdict(list)
        endswith = defaultdict(list)

        for word in words:
            startswith[word[0]].append(word)
            endswith[word[1]].append(word)
        
        ans = list()
        for top in words:
            for left in words:
                if top!=left and top[0]==left[0]:
                    for right in words:
                        if right!=top and right!=left and right[0]==top[-1]:
                            for bottom in words:
                                if bottom!=left and bottom!=top and bottom!=right and bottom[0]==left[-1] and bottom[-1]==right[-1]:
                                    ans.append([top,left,right,bottom])
        return sorted(ans)



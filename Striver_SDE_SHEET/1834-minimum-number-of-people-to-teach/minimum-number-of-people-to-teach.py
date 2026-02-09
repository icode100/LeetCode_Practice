class Solution:
    def minimumTeachings(
        self, n: int, languages: List[List[int]], friendships: List[List[int]]
    ) -> int:
        '''

        * first check among all the frnds who can't comm
        * for the frnds who can't comm check which all langs they lack and maintain a map for each of the persons involved in frndship 
        * run an independent loop over the langs to find which 
        '''

        languages_new = [set(item) for item in languages]
        languages[::] = languages_new
        potenz = set()

        for u,v in friendships:
            if len(languages[u-1] & languages[v-1])==0:
                potenz.add((u,v))
        ans = len(languages)
        for l in range(1,n+1):
            count = 0
            newlang = defaultdict(set)
            for u,v in potenz:
                if l not in languages[u-1] and l not in newlang[u]:
                    newlang[u].add(l)
                    count+=1
                if l not in languages[v-1] and l not in newlang[v]:
                    newlang[v].add(l)
                    count+=1
            ans = min(count,ans)
        return ans


        


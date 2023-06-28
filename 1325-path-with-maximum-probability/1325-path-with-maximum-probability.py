from heapq import heappush,heappop
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        ed,suc,s,e=edges,succProb,start,end
        d=defaultdict(list)
        for (a,b),prob in zip(ed,suc):
            d[a].append((b,prob))
            d[b].append((a,prob))
        heap=[(-1,s)]
        seen=set()
        while heap:
            prob,cur=heappop(heap)
            seen.add(cur)
            if cur==end:
                return -prob
            for neigh,p in d[cur]:
                if not neigh in seen:
                    new_prob=-1*abs(prob*p)
                    heappush(heap,(new_prob,neigh))
        return 0
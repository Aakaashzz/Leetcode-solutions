class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [dst / sp for dst, sp in zip(dist, speed)]
        time.sort()
        
        for index, t in enumerate(time):
            if t <= index:
                return index

        return len(time)
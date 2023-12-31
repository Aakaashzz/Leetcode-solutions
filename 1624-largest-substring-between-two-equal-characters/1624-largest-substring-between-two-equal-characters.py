class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        return max([s.rfind(x)-s.find(x) for x in set(s)])-1
        
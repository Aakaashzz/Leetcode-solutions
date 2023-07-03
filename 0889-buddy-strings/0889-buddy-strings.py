class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        different_letters = [
            (i, a, b)
            for i, (a, b) in enumerate(zip(s, goal))
            if a != b
        ]

        if len(different_letters) != 2:
            # If two strings are the same, then we just need to swap duplicates
            return not different_letters and len(set(s)) < len(s)

        (_, a1, b1), (_, a2, b2) = different_letters
        return a1 == b2 and b1 == a2
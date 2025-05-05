import math

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)

        # helper function to check rotations for a given target value
        def check(target):
            rotations_top = 0
            rotations_bottom = 0
            for i in range(n):
                if tops[i] != target and bottoms[i] != target:
                    # Target value not present on this domino, impossible
                    return math.inf
                elif tops[i] != target:
                    # Must rotate to make top target
                    rotations_top += 1
                elif bottoms[i] != target:
                    rotations_bottom +=1
            return min(rotations_top, rotations_bottom)

        rotations = check(tops[0])

        if tops[0] != bottoms[0]:
            rotations = min(rotations, check(bottoms[0]))
        return rotations if rotations != math.inf else -1

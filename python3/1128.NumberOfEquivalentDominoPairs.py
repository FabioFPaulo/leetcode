class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = collections.defaultdict(int)
        num_pairs = 0

        for domino in dominoes:
            val1 = domino[0]
            val2 = domino[1]

            canonical_key = tuple(sorted((val1, val2)))

            num_pairs += counts[canonical_key]

            counts[canonical_key] +=1

        return num_pairs
                
            
        

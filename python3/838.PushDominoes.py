class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        forces = [0] * N

        # calculate rightward forces (from nearest 'R' to the left)
        force = 0
        for i in range(N):
            if dominoes[i] == 'R':
                force = N
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] += force # Add rightward force

        # calculate leftward forces (from nearest 'L' to the right)
        force = 0
        for i in range(N -1, -1, -1): # iterate backwards
            if dominoes[i] == 'L':
                force = N
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(0, force - 1)
            forces[i] -= force # Add rightward force

        # deretmine final state based on net force
        result = []

        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else: # f == 0
                result.append('.')
        return "".join(result)

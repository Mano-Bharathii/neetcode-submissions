from math import ceil

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_spd = list(zip(position, speed))
        pos_spd.sort(reverse = True)

        for p, s in pos_spd:
            if stack and stack[-1] >= (target - p) / s:
                continue
            stack.append((target - p) / s)
        
        return len(stack)
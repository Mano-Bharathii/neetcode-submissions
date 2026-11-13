from math import ceil

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_spd = [(position[i], speed[i]) for i in range(len(speed))]
        pos_spd.sort(reverse = True)
        # print(pos_idx)

        for p, s in pos_spd:
            print((target - p) / s, stack)
            if stack and stack[-1] >= (target - p) / s:
                continue
            stack.append((target - p) / s)
        
        return len(stack)




        return 1
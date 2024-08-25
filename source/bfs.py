from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        queue = [0]
        visited = set()
        jumps = 0
        length = len(nums)
        result = False
        while not result:
            next_queue = []
            for el in queue:
                if el not in visited:
                    visited.add(el)
                    if el == length - 1:
                        result = True
                    for index in range(el, el + nums[el] + 1):
                        if index not in visited and index < length:
                            next_queue.append(index)
            if not result:
                jumps += 1
            queue = next_queue
        return jumps

from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        current_pos = 0
        jump_count = 0
        right_index = len(nums) - 1
        while current_pos < right_index:
            jump_distance = nums[current_pos]
            next_pos = current_pos
            righest_index = min(next_pos + nums[next_pos], right_index)
            for distance in range(1, jump_distance + 1):
                index = current_pos + distance
                if index <= right_index:
                    next_right_index = min(index + nums[index], right_index)
                    if  next_right_index >= righest_index:
                        next_pos = index
                        righest_index =  next_right_index
            current_pos = next_pos
            jump_count += 1
        return jump_count

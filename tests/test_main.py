from unittest import TestCase

from main import Solution


class TestSolution(TestCase):
    def test_jump_1(self):
        jumps = [2, 3, 1, 1, 4]
        expected = 2
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

    def test_jump_2(self):
        jumps = [4, 0, 1, 0, 2]
        expected = 1
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

    def test_jump_3(self):
        jumps = [3, 5, 2, 0, 0, 0, 2]
        expected = 2
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

    def test_jump_4(self):
        jumps = [4, 0, 5, 0, 1, 0, 0, 4]
        expected = 2
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

    def test_jump_5(self):
        jumps = [10, 0, 3]
        expected = 1
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

    def test_jump_6(self):
        jumps = [2, 0, 0]
        expected = 1
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

    def test_jump_7(self):
        jumps = [10, 1, 1, 1, 1, 1, 1, 0, 1]
        expected = 1
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

    def test_jump_8(self):
        jumps = [2, 3, 1, 1, 4]
        expected = 2
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

    def test_jump_9(self):
        jumps = [2, 3, 0, 1, 4]
        expected = 2
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

    def test_jump_10(self):
        jumps = [0]
        expected = 0
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

    def test_jump_11(self):
        jumps = [7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3]
        expected = 2
        result = Solution().jump(jumps)
        self.assertEqual(expected, result)

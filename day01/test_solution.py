import unittest

from day01.solution import part1, part2
from test.test_parent import ParentTestCase, read_text_file


class DayTestCase(ParentTestCase):
    sample1 = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

    puzzle_input = read_text_file(__file__, "input.txt")

    test_cases_part1 = (
        ("sample 1", sample1, 3),
        ("puzzle input", puzzle_input, 1120),
    )
    test_cases_part2 = (
        ("sample 1", sample1, 6),
        ("puzzle input", puzzle_input, 6554),
    )

    def test_part1(self):
        self.run_tests_for_part(part1, self.test_cases_part1)

    def test_part2(self):
        self.run_tests_for_part(part2, self.test_cases_part2)


if __name__ == "__main__":
    unittest.main()

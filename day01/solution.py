import itertools
from typing import Tuple


def part1(input_data: str) -> int:
    rotations = [to_int(line) for line in input_data.splitlines()]

    rotations.insert(0, 50)
    positions = itertools.accumulate(rotations)
    answer = sum(1 for position in positions if position % 100 == 0)

    return answer


def part2(input_data: str) -> int:
    rotations = [to_int(line) for line in input_data.splitlines()]

    rotations.insert(0, 50)
    # a little optimization: dividing just once
    positions = [(x, x // 100, x % 100 == 0) for x in itertools.accumulate(rotations)]
    answer = sum(get_n_zero_pointings(a, b) for a, b in itertools.pairwise(positions))

    return answer


def get_n_zero_pointings(a: Tuple[int, int, bool], b: Tuple[int, int, bool]) -> int:
    a_position, a_hundreds, is_a_zero = a
    b_position, b_hundreds, is_b_zero = b
    is_turning_left = a_position > b_position
    n_full_circles = abs(b_hundreds - a_hundreds)
    correction = 1 if is_b_zero and is_turning_left else (-1 if is_a_zero and is_turning_left else 0)
    return n_full_circles + correction


def to_int(line: str) -> int:
    value = int(line[1:])
    return value if line[0] == 'R' else -value

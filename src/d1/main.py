from typing import Final
from pathlib import Path
import math

# DATA_FILE: Final = Path("src/d1/c1/sample.txt")
# DATA_FILE: Final = Path("src/d1/c1/test.txt")
# DATA_FILE: Final = Path("src/d1/c2/sample.txt")
DATA_FILE: Final = Path("src/d1/c2/test.txt")


def main():
    with DATA_FILE.open() as f:
        first_list = []
        second_list = []
        for line in f.readlines():
            f, s = parse_line(line)
            first_list.append(f)
            second_list.append(s)
    print(first_list)
    print(second_list)
    first_list.sort()
    second_list.sort()

    # res = sum_diffs(first_list, second_list)
    res = sum_multiply_count(first_list, second_list)
    print(f"Result: {res=}")


def parse_line(line: str) -> tuple[int, int]:
    x, y = line.split("   ")
    return int(x), int(y)


# Part 1
def sum_diffs(first: list[int], second: list[int]) -> int:
    return sum([abs(f - s) for f, s in zip(first, second)])


# Part 2
def sum_multiply_count(first: list[int], second: list[int]) -> int:
    return sum([f * second.count(f) for f in first])


if __name__ == "__main__":
    main()

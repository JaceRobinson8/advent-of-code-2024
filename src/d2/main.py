from pathlib import Path
from dataclasses import dataclass
from itertools import pairwise


@dataclass(frozen=True)
class Report:
    levels: list[int]

    @staticmethod
    def unsafe_condition(x0: int, x1: int, is_increasing: bool) -> bool:
        if is_increasing:
            cond1 = x0 >= x1
        else:
            cond1 = x0 <= x1
        cond2 = abs(x1 - x0) < 1  # less than 1
        cond3 = abs(x1 - x0) > 3  # greater than 3
        return cond1 or cond2 or cond3

    def is_safe(self) -> bool:
        safe = True  # assume safe until condition violated
        is_increasing = (
            self.levels[0] < self.levels[1]
        )  # determine if increasing or decreasing

        for x0, x1 in pairwise(self.levels):
            if self.unsafe_condition(x0, x1, is_increasing):
                safe = False
                break

        return safe


def parse_line(line: str) -> list[int]:
    return [int(num) for num in line.strip().split(" ")]


def parse_data(data_file: Path) -> list[Report]:
    with data_file.open() as f:
        reports = [Report(parse_line(line)) for line in f.readlines()]
    return reports


def main1(data_file: Path):
    reports = parse_data(data_file)
    res = sum([report.is_safe() for report in reports])
    print(f"Result: {res=}")


def main2(data_file: Path):
    reports = parse_data(data_file)
    res = sum([report.is_safe() for report in reports])
    print(f"Result: {res=}")


if __name__ == "__main__":
    # main1(Path("src/d2/c1/sample.txt"))
    # main1(Path("src/d2/c1/test.txt"))
    main2(Path("src/d2/c2/sample.txt"))
    # main2(Path("src/d2/c2/test.txt"))

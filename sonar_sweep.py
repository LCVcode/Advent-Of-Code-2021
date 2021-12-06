from typing import Callable

# Day 1


def _extract_depth_list(depths: str) -> tuple[int, ...]:
    return tuple(int(depth) for depth in depths.split("\n"))


def count_depth_increase(depth_list: tuple[int, ...]) -> int:
    count = 0
    for i in range(len(depth_list) - 1):
        if depth_list[i] < depth_list[i + 1]:
            count += 1
    return count


def sliding_window(depth_list: tuple[int, ...]) -> tuple[int, ...]:
    indices = range(len(depth_list) - 2)
    return tuple(sum(depth_list[i: i + 3]) for i in indices)


def day_1_part_1(depths: str) -> int:
    return count_depth_increase(_extract_depth_list(depths))


def day_1_part_2(depths: str) -> int:
    depth_list = _extract_depth_list(depths)
    sliding_depth_list = sliding_window(depth_list)
    return count_depth_increase(sliding_depth_list)


# Day 2


class Course:

    depth: int
    distance: int
    _direction_function_map: dict[str: Callable]

    def __init__(self):
        self.depth, self.distance = 0, 0
        self._direction_function_map = {
            "forward": self._forward,
            "up": self._up,
            "down": self._down
        }

    def _forward(self, x: int) -> None:
        self.distance += x

    def _up(self, x: int) -> None:
        self.depth -= x

    def _down(self, x: int) -> None:
        self.depth += x

    def add_step(self, step: str) -> None:
        direction, distance = step.split(" ")
        magnitude = int(distance)
        # noinspection PyArgumentList
        self._direction_function_map.get(direction)(int(magnitude))


def day_2_part_1() -> int:
    with open("inputs/day2") as f:
        steps = tuple(f.read().split("\n"))
    course = Course()
    for step in steps:
        course.add_step(step)
    return course.depth * course.distance


class AdvancedCourse(Course):

    aim: int

    def __init__(self):
        super().__init__()
        self.aim = 0

    def _forward(self, x: int) -> None:
        self.distance += x
        self.depth += x * self.aim

    def _up(self, x: int) -> None:
        self.aim -= x

    def _down(self, x: int) -> None:
        self.aim += x


def day_2_part_2() -> int:
    with open("inputs/day2") as f:
        steps = tuple(f.read().split("\n"))
    course = AdvancedCourse()
    for step in steps:
        course.add_step(step)
    return course.depth * course.distance

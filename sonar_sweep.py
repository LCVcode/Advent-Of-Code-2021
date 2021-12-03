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
    return tuple(sum(depth_list[i : i + 3]) for i in indices)


def day_1_part_1(depths: str) -> int:
    return count_depth_increase(_extract_depth_list(depths))


def day_1_part_2(depths: str) -> int:
    depth_list = _extract_depth_list(depths)
    sliding_depth_list = sliding_window(depth_list)
    return count_depth_increase(sliding_depth_list)

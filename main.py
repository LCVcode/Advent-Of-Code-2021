from sonar_sweep import day_1_part_1, day_1_part_2, day_2_part_1, day_2_part_2


if __name__ == "__main__":
    print("=== Day 1 ===")
    with open("inputs/day1") as f:
        puzzle_input = f.read()
    print(day_1_part_1(puzzle_input))
    print(day_1_part_2(puzzle_input))

    print("=== Day 2 ===")
    print(day_2_part_1())
    print(day_2_part_2())

"""
Tests for astar_grid.py

Run with:
    pytest 01_Informed_Search_A_Star/starter_code/test_astar_grid.py -v

`test_given_example` below is COMPLETE -- study it as a template.

You must then write the 3 required test cases (test_case_1, test_case_2,
test_case_3). Read ../../03_Test_Case_Design/mindmap.md and
training_guide.md before choosing what your 3 cases should cover. Aim to
pick 3 *different* categories (e.g. one typical/normal case, one
edge/boundary case, one unsolvable-or-stress case) rather than 3 variations
of the same thing.

For each test case, write a short comment explaining WHICH category from
the mind-map it represents and WHY you chose it.
"""
import pytest
from astar_grid import astar, find_cell, heuristic


def test_case_1():
    """Test Case 1: Unreachable Goal (Blocked by Walls).

    Verifies that the algorithm correctly identifies when no valid path exists
    and returns (None, float('inf')).
    """
    grid = [
        "S...#...",
        "....#...",
        "#####...",
        "....#G..",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is None, "Path should be None when goal is completely blocked"
    assert cost == float(
        "inf"
    ), "Cost should be float('inf') when goal is unreachable"


def test_case_2():
    """Test Case 2: Open Grid / Direct Path.

    Verifies path reconstruction accuracy and total cost on a simple open grid
    without obstacles.
    """
    grid = [
        "S...",
        "....",
        "....",
        "...G",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    expected_cost = 6

    assert path is not None, "Path should be found on an open grid"
    assert cost == expected_cost, f"Expected cost {expected_cost}, got {cost}"
    assert path[0] == start, "Path must start at the start cell"
    assert path[-1] == goal, "Path must end at the goal cell"
    assert (
        len(path) == expected_cost + 1
    ), "Path length should equal cost + 1 (nodes count)"


def test_case_3():
    """Test Case 3: Maze Traversal & Heuristic Function Accuracy.

    Tests pathfinding around wall barriers and verifies that heuristic()
    correctly calculates Manhattan distance.
    """
    assert heuristic((0, 0), (3, 3)) == 6
    assert heuristic((1, 4), (5, 2)) == 6

    grid = [
        "S#...",
        ".#.#.",
        ".#.#.",
        "...#G",
    ]
    start = find_cell(grid, "S")
    goal = find_cell(grid, "G")

    path, cost = astar(grid, start, goal)

    assert path is not None, "Path should be found around walls"
    assert (
        cost == 13
    ), f"Expected optimal path cost of 13 around maze, got {cost}"
    assert path[0] == start
    assert path[-1] == goal

    for i in range(len(path) - 1):
        r1, c1 = path[i]
        r2, c2 = path[i + 1]
        assert grid[r1][c1] != "#", f"Path includes a wall cell at {(r1, c1)}"
        step_dist = abs(r1 - r2) + abs(c1 - c2)
        assert (
            step_dist == 1
        ), f"Invalid non-adjacent step from {path[i]} to {path[i+1]}"
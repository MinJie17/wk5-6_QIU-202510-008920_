import pytest
from csp_map_coloring import backtracking_search, is_consistent


def _is_valid_solution(solution, variables, neighbours):
    """Helper: check a solution assigns every variable and breaks no
    adjacency constraint.
    """
    if solution is None:
        return False
    if set(solution.keys()) != set(variables):
        return False
    for var, value in solution.items():
        for neighbour in neighbours[var]:
            if neighbour in solution and solution[neighbour] == value:
                return False
    return True


# ---------------------------------------------------------------------
# GIVEN EXAMPLE -- complete, do not modify.
# Category: Typical / Solvable Case
# ---------------------------------------------------------------------
def test_given_example():
    from csp_map_coloring import VARIABLES, NEIGHBOURS, DOMAIN

    solution = backtracking_search(VARIABLES, DOMAIN)

    assert solution is not None
    assert _is_valid_solution(solution, VARIABLES, NEIGHBOURS)


# ---------------------------------------------------------------------
# Test Case 1
# Category: Boundary / Edge Case
# Purpose: Check that is_consistent() returns True when there are
# no assigned neighbours yet.
# ---------------------------------------------------------------------
def test_case_1():
    assignment = {}

    assert is_consistent(assignment, "WA", "Red") is True


# ---------------------------------------------------------------------
# Test Case 2
# Category: Invalid / Constraint Violation
# Purpose: A neighbouring region already has the same colour, so
# is_consistent() should reject it.
# ---------------------------------------------------------------------
def test_case_2():
    assignment = {
        "NT": "Red"
    }

    assert is_consistent(assignment, "WA", "Red") is False


# ---------------------------------------------------------------------
# Test Case 3
# Category: Over-constrained / Unsolvable Case
# Purpose: Only one colour is available, so Australia cannot be
# coloured without conflicts.
# ---------------------------------------------------------------------
def test_case_3():
    from csp_map_coloring import VARIABLES

    domain = ["Red"]

    solution = backtracking_search(VARIABLES, domain)

    assert solution is None


if __name__ == "__main__":
    import sys
    sys.exit(pytest.main([__file__, "-v"]))
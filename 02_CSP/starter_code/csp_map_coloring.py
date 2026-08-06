"""
Assignment starter: backtracking CSP solver for map colouring.

Read ../guide.md and ../worked_example.md BEFORE you start coding here.

Your job: fill in every function marked TODO. Do not change function
signatures (the tests in test_csp_map_coloring.py rely on them).

The problem: colour a map of Australia's 7 regions so that no two adjacent
regions share a colour, using only 3 colours.
"""

VARIABLES = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]

# Adjacency list: which regions border which. T (Tasmania) is an island --
# it has no neighbours, so it's unconstrained.
NEIGHBOURS = {
    "WA":  ["NT", "SA"],
    "NT":  ["WA", "SA", "Q"],
    "SA":  ["WA", "NT", "Q", "NSW", "V"],
    "Q":   ["NT", "SA", "NSW"],
    "NSW": ["SA", "Q", "V"],
    "V":   ["SA", "NSW"],
    "T":   [],
}

DOMAIN = ["Red", "Green", "Blue"]


def is_consistent(assignment, var, value):
    """Return True if assigning value to var does not conflict with
    already-assigned neighbours.
    """
    for neighbour in NEIGHBOURS[var]:
        if neighbour in assignment and assignment[neighbour] == value:
            return False
    return True


def select_unassigned_variable(assignment):
    """Return the first variable that has not been assigned."""
    for var in VARIABLES:
        if var not in assignment:
            return var
    return None


def backtracking_search(variables, domain):
    """Run backtracking search."""

    def backtrack(assignment):
        # 1. If assignment is complete, return it
        if len(assignment) == len(variables):
            return assignment

        # 2. Select an unassigned variable
        var = select_unassigned_variable(assignment)

        # 3. Try each value
        for value in domain:

            # 4. Check consistency
            if is_consistent(assignment, var, value):

                # Tentatively assign
                assignment[var] = value

                # Recurse
                result = backtrack(assignment)

                # Success
                if result is not None:
                    return result

                # Backtrack
                del assignment[var]

        # Failure
        return None

    return backtrack({})


if __name__ == "__main__":
    solution = backtracking_search(VARIABLES, DOMAIN)
    if solution:
        print("Solution found:")
        for region in VARIABLES:
            print(f"  {region}: {solution[region]}")
    else:
        print("No solution exists with this domain.")
import unittest
import numpy as np
from csp import CSP

# TODO: change all values, find a certain problem with solutions and test it
# this is simply copied from the given tests, so needed to be altered a lot.
def test_search_ben(self):
    groups = [[(0, 0), (1, 0)], [(2, 0), (0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
    constraints = [(2, 2), (4, 4), (3, 3)]

    start_grid = np.array([[0, 1, 1],
                           [0, 1, 1],
                           [1, 0, 0]])
    csp = CSP(start_grid, numbers=set([1, 2, 3]), groups=groups, constraints=constraints)
    result = csp.start_search()
    solution_grid = np.array([
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ])
    self.assertTrue(np.all(result == solution_grid))

    # Change the constraints to make it impossible and check again:
    constraints = [(2, 1), (4, 2), (3, 1)]

    csp = CSP(start_grid, numbers=set([1, 2, 3]), groups=groups, constraints=constraints)
    result = csp.start_search()
    self.assertIsNone(result)

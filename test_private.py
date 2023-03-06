import unittest
import numpy as np
from csp import CSP

# TODO: change all values, find a certain problem with solutions and test it
# this is simply copied from the given tests, so needed to be altered a lot.
def test_search():
        horizontal_groups = [[(0,0),(0,1)], [(1,0), (1,1)]]
        vertical_groups = [[(0,0), (1,0)], [(0,1), (1,1)]]
        groups = horizontal_groups + vertical_groups
        constraints = [(3, 1), (3, 1), (3, 1), (3, 1)]

        valid_grid = np.array([[1,0],
                               [0,0]])
        csp = CSP(valid_grid, numbers=set([1,2]), groups=groups, constraints=constraints)
        result = csp.start_search()

        solution_grid = np.array([[1,2],
                                  [2,1]])

        unittest.TestCase.assertTrue(np.all(solution_grid == result))

        valid_grid = np.array([[2,0],
                               [0,0]])
        csp = CSP(valid_grid, numbers=set([1,2]), groups=groups, constraints=constraints)
        result = csp.start_search()

        solution_grid = np.array([[2,1],
                                  [1,2]])

        unittest.TestCase.assertTrue(np.all(solution_grid == result))

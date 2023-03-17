import unittest
import numpy as np
from csp import CSP

class TestCSP(unittest.TestCase):
    def test_search_easy(self):
        groups = [[(0, 0), (1, 0)], [(2, 0), (0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
        constraints = [(4, 1), (4, 4), (3, 3)]

        start_grid = np.array([[0, 1, 1],
                               [0, 1, 1],
                               [1, 0, 0]])
        csp = CSP(start_grid, numbers={1, 2, 3}, groups=groups, constraints=constraints)
        result = csp.start_search()
        solution_grid = np.array([
            [1, 1, 1],
            [2, 1, 1],
            [1, 1, 1],
        ])
        self.assertTrue(np.all(result == solution_grid))

    def test_search_private_hard(self):
        groups = [[(0, 0), (1, 0)], [(0, 1), (0, 2), (1, 1)], [(2, 0), (2, 1), (2, 2), (1, 2)]]
        constraints = [(3, 2), (15, 1), (20, 2)]

        start_grid = np.array([[1, 0, 0],
                               [0, 3, 0],
                               [0, 0, 6]])

        csp = CSP(start_grid, numbers={2, 3, 4, 5, 6}, groups=groups, constraints=constraints)
        result = csp.start_search()
        solution_grid = np.array([
            [1, 2, 4],
            [2, 3, 2],
            [2, 3, 6]
        ])
        self.assertTrue(np.all(result == solution_grid))

    def test_search_private_false(self):
        groups = [[(0, 0), (1, 0)], [(2, 0), (0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)]]
        constraints = [(2, 2), (4, 2), (3, 1)]

        start_grid = np.array([[0, 1, 1],
                               [0, 1, 1],
                               [1, 0, 0]])
        csp = CSP(start_grid, numbers={1, 2, 3, 4}, groups=groups, constraints=constraints)
        result = csp.start_search()
        self.assertIsNone(result)

##################################################################################
# It is not allowed to add imports here. Use these two packages and nothing else.
import numpy as np
import typing
##################################################################################


class CSP:
    def __init__(self, grid:np.ndarray, numbers: typing.Set[int], groups: typing.List[typing.List[typing.Tuple[int,int]]],
                 constraints: typing.List[typing.Tuple[int,int]]):
        
        """
        The CSP solver object, containing all information and functions required for the assignment. You do not need to change
        this function.

        :param grid: 2-d numpy array corresponding to the grid that we have to fill in. Empty squares are denoted with 0s.
        :param numbers (N): The set of numbers that we are allowed to use in order to fill the grid (can be any set of integers)
        :param groups (M(G)): A list of cell groups (cell groups are lists of location tuples).
        :param constraints (S(G), C(G)): The list of constraints for every group of cells. constraints[i] hold for groups[i]. Every
                            constraint is a tuple of the form (sum_of_elements, max_count_element) where sum_of_elements 
                            indicates what the sum must be of the elements of the given group, and max_count_element indicates
                            the maximum number of times that a number/element may occur in the given group
        """

        self.width = grid.shape[1]
        self.height = grid.shape[0]
        self.numbers = numbers
        self.groups = groups
        self.constraints = constraints

        self.grid = grid
        self.cell_to_groups = {(row_idx, col_idx): [] for row_idx in range(self.height) for col_idx in range(self.width)}


    def fill_cell_to_groups(self):
        """
        Function that fills in the self.cell_to_groups datastructure, which maps a cell location (row_idx, col_idx)
        to a list of groups of which it is a member. For example, suppose that cell (0,0) is member of groups 0, 1,
        and 2. Then, self.cell_to_groups[(0,0)] should be equal to [0,1,2]. This function should do this for every cell. 
        If a cell is not a member of any groups, self.cell_to_groups[cell] should be an empty list []. 
        The function does not return anything. 

        Before completing this function, make sure to read the assignment description and study the data structures created
        in the __init__ function above (self.groups and self.cell_to_groups).
        """

        # loop through dict
            # for key (a, b): loop through groups list and check for each group if it is in it.
                # If in group, add group index to list
            # assign list to dict key

        for key in self.cell_to_groups:
            for i in range(0, len(self.groups)):
                if key in self.groups[i]:
                    self.cell_to_groups[key].append(i)


    def satisfies_sum_constraint(self, group: typing.List[typing.Tuple[int,int]], sum_constraint: int) -> bool:
        """
        Function that checks whether the given group satisfies the given sum constraint (group smaller or equal 
        than sum). Returns True if the current group satisfies the constraint and False otherwise. 

        :param group: The list of locations [loc1, loc2, loc3,...,locN] that specify the group. Here, every loc is 
                      a tuple (row_idx, col_idx) of indices, specifying the row and column of the cell. 
        :param sum_constraint: The sum_of_elements constraint specifying that the numbers in the given group must
                               sum up to this number. This is None if there is no sum constraint for the given group. 
        """

        # loop through group
            # find value of location in grid
            # add up all values
        # compare to sum constraint
        total_value = 0
        for location in group:
            total_value += self.grid[location]
        if total_value > sum_constraint:
            return False
        else:
            return True
    
    def satisfies_count_constraint(self, group: typing.List[typing.Tuple[int,int]], count_constraint: int) -> bool:
        """
        Function that checks whether the given group satisfies the given count constraint.
        Returns True if the current group satisfies the constraint and False otherwise. 
        Recall that the value of 0 indicates an empty cell (0s should not count towards the count constraint).

        :param group: The list of locations [loc1, loc2, loc3,...,locN] that specify the group. Here, every loc is 
                      a tuple (row_idx, col_idx) of indices, specifying the row and column of the cell. 
        :param count_constraint: Integer specifying that a given number cannot occur more than this amount of times. 
                                 This is None if there is no count constraint for the given group. 
        """

        # TODO: write this function
        # Make new list (counts) of group with values instead of locations (find locations in grid)

        counts = []
        for location in group:
            counts.append(self.grid[location])
        # Make list (values) of values in group where they all appear only once, not including 0
        values = list(dict.fromkeys(counts))
        # loop through values:
        for v in values:
            # count how often the value appears in counts
            rep = counts.count(v)
            # check constraint
            if rep > count_constraint:
                return False
        # if loop finishes, then no False was returned, so automatically return True.
        return True

    def satisfies_group_constraints(self, group_indices: typing.List[int]) -> bool:
        """
        Function that checks whether the constraints for the given group indices are satisfied.
        Returns True if all relevant constraints are satisfied, False otherwise. Make sure to use functions defined above. 

        :param group_indices: The indices of the groups for which we check all of the constraints 
        """

        # TODO: write this function
        # loop through group indices: for the relevant group:
        for i in group_indices:
            current_group = self.groups[i]
            sum_constraint, count_constraint = self.constraints[i]
            if not self.satisfies_sum_constraint(current_group, sum_constraint) or not self.satisfies_count_constraint(current_group, count_constraint):
                return False
        return True

    def search(self, empty_locations: typing.List[typing.Tuple[int, int]]) -> np.ndarray:
        """
        Recursive exhaustive search function. It tries to fill in the empty_locations with permissible values
        in an attempt to find a valid solution that does not violate any of the constraints. Instead of checking all
        possible constraints after filling in a number, it checks only the relevant group constraints using the 
        self.cell_to_groups data structure. 

        Returns None if there is no solution. Returns the filled in solution (self.grid) otherwise if a solution is found.

        :param empty_locations: list of empty locations that still need a value from self.numbers 
        """
        # problem with this: time complexity is n^2?

        # loop through the empty locations
        for empty_cell in empty_locations:
            # create a new list of empty locations excluding the one we're checking
            new_locations = empty_locations
            new_locations.remove(empty_cell)
            # if the list of empty location is empty, or the grid is full, check if it's a solution
            if len(new_locations) == 0:
                # TODO add function to check solutions. Return the grid if true, else continue?
            # loop through all possible numbers
            for num in self.numbers:
                # fill in grid with number
                self.grid[empty_cell] = num
                # search the new grid with the new empty locations list
                self.search(self, new_locations)
        return None

    def start_search(self):
        """
        Non-recursive function that starts the recursive search function above. It first fills the cell_to_group
        data structure and computes the empty locations. Then, it starts the recursive search procedure. 
        The result is None if there is no solution possible. Otherwise, it returns the grid that is a solution.

        You do not need to change this function.
        """

        self.fill_cell_to_groups()
        empty_locations = [(row_idx, col_idx) for row_idx in range(self.height) for col_idx in range(self.width) if self.grid[row_idx,col_idx]==0]
        return self.search(empty_locations)
    


class Grid:

    def __init__(self, list_2d):
        self._grid = list_2d

    def filled_out(self):
        """whether or not the uncertened cells' set is empty.
        """
        pass

    def is_solved(self):
        """true if get a fine solution .
        """
        pass

    def row(self, i):
        """return a generator of the specific row.
        """
        pass

    def col(self, j):
        """return a generator of the specific column.
        """
        pass

    def block(self, i):
        """return a generator of the block in the given No.
        """
        pass

    def affected_cells(self, i, j):
        """all cells of row, column, block in which the given cell is based.  
        pass

    def clone(self):
        """return a copy of self's instance.
        """
        pass
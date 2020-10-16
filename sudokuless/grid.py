
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
        pass"""

    def clone(self):
        """return a copy of self's instance.
        """
        pass

class Grid:

    def __init__(self, flatlist=None):
        if flatlist != None:
            self.init(flatlist)

    def init(self, flatlist):
        self.list = list(flatlist)
        self._check()
        self.size = (9,9)

    def _check(self):
        assert self.list
        assert len(self.list) == 81
        assert all(map(lambda x: isinstance(x, int), self.list))
        assert all(map(lambda x: x>=0 and x<=9, self.list))

    def __getitem__(self, key):
        N = 9
        if isinstance(key, tuple):
            assert isinstance(key[0], (int, slice))
            assert isinstance(key[1], (int, slice))
            row = key[0]
            col = key[1]
        else:
            assert isinstance(key, (int, slice))
            row = key
            col = slice(N)
        if isinstance(row, int):
            row *= N
            l = self.list[row:row+N]
            return l[col]
        else:
            ret = []
            for rstart in range(N)[row]:
                rstart *= N
                print(self.list[rstart:rstart+N])
                ret.append(self.list[rstart:rstart+N][col])
            return ret

    def clone(self):
        return self.__class__(self.list.copy())

    def __eq__(self, other):
        return self.list == other.list

    @property
    def is_over(self):
        N = 9
        for xi in range(N):
            tester = [x+1 for x in range(N)]
            for yi in range(N):
                tester[self[xi, yi]-1] = 0
            if sum(tester) != 0:
                return False

        for yi in range(self.size[1]):
            tester = [x+1 for x in range(N)]
            for xi in range(N):
                tester[self[xi, yi]-1] = 0
            if sum(tester) != 0:
                return False

        mapper = [(0,0),(0,3),(0,6),
                  (3,0),(3,3),(0,6),
                  (6,0),(6,3),(6,6),]
        for bi in range(9):
            tester = [x+1 for x in range(9)]
            for xi in range(3):
                for yi in range(3):
                    tester[self[(mapper[bi][0]+xi), (mapper[bi][1]+yi)]-1] = 0
            if sum(tester) != 0:
                return False

        return True
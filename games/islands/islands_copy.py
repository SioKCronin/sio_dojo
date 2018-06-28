from pprint import pprint

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # Convert the grid to a bag of land
        self.lands = set(
            (row, col)
            for row, line in enumerate(grid)
            for col, land in enumerate(line)
            if land == '1'
        )

        pprint(self.lands)

        island_counter = 0
        # Remove islands from the bag one by one
        while self.lands:
            island_seed = next(iter(self.lands))  # pick a random land
            island_counter += 1
            self.remove_island(island_seed)

        return island_counter

    def remove_island(self, coordinates):
        try:
            self.lands.remove(coordinates)
        except KeyError:
            return

        x, y = coordinates
        self.remove_island((x - 1, y))
        self.remove_island((x + 1, y))
        self.remove_island((x, y - 1))
        self.remove_island((x, y + 1))

if __name__ == '__main__':
    from textwrap import dedent
    grid = dedent("""\
        11000
        11000
        00100
        00011""")

    grid = [[c for c in line] for line in grid.split('\n')]
    pprint(grid)
    print Solution().numIslands(grid)


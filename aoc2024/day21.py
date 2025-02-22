from functools import lru_cache

from grid import Grid

def parse_input():
    return ("341A", "083A", "802A", "973A", "780A")

def make_paths(cpt, npt, g):
    # only take L paths if they don't pass through the # in the grid
    if cpt == npt:
        return ['A']

    nx, ny = (abs(npt[0] - cpt[0]), abs(npt[1] - cpt[1]))
    cx = '>' if npt[0] > cpt[0] else '<'
    cy = 'v' if npt[1] > cpt[1] else '^'

    paths = set([cx * nx + cy * ny, cy * ny + cx * nx])
    for path in list(paths):
        pt = cpt
        for dir in path:
            pt, c = g.stepc(pt, dir)
            if c == '#':
                paths.remove(path)
                break

    return [_ + 'A' for _ in paths]

def part(codes):
    # use small grids to generate paths
    ng = Grid(['789', '456', '123', '#0A'])
    dg = Grid(['#^A', '<v>'])

    # generate paths between points on each grid
    paths = {}
    for g in (ng, dg):
        for pt1, c1 in g.iterc():
            if c1 != '#':
                for pt2, c2 in g.iterc():
                    if c2 != '#':
                        paths[(c1, c2)] = make_paths(pt1, pt2, g)

    @lru_cache(maxsize=None)
    def countem(code, times):
        if times == 0:
            return len(code)

        prev = 'A'
        tot = 0
        for c in code:
            tot += min(countem(_, times-1) for _ in paths[(prev, c)])
            prev = c

        return tot

    tot1 = tot2 = 0
    for code in codes:
        num = int(code.lstrip('A0').rstrip('A'))
        dummy = num * countem(code, 3) # for logging out to see intermediate results and find problem
        print(f"{code}: {dummy}")
        tot1 += dummy
        tot2 += num * countem(code, 26)

    print(f"P1: {tot1}")
    print(f"P2: {tot2}")

def main():
    data = parse_input()
    part(data)

if __name__ == '__main__':
    main()
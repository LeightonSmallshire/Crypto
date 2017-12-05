from secrets import randbelow


def DH():
    g = generator = 5
    p = prime = 23

    a_priv = randbelow(p)
    b_priv = randbelow(p)

    a_pub = g.__pow__(a_priv, p)
    b_pub = g.__pow__(b_priv, p)

    a_secret = b_pub.__pow__(a_priv, p)
    b_secret = a_pub.__pow__(b_priv, p)

    print(a_secret == b_secret)


def generic():
    def f(a, b, c):
        return a.__pow__(c, b)

    g = 5
    p = 23

    a_priv = randbelow(p)
    b_priv = randbelow(p)

    a_pub = f(g, p, a_priv)
    b_pub = f(g, p, b_priv)

    a_secret = f(b_pub, p, a_priv)
    b_secret = f(a_pub, p, b_priv)

    print(a_secret == b_secret)


class GameOfLifeBoard:
    def __init__(self, w, h, value, wrap=False):
        self.size = self.w, self.h = w, h
        self._grid = value
        self.wrapping = wrap

    @staticmethod
    def rules(neighbours, alive):
        #   neighbours  return
        #   0,1         0
        #   2           alive?
        #   3           1
        #   4,5,6,7,8   0
        return neighbours == 3 or (alive and neighbours == 2)

    @staticmethod
    def rules_boom(neighbours, alive):
        return neighbours == 3 or neighbours == 2 or (alive and neighbours == 4)

    @staticmethod
    def get_neighbours(grid, width, c):
        count = 0

        w = width
        n = grid

        n >>= (c - w - 1)

        count += n & 1
        n >>= 1
        count += n & 1
        n >>= 1
        count += n & 1

        n >>= w - 2
        count += n & 1
        n >>= 1
        alive = n & 1
        n >>= 1
        count += n & 1

        n >>= w - 2
        count += n & 1
        n >>= 1
        count += n & 1
        n >>= 1
        count += n & 1
        return count, alive

    def step(self, rules=None):
        if rules is None:
            rules = self.rules

        old_grid = self._grid
        old_expanded = 0
        w = self.w
        h = self.h

        row_mask = (1 << w) - 1
        for row in range(h):
            mask = row_mask << (row * w)
            grid_row = old_grid & mask
            row_expanded = grid_row << (row * (w - 2) + 1 + (w + 2))

            old_expanded |= row_expanded

        new_grid = 0
        _w, _h = w + 2, h + 2
        for y in range(h):
            _y = y + 1
            for x in range(w):
                _x = x + 1
                _c = _y * _w + _x
                c = y * w + x

                neighbours, alive = self.get_neighbours(old_expanded, _w, _c)
                new_val = rules(neighbours, alive)

                if new_val:
                    new_grid |= new_val << c

        self._grid = new_grid
        return new_grid

    @staticmethod
    def main():
        # 0 0 0 0   1 2 3 2         0 1 2 3
        # 0 1 1 1   2 2 4 2         4 5 6 7
        # 0 1 0 1   3 4 8 4         8 9 a b
        # 0 1 1 1   2 2 4 2         c d e f
        step0 = (1 << 5) + (1 << 6) + (1 << 7) + (1 << 9) + (1 << 11) + (1 << 13) + (1 << 14) + (1 << 15)

        # 0 0 1 0   1 2 2 2         0 1 2 3
        # 0 1 0 1   2 2 3 1         4 5 6 7
        # 1 0 0 0   2 3 4 2         8 9 a b
        # 0 1 0 1   2 1 2 0         c d e f
        step1 = (1 << 2) + (1 << 5) + (1 << 7) + (1 << 8) + (1 << 13) + (1 << 15)

        # 0 0 1 0   1 3 2 2         0 1 2 3
        # 0 1 1 0   3 4 3 2         4 5 6 7
        # 1 1 0 0   2 3 3 1         8 9 a b
        # 0 0 0 0   2 2 1 0         c d e f
        step2 = (1 << 2) + (1 << 5) + (1 << 6) + (1 << 8) + (1 << 9)

        b = GameOfLifeBoard(4, 4, step0)
        assert b.step() == step1
        assert b.step() == step2


def GOLC():
    def step(board, cfg, steps):
        w, h = cfg
        __board = GameOfLifeBoard(w, h, board)
        for _ in range(steps):
            __board.step(GameOfLifeBoard.rules_boom)
        return __board._grid

    cfg = 32, 32  # 4096 bits
    b = randbelow(cfg[0] * cfg[1])
    key_max = 1024

    a_priv = randbelow(key_max)  # Random priv key matching board size
    b_priv = randbelow(key_max)  # Random priv key matching board size

    a_pub = step(b, cfg, a_priv)
    b_pub = step(b, cfg, b_priv)

    a_secret = step(b_pub, cfg, a_priv)
    b_secret = step(a_pub, cfg, b_priv)
    assert a_secret == b_secret


if __name__ == '__main__':
    for i in range(10):
        GOLC()
        print(f'{i+1} done.')

def get_static_obstacles():
    return {
        (7, 1), (7, 2), (7, 10),
        (6, 2), (6, 6), (6, 10), (6, 11),
        (5, 10),
        (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8), (4, 9),
        (3, 0),
        (2, 0), (2, 3), (2, 4), (2, 5), (2, 6),
        (1, 0), (1, 6), (1, 7), (1, 8), (1, 9),
        (0, 0)
    }

def coord_to_label(pos):
    row, col = pos
    return f"{chr(ord('a') + col)}{row + 1}"

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
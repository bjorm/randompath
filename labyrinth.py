import random
from collections import namedtuple, OrderedDict


class Position2(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return '({}, {})'.format(self.x, self.y)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Position):
            return False

        return o.x == self.x and o.y == self.y

    def __hash__(self) -> int:
        return hash((self.x, self.y))


Position = namedtuple('Position', ['x', 'y', 'direction'])

LEFT = 'LEFT'
DOWN = 'DOWN'
RIGHT = 'RIGHT'
UP = 'UP'

MAX = 7

positions = OrderedDict()


def would_hit_boundary(direction, current_position):
    would_hit_bottom = direction == DOWN and current_position.y == 0
    would_hit_left = direction == LEFT and current_position.x == 0
    would_hit_right = direction == RIGHT and current_position.x == MAX
    would_hit_top = direction == UP and current_position.y == MAX
    return would_hit_right or would_hit_bottom or would_hit_left


def get_next_position(current_position):
    direction = get_next_direction()

    while would_hit_boundary(direction, current_position):
        direction = get_next_direction()

    if direction == UP:
        new_x = current_position.x
        new_y = current_position.y + 1
    elif direction == DOWN:
        new_x = current_position.x
        new_y = current_position.y - 1
    elif direction == LEFT:
        new_x = current_position.x - 1
        new_y = current_position.y
    elif direction == RIGHT:
        new_x = current_position.x + 1
        new_y = current_position.y
    else:
        raise RuntimeError('Unknown direction: {}'.format(direction))

    return Position(new_x, new_y, direction)


def get_next_direction():
    return random.choice([UP, RIGHT, LEFT])


def key(position):
    return position.x, position.y


current_position = Position(random.randint(0, 7), 0, 'START')
positions[key(current_position)] = current_position

while current_position.y != 7:
    next_position = get_next_position(current_position)
    while key(next_position) in positions:
        next_position = get_next_position(current_position)

    positions[key(next_position)] = next_position
    current_position = next_position

board = [[' . ' for _ in range(8)] for _ in range(8)]

for i, key in enumerate(positions):
    position = positions[key]
    board[position.y][position.x] = '{:3}'.format(i)

for line in board:
    print(''.join(line))

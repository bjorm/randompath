import random
from collections import namedtuple, OrderedDict

import logging

Position = namedtuple('Position', ['x', 'y', 'direction'])

LEFT = 'LEFT'
DOWN = 'DOWN'
RIGHT = 'RIGHT'
UP = 'UP'


def would_hit_boundary(direction, current_position, max_size):
    would_hit_bottom = direction == DOWN and current_position.y == 0
    would_hit_left = direction == LEFT and current_position.x == 0
    would_hit_right = direction == RIGHT and current_position.x == max_size
    return would_hit_right or would_hit_bottom or would_hit_left


def is_legal_move(previous_directions, next_direction):
    if len(previous_directions) < 2:
        return True

    if next_direction == UP:
        return True

    if previous_directions[-1] == RIGHT and next_direction == LEFT or \
            previous_directions[-1] == LEFT and next_direction == RIGHT:
        return False

    if next_direction in [RIGHT, LEFT] and previous_directions[-1] == UP and not previous_directions[-2] == UP:
        return False

    return True


def compute_next_position(next_direction, current_position):
    if next_direction == UP:
        new_x = current_position.x
        new_y = current_position.y + 1
    elif next_direction == DOWN:
        new_x = current_position.x
        new_y = current_position.y - 1
    elif next_direction == LEFT:
        new_x = current_position.x - 1
        new_y = current_position.y
    elif next_direction == RIGHT:
        new_x = current_position.x + 1
        new_y = current_position.y
    else:
        raise RuntimeError('Unknown direction: {}'.format(next_direction))

    return Position(new_x, new_y, next_direction)


def get_next_position(current_position, previous_positions, directions, max_size):
    while True:
        next_direction = get_next_direction()
        next_position = compute_next_position(next_direction, current_position)

        is_unique = not key(next_position) in previous_positions
        is_within_boundary = not would_hit_boundary(next_direction, current_position, max_size)
        is_legal = is_legal_move(directions, next_direction)

        if is_within_boundary and is_unique and is_legal:
            break

        logging.debug('Illegal turn %s, retry', next_direction)

    logging.debug('next direction: %s', next_direction)
    directions.append(next_direction)

    return next_position


def get_next_direction():
    return random.choices([UP, RIGHT, LEFT], [0.1, 0.5, 0.5])[0]


def key(position):
    return position.x, position.y


def compute_random_path(board_size):
    directions = []
    positions = OrderedDict()
    max_size = board_size - 1

    current_position = Position(random.randint(0, max_size), 0, 'START')
    positions[key(current_position)] = current_position

    while True:
        next_position = get_next_position(current_position, positions, directions, max_size)
        positions[key(next_position)] = next_position
        current_position = next_position

        if current_position.y == max_size:
            break

    return positions


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--size', help='board size', default=8, type=int)
    parser.add_argument('--debug', help='debug mode', action='store_true')
    args = parser.parse_args()

    board_size = args.size

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    path = compute_random_path(board_size)

    board = [[' . ' for _ in range(board_size)] for _ in range(board_size)]

    for i, key in enumerate(path):
        position = path[key]
        board[position.y][position.x] = '{:^3}'.format(i)

    for line in board:
        print(''.join(line))

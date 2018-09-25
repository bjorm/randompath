import random
import enum
import logging
from collections import namedtuple, OrderedDict

Position = namedtuple('Position', ['x', 'y', 'direction'])


class Direction(enum.Enum):
    UP = 'UP'
    DOWN = 'DOWN'
    RIGHT = 'RIGHT'
    LEFT = 'LEFT'


def _would_hit_boundary(direction, current_position, max_size):
    would_hit_bottom = direction == Direction.DOWN and current_position.y == 0
    would_hit_left = direction == Direction.LEFT and current_position.x == 0
    would_hit_right = direction == Direction.RIGHT and current_position.x == max_size
    return would_hit_right or would_hit_bottom or would_hit_left


def _is_legal_move(previous_directions, next_direction):
    if len(previous_directions) < 2:
        return True

    if next_direction == Direction.UP:
        return True

    if previous_directions[-1] == Direction.RIGHT and next_direction == Direction.LEFT or \
            previous_directions[-1] == Direction.LEFT and next_direction == Direction.RIGHT:
        return False

    if next_direction in [Direction.RIGHT, Direction.LEFT] and \
            previous_directions[-1] == Direction.UP and \
            not previous_directions[-2] == Direction.UP:
        return False

    return True


def _compute_next_position(next_direction, current_position):
    if next_direction == Direction.UP:
        new_x = current_position.x
        new_y = current_position.y + 1
    elif next_direction == Direction.DOWN:
        new_x = current_position.x
        new_y = current_position.y - 1
    elif next_direction == Direction.LEFT:
        new_x = current_position.x - 1
        new_y = current_position.y
    elif next_direction == Direction.RIGHT:
        new_x = current_position.x + 1
        new_y = current_position.y
    else:
        raise RuntimeError('Unknown direction: {}'.format(next_direction))

    return Position(new_x, new_y, next_direction)


def _get_next_position(current_position, previous_positions, directions, max_size):
    while True:
        next_direction = _get_next_direction()
        next_position = _compute_next_position(next_direction, current_position)

        is_unique = not _key(next_position) in previous_positions
        is_within_boundary = not _would_hit_boundary(next_direction, current_position, max_size)
        is_legal = _is_legal_move(directions, next_direction)

        if is_within_boundary and is_unique and is_legal:
            break

        logging.debug('Illegal turn %s, retry', next_direction)

    logging.debug('next direction: %s', next_direction)
    directions.append(next_direction)

    return next_position


def _get_next_direction():
    return random.choices([Direction.UP, Direction.LEFT, Direction.RIGHT], [0.1, 0.5, 0.5])[0]


def _key(position):
    return position.x, position.y


def compute_random_path(board_size):
    directions = []
    positions = OrderedDict()
    max_size = board_size - 1

    current_position = Position(random.randint(0, max_size), 0, 'START')
    positions[_key(current_position)] = current_position

    while True:
        next_position = _get_next_position(current_position, positions, directions, max_size)
        positions[_key(next_position)] = next_position
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

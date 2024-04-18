import random

all_colors = ["red", "blue", "orange", "black"]


def get_color(piece):
    return piece.split(" ")[0]


def get_num(piece):
    return piece.split(" ")[-1]


def split_into_colors(pieces):
    """Returns a list of pieces of the same color grouped in lists."""
    # Molaria bastant més així però no sé si es pot no posar res al else, no deixa continue
    #
    # return [
    #     [piece if get_color(piece) == color else ??? DO NOTHING ??? for piece in pieces]
    #     for color in all_colors
    # ]

    split = [[] for _ in all_colors]
    for index, color in enumerate(all_colors):
        for piece in pieces:
            if get_color(piece) == color:
                split[index].append(piece)

    return split


def is_group(pieces):
    """Returns true if all the pieces have the same number and are different colors, that is, they form a group."""
    are_same_num = all([get_num(piece) == get_num(pieces[0]) for piece in pieces])

    colors = [get_color(piece) for piece in pieces]
    are_different_color = len(colors) <= 4 and all(
        [colors.count(color) < 2 for color in colors]
    )

    return are_same_num and are_different_color


def find_groups(pieces):
    """Returns all possible groups from the list of pieces provided."""
    return None


def is_run(pieces):
    """Returns true if all the pieces are of the same color and their numbers are consecutive, that is, they form a run."""
    are_same_color = all([get_color(piece) == get_color(pieces[0]) for piece in pieces])

    nums = [int(get_num(piece)) for piece in pieces]
    nums.sort()
    are_a_run = len(nums) >= 3 and nums == list(range(nums[0], nums[-1] + 1))

    return are_same_color and are_a_run


def find_runs(pieces):
    """Returns all the possible runs from the list of pieces provided."""
    sorted_pieces = split_into_colors(pieces)
    all_runs = []
    for color in sorted_pieces:
        color.sort(key=lambda x: int(get_num(x)))
        runs = []
        for index in range(0, len(color) - 2):
            for end in range(index + 3, len(color) + 1):
                if is_run(color[index:end]):
                    runs.append(color[index:end])
                else:
                    break
        all_runs.extend(runs)

    return all_runs


def get_random_pieces(number):
    """Returns the number of random pieces specified in "number".
    There could be more than the 2 existent pieces of the same color and number in the real game.
    """

    return [
        f"{all_colors[random.randint(0, len(all_colors) - 1)]} {random.randint(1,14)}"
        for _ in range(0, number)
    ]


all_pieces = [f"{color} {number}" for number in range(1, 14) for color in all_colors]

random_pieces = get_random_pieces(14)
print(find_runs(random_pieces))

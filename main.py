class Moves:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent

        # Calculate all moves
        self.moves = []
        self.moves.append([self.position[0] + 1, self.position[1] + 2])
        self.moves.append([self.position[0] + 1, self.position[1] - 2])
        self.moves.append([self.position[0] + 2, self.position[1] + 1])
        self.moves.append([self.position[0] + 2, self.position[1] - 1])
        self.moves.append([self.position[0] - 1, self.position[1] + 2])
        self.moves.append([self.position[0] - 1, self.position[1] - 2])
        self.moves.append([self.position[0] - 2, self.position[1] + 1])
        self.moves.append([self.position[0] - 2, self.position[1] - 1])

        # Calculate all possible moves inside the board
        self.possible_moves = []

        # For each move
        for move in self.moves:
            # Filter moves that have values less than zero or greater than 7
            if move[0] >= 0 and move[0] <= 7 and move[1] >= 0 and move[1] <= 7:
                self.possible_moves.append(move)

def knight_moves(start, finish):

    # Paths of knight from the start to finish
    paths = []

    # Current position and possible moves
    current = Moves(start)

    # If paths not found
    while current.position != finish:

        # Check all possible moves
        for move in current.possible_moves:
            paths.append(Moves(move, current))

        # Cycle through all paths
        current = paths[0]

        # print(paths)

        # Remove already seen paths
        paths.pop(0)

    # Backtracking
    correct_path = []

    # If not on the starting position
    while current.position != start:

        # Append current position to correct_path
        correct_path.append(current.position)
        current = current.parent

    # Append starting position to paths
    # correct_path.append(current.position)

    # Results
    print("You made it in %s" % (len(correct_path)))
    print("Paths:")
    print("\t", start, "- STARTING POSITION")
    for move in reversed(correct_path):
        print("\t", move)

    return list(reversed(correct_path))

calculate_moves = knight_moves([3, 3], [4, 3])
print('Result: ', calculate_moves)

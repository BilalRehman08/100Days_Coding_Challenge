N, M = 5, 5
n_players = 2
marks = ['X', 'O']
count_boxes = [0, 0]
grid = [['.' for i in range(M-1)] for _ in range(N-1)]
horizontal_grid = [[False for i in range(M)] for j in range(N+1)]
vertical_grid = [[False for i in range(M+1)] for j in range(N)]
# This function prints the grid of Dots-and-Boxes as the game progresses


def print_grid():
    for i in range(n_players):
        print('Player %d: %c  ' % (i+1, marks[i]), end='')
        if i < n_players-1:
            print('vs  ', end='')
    print()
    print('--' + '------' * (M-1))
    for i in range(N):
        print(' . ', end='')
        for j in range(M):
            print('---' if horizontal_grid[i][j] else '   ', end='')
            if j < M-1:
                print(' . ', end='')
        print()
        for j in range(M+1):
            print(' |  ' if vertical_grid[i][j] else '    ', end='')
            if i < N-1 and j < M-1:
                print(grid[i][j] if grid[i][j] != '.' else ' ', end='')
            print(' ', end='')
        print()
    for i in range(n_players):
        print('Player %c is %d' % (marks[i], count_boxes[i]))
    print('--' + '------' * (M-1))
# This function checks if the grid is full or not


def check_full():
    for i in range(N - 1):
        for j in range(M - 1):
            if(horizontal_grid[i][j] == False or vertical_grid[i][j] == False):
                return False
    return True
# This function checks if the given side is empty or not


def check_empty_side(i1, j1, i2, j2):
    if(i1 == i2):
        if(not horizontal_grid[i1][j1]):
            return True
    if(j1 == j2):
        if(vertical_grid[i1][j1] == False):
            return True
    return False
# This function checks if the given position is valid in the grid or not


def check_valid_position(i, j):
    if(i >= 0 and i < N and j >= 0 and j < M):
        return True
    return False
# This function checks if given side is valid or not


def check_valid_side(i1, j1, i2, j2):
    if((i1 == i2 and abs(j1 - j2) == 1) or (j1 == j2 and abs(i1 - i2) == 1)):
        return True
    return False
# This function sets the given side


def set_side(i1, j1, i2, j2):
    if(i1 == i2):
        horizontal_grid[i1][j1] = True
    else:
        vertical_grid[i1][j1] = True


def is_complete_box(i, j):
    if (horizontal_grid[i][j] and vertical_grid[i][j] and horizontal_grid[i + 1][j] and vertical_grid[i][j + 1]):
        return True
    return False


def set_box(i, j, player):
    grid[i][j] = marks[player]
    count_boxes[player] += 1


def set_neighbor_box(i1,  j1,  i2,  j2,  player):
    if(i1 == i2 and i1 != 0 and i1 != N - 1):
        if(is_complete_box(i1 - 1, j1)):
            set_box(i1 - 1, j1, player)
            return True
    elif(j1 == j2 and j1 != 0 and j1 != M - 1):
        if(is_complete_box(i1, j1-1)):
            set_box(i1, j1-1, player)
            return True
    return False

# This function checks and sets the neighbor completed boxes


def set_neighbor_boxes(i1, j1, i2, j2, player):
    flag = False
    if (i1 == i2 and i1 == N - 1):
        if (is_complete_box(i1 - 1, j1)):
            set_box(i1 - 1, j1, player)
            flag = True
    elif (j1 == j2 and j1 == M - 1):
        if (is_complete_box(i1, j1 - 1)):
            set_box(i1, j1 - 1, player)
            flag = True
    elif (is_complete_box(i1, j1)):
        set_box(i1, j1, player)
        flag = True
    if (set_neighbor_box(i1, j1, i2, j2, player)):
        flag = True
    return flag
# This function arranges the points of the side


def arrange_side_points(i1, j1, i2, j2):
    mini = min(i1, i2)
    maxi = max(i1, i2)
    i1 = mini
    i2 = maxi
    mini = min(j1, j2)
    maxi = max(j1, j2)
    j1 = mini
    j2 = maxi
    return i1, j1, i2, j2
# This function clears the game structures


def grid_clear():
    for i in range(N-1):
        for j in range(M-1):
            grid[i][j] = '.'
    for i in range(N):
        for j in range(M):
            horizontal_grid[i][j] = False
            vertical_grid[i][j] = False
    count_boxes[0] = 0
    count_boxes[1] = 0

# This function reads a valid and arranged side input


def read_input():
    i1, j1, i2, j2 = map(int, input(
        'Enter the two points of the side: ').split())
    i1, j1, i2, j2 = arrange_side_points(i1, j1, i2, j2)
    while not check_valid_position(i1, j1) or not check_valid_position(i2, j2) or \
            not check_valid_side(i1, j1, i2, j2) or not check_empty_side(i1, j1, i2, j2):
        i1, j1, i2, j2 = map(int, input(
            'Enter a valid two points of the side: ').split())
        i1, j1, i2, j2 = arrange_side_points(i1, j1, i2, j2)
    return i1, j1, i2, j2
# MAIN FUNCTION


def play_game():
    print("Dots-and-Boxes Game!")
    print("Welcome...")
    print("============================")
    player = 0
    while True:
        # Prints the grid
        print_grid()
        # Read an input position from the player
        print('Player %s is playing now' % marks[player])
        i1, j1, i2, j2 = read_input()
        print(i1)
        print(j2)
        # Set the input position with the mark
        set_side(i1, j1, i2, j2)
        # Set the neighbor boxes with the mark
        box_complete = set_neighbor_boxes(i1, j1, i2, j2, player)
        # Check if the state of the grid has a complete state
        if check_full():
            # Prints the grid
            print_grid()
            # Announcement of the final statement
            if count_boxes.count(max(count_boxes)) == 1:
                idx_max_player = count_boxes.index(max(count_boxes))
                print('Congrats, Player %s is won!' % marks[idx_max_player])
            else:
                print("Woah! That's a tie!")
            break
        # Keep the player if there is a complete box
        if not box_complete:
            # Player number changes after each turn
            player = (player + 1) % n_players


while True:
    grid_clear()
    play_game()
    c = input('Play Again [Y/N] ')
    if c not in 'yY':
        break

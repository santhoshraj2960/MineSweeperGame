from random import randint
mine_sweeper = []
mines_dict = {}
visited_dict = {}
no_of_row_cols = 9
user_input = '1 4'
all_combs = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (1,1)]
visited_dict = {}
queue = []

def build_mine_sweeper(self, no_of_row_cols):
    for row in range(0, no_of_row_cols):
        row_list = []
        for col in range(0, no_of_row_cols):
            row_col_comb = str(row)+str(col)
            row_list.append(row_col_comb)

        mine_sweeper.append(row_list)
        print row_list

    for row in range(0, no_of_row_cols):
        pos_of_mine_in_row = str(randint(0, no_of_row_cols))
        mines_dict[str(row) + pos_of_mine_in_row] = True

    print mines_dict

if user_input in mines_dict:
    print 'Lost'
else:
    find_surrounding_mines(mine_sweeper, user_input)


def find_surrounding_mines(user_input):
    queue = []
    queue.append((int(user_input.split()[0]), int(user_input.split()[1])))
    if user_input.split()[0] + user_input.split()[1] in visited_dict:
        print 'Invalid input: Already visited: enter a diff input'
        return
    elif user_input.split()[0] + user_input.split()[1] in mines_dict:
        print 'Oops you just stepped on a mine. You LOST!'
        print mines_dict
        return

    while(queue):
        neighbours_list = []
        cell = queue.pop()
        no_of_mines_surrounding_cell = 0
        
        for comb in all_combs:
            formed_cell_row = cell[0]+comb[0]
            formed_cell_col = cell[1]+comb[1]
            if (formed_cell_row < 0 or formed_cell_col < 0 or formed_cell_row >= 
                len(mine_sweeper) or formed_cell_col >= len(mine_sweeper[0])):
                continue
            else:
                if (mine_sweeper[formed_cell_row][formed_cell_col] in mines_dict):
                    no_of_mines_surrounding_cell += 1
                neighbours_list.append((formed_cell_row, formed_cell_col))
        
        if no_of_mines_surrounding_cell > 0:
            mine_sweeper[cell[0]][cell[1]] = 'M'+str(no_of_mines_surrounding_cell)
            visited_dict[str(cell[0]) + str(cell[1])] = True
        else:
            mine_sweeper[cell[0]][cell[1]] = '__'
            for cell in neighbours_list:
                if str(cell[0]) + str(cell[1]) in visited_dict:
                    continue
                else:
                    queue.append(cell)
                    visited_dict[str(cell[0]) + str(cell[1])] = True
        print 'cell = ', cell
        print 'no_of_mines_surrounding_cell = ', no_of_mines_surrounding_cell


def print_mine_sweeper():
    for row in mine_sweeper:
        print row

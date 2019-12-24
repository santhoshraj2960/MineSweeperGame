from random import randint

class MineSweeperSolver():
    def __init__(self, difficulty='easy'):
        if difficulty == 'easy':
            self.no_of_row_cols = 9
        self.mine_sweeper = []
        self.mines_dict = {}
        self.visited_dict = {}
        # all_combs - used to traverse through the minesweeper in all directions
        self.all_combs = [(1,0), (0,1), (-1,0), (0,-1), (-1,-1), (1,1)]

    def build_mine_sweeper(self):
        for row in range(0, self.no_of_row_cols):
            row_list = []
            for col in range(0, self.no_of_row_cols):
                row_col_comb = str(row)+str(col)
                row_list.append(row_col_comb)

            self.mine_sweeper.append(row_list)
            print row_list

        for row in range(0, self.no_of_row_cols):
            pos_of_mine_in_row = str(randint(0, self.no_of_row_cols))
            self.mines_dict[str(row) + pos_of_mine_in_row] = True

        #print self.mines_dict

    def find_surrounding_mines(self, user_input):
        queue = []
        queue.append((int(user_input.split()[0]), int(user_input.split()[1])))
        
        if user_input.split()[0] + user_input.split()[1] in self.visited_dict:
            print 'Invalid input: Already visited: enter a diff input'
            return True
        elif user_input.split()[0] + user_input.split()[1] in self.mines_dict:
            print 'Oops you just stepped on a mine. You LOST!'
            print self.mines_dict
            return False

        #Doing a BFS to find the surrounding mines
        while(queue):
            neighbours_list = []
            cell = queue.pop()
            no_of_mines_surrounding_cell = 0
            
            for comb in self.all_combs:
                formed_cell_row = cell[0]+comb[0]
                formed_cell_col = cell[1]+comb[1]
                if (formed_cell_row < 0 or formed_cell_col < 0 or formed_cell_row >= 
                    len(self.mine_sweeper) or 
                    formed_cell_col >= len(self.mine_sweeper[0])):
                    continue
                else:
                    if (self.mine_sweeper[formed_cell_row][formed_cell_col] in self.mines_dict):
                        no_of_mines_surrounding_cell += 1
                    neighbours_list.append((formed_cell_row, formed_cell_col))
            
            if no_of_mines_surrounding_cell > 0:
                self.mine_sweeper[cell[0]][cell[1]] = 'M'+ \
                str(no_of_mines_surrounding_cell)
                self.visited_dict[str(cell[0]) + str(cell[1])] = True
            else:
                self.mine_sweeper[cell[0]][cell[1]] = '__'
                for cell in neighbours_list:
                    if str(cell[0]) + str(cell[1]) in self.visited_dict:
                        continue
                    else:
                        queue.append(cell)
                        self.visited_dict[str(cell[0]) + str(cell[1])] = True

        self.print_mine_sweeper()

        if (len(self.visited_dict.keys()) + len(self.mines_dict.keys()) == 
            self.no_of_row_cols ** 2):
            print 'Hurray! You have successfully completed this game!'
            return False
        
        return True

    def print_mine_sweeper(self):
        for row in self.mine_sweeper:
            print row


if __name__ == '__main__':
    mine_sweeper_solver = MineSweeperSolver()
    mine_sweeper_solver.build_mine_sweeper()
    user_input = raw_input('Enter cell number as\n rowNumber<space>colNumber: ')

    while(mine_sweeper_solver.find_surrounding_mines(user_input)):
        user_input = raw_input('Enter cell number as \n rowNumber<space>colNumber: ')

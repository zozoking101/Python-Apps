# GameBoard Class
# For the game board properties
class GameBoard():
    def __init__(self):
        # For the nine spaces on the board
        self.game_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}

    def display_state(self, player, position, game_board):
        # Returns the current board state as players take turns
        game_board[position] = player
        return game_board

    @property
    # Decorator property for gameboard attribute
    def gameboard(self):
        return self.game_board

    # To clear the board
    def clearboard(self):
        for position in self.game_board:
            self.game_board[position] = ' '

    # Function to check if a symbol is at a position
    def is_position_occupied(self, game_board, index):
        if game_board[index] != ' ':
            return True

    # Function to check if all positions have been filled
    def is_board_completed(self, game_board):
        for index in range(1, 10):
            if game_board[index] == ' ':
                return False
        return True

    # Function to determine who won a game
    def is_game_won(self, game_board):
        win_conditions = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7))
        for win_condition in win_conditions:
            if ( # Checks if game positons correspond with win conditions
                game_board[win_condition[0]] == game_board[win_condition[1]]
                and game_board[win_condition[1]] == game_board[win_condition[2]]
                and game_board[win_condition[0]] != ' '):
                return True
        return False

    # Function to print game board
    def print_game_board(self, game_board):
        index = 0
        for row in range(1, 4):
            for column in range(1, 4):
                index += 1
                if column != 3:
                    print(game_board[index], end='')
                    print('|', end='')
                else:
                    print(game_board[index])
                    if row != 3:
                        print('-+-+-')

# To manage game flow
class Game():
    def __init__(self):
        self.control_board = GameBoard()
        self.game_running = True
        
    # Game start
    def game_start(self):
        self.control_board = GameBoard()
        self.game_board = self.control_board.game_board.copy()
        self.playerone = "X"
        self.playertwo = "O"
        print("X - O Game\n")
        self.player_one = "Player one"
        self.player_two = "Player two"
        print("The game board has nine spaces. Enter 1-9 to play X or O in a space")
        self.control_board.print_game_board(self.game_board)
        self.turn = 1
        self.game_running = True
        
    #Game end
    def game_end(self):
        replay = input("Enter 1 to play again or 0 or any other digit to play again: ")
        if replay == '1':
            #Clear the game board
            self.control_board.clearboard()
            self.turn = 1 #Reset turns
            self.game_start()
            #self.game_running = True
            #return True
            #self.game_start()
            #Ccontinue
        else:
            self.game_running = False
        
    # Takingturns
    def take_turn(self, player, item):
        print(player + " choose a space from 1-9: ")
        try:
            position = int(input(': '))
            if position > 9 or position < 1:
                raise Exception
        except:
            print("Pick a number between 1-9")
            return self.take_turn(player, item)

        if self.control_board.is_position_occupied(self.game_board, position):
            print("Position occupied")
            return self.take_turn(player, item)
        else:
            self.control_board.display_state(item, position, self.game_board)
            self.control_board.print_game_board(self.game_board)
            if self.control_board.is_game_won(self.game_board):
                print(player + " wins!!!")
                self.game_running = False

    #Which Player's turn
    def main(self):
        while self.game_running:
            self.game_start()
            while self.game_running:
                if self.turn % 2 != 0:
                    self.take_turn(self.player_one, "X")
                else:
                    self.take_turn(self.player_two, "O")

                if self.control_board.is_game_won(self.game_board):
                    break
                
                elif self.control_board.is_board_completed(self.game_board):
                    #Game board filled without winner or loser
                    print("Draw!")
                    break
                self.turn += 1
                
            #Game over
            self.game_running = False

# Launch the game
if __name__ == '__main__':
    Game().main()
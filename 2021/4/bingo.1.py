import sys


class Board:

    def __init__(self, matrix):
        self.marked = [ [False]*5 for _ in range(5) ]
        self.pos = {}
        for i in range(5):
            for j in range(5):
                self.pos[matrix[i][j]] = (i,j)

    def mark(self, num):
        if num in self.pos:
            i,j = self.pos[num]
            self.marked[i][j] = True

    def sum(self):
        total = 0
        for num,pos in self.pos.items():
            i,j = pos
            if not self.marked[i][j]:
                total = total + num
        return total
                    
    def winner(self):

        # check rows
        for i in range(5):
            all_marked = True
            for j in range(5):
                if not self.marked[i][j]:
                    all_marked = False
                    break
            if all_marked:
                return True

        # check columns
        for j in range(5):
            all_marked = True
            for i in range(5):
                if not self.marked[i][j]:
                    all_marked = False
                    break
            if all_marked:
                return True

        return False

    def __str__(self):
        """Make a pretty board with bold numbers"""
        board = [[0]*5 for _ in range(5)]
        for num,pos in self.pos.items():
            i,j = pos
            board[i][j] = num

        buffer = []
        for i in range(5):
            row=[]
            for j in range(5):
                if self.marked[i][j]:
                    row.append('\033[1m' + str(board[i][j]) + '\033[0m')
                else:
                    row.append(str(board[i][j]))
            buffer.append(" ".join(row))
        return "\n".join(buffer)

    
def main():

    # grab the nums
    nums = [int(i) for i in sys.stdin.readline().split(',')]

    # grab the boards
    boards = []
    line = sys.stdin.readline()
    while line:
        matrix = [0]*5
        for i in range(5):
            matrix[i] = [int(i) for i in sys.stdin.readline().split()]
        boards.append(Board(matrix))
        line = sys.stdin.readline()

    ## run through the numbers
    for num in nums:
        print("NUM = {}".format(num))
        winner = False
        for board in boards:
            board.mark(num)
            if board.winner():
                winner = True
                print(num*board.sum())
                print(board)
                break
        if winner:
            break

if __name__ == '__main__':
    main()

    
        
    

import random
class minesweeper():
    def __init__(self,size,num):
        self.size=size
        self.num=num
    ['uncovered?','flagged?','display']
    def print_board(self,board):

        top='  1 2 3 4 5 6 7 8 9 10'
        print(top)
        for i in range(self.size):
            buffer=str(i+1)+' '
            for j in board[i]:
                if j[0]==True:
                    buffer+=str(j[2])+' '
                elif j[1]==True:
                    buffer+='F'+' '
                else:
                    buffer+=' '+' '
            print(buffer[:-1])
    def get_mines(self):
        mines=[]
        while len(mines)<self.num:
            temp=(random.randint(1,self.size),random.randint(1,self.size))
            if temp not in mines:
                mines.append(temp)
        return mines
    def sub1(self, coord):
        a,b=coord
        return (a-1,b-1)
    def create_starting_board(self,mines):
        board=[]
        o=[False,False,0,False]
        for i in range(self.size):
            board.append(list([]))
            for j in range(self.size):
                board[i].append(list(o))
        for i in mines:
            mine=self.sub1(i)
            x,y=mine
            board[x][y][2]='M'
        for i in range(self.size):
            for j in range(self.size):
                c=0
                if board[i][j][2]=='M':
                    continue
                for k in range(-1,2):
                    for l in range(-1,2):
                        try:
                            if board[i+k][j+l][2]=='M':
                                c+=1
                        except:
                            pass
                board[i][j][2]=c
        return board
    def print_ending(self,board):
        for i in board:
            buffer=''
            for j in i:
                buffer+=str(j[2])+' '
            print(buffer)
        exit()
    def check_success(self,board):
        for i in board:
            for j in i:
                if j[2]!='M':
                    if not j[0]:
                        return False
        return True
    def check_death(self,board):
        for i in board:
            for j in i:
                if j[2]=='M':
                    if j[0]:
                        return True
        return False
    def check(self,board):
        if self.check_death(board):
            print('GAME OVER')
            self.print_ending(board)
        elif self.check_success(board):
            print('YOU WIN')
            self.print_ending(board)
    def richochet(self,board,coord):
        x,y=coord
        board[x][y][3]=True
        for i in range(-1,2):
            for j in range(-1,2):
                try:
                    if not board[x+i][y+j][3]:
                        board[x+i][y+j][0]=True
                        board[x+i][y+j][3]=True
                        if board[x+i][y+j][2]==0:
                            self.richochet(board,(x+i,y+j))
                except:
                    continue

        return board

terminal_minesweeper=minesweeper(10,10)
mines=terminal_minesweeper.get_mines()
board=terminal_minesweeper.create_starting_board(mines)
# terminal_minesweeper.print_board(board)
def main(board):
    while True:
        terminal_minesweeper.print_board(board)
        cmd=input()
        cmds=cmd.split()
        if cmds[0]=='uc':
            if (not board[int(cmds[1])-1][int(cmds[2])-1][0]) and (not board[int(cmds[1])-1][int(cmds[2])-1][1]):
                board[int(cmds[1])-1][int(cmds[2])-1][0]=True
                if board[int(cmds[1])-1][int(cmds[2])-1][2]==0:
                    board=terminal_minesweeper.richochet(board,(int(cmds[1])-1,int(cmds[2])-1))
            else:
                print('already uncovered')
        elif cmds[0]=='fl':
            if not board[int(cmds[1])-1][int(cmds[2])-1][1]:
                board[int(cmds[1])-1][int(cmds[2])-1][1]=True
            else:
                print('already flagged')
        elif cmds[0]=='uf':
            if board[int(cmds[1])-1][int(cmds[2])-1][2]:
                board[int(cmds[1])-1][int(cmds[2])-1][0]=False
            else:
                print('already not flagged')
        terminal_minesweeper.check(board)
main(board)

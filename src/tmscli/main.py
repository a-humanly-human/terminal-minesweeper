import random
import argparse
import importlib.metadata
class minesweeper():
    def __init__(self,size,num):
        self.size=size
        self.num=num
    ['uncovered?','flagged?','display']
    def print_board(self,board):
        top=' '+(self.size*2)*'_'
        print(top)
        for i in range(self.size):
            buffer='| '
            for j in board[i]:
                if j[0]==True:
                    buffer+=str(j[2])+' '
                elif j[1]==True:
                    buffer+='F'+' '
                else:
                    buffer+=' '+' '
            print(buffer[:-1]+'|')
        bottom=' '+(len(top)-1)*'-'
        print(bottom)
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
                            if (i+k >=0) and (j+l >=0):
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
            return True
        elif self.check_success(board):
            print('YOU WIN')
            return True
        return False
    def richochet(self,board,coord):
        x,y=coord
        board[x][y][3]=True
        for i in range(-1,2):
            for j in range(-1,2):
                if x+i>=0 and y+j>=0:
                    try:
                        if not board[x+i][y+j][3]:
                            board[x+i][y+j][0]=True
                            board[x+i][y+j][3]=True
                            if board[x+i][y+j][2]==0:
                                self.richochet(board,(x+i,y+j))
                    except:
                        continue

        return board

terminal_minesweeper=minesweeper(9,5)
# terminal_minesweeper.print_board(board)
def throw():
    print('unrecognised command, please try again')
def main_loop(board):
    try:
        while True:
            terminal_minesweeper.print_board(board)
            cmd=input()
            cmds=cmd.split()
            if len(cmds)!=3:
                throw()
                continue
            elif cmds[0] not in ['uc','uf','fl']:
                throw()
                continue
            if int(cmds[1])>terminal_minesweeper.size or int(cmds[1])<=0 or int(cmds[2])>terminal_minesweeper.size or int(cmds[2])<=0:
                print('coordinate out of range, please try again')
                continue
            if cmds[0]=='uc':
                if (not board[int(cmds[1])-1][int(cmds[2])-1][0]) and (not board[int(cmds[1])-1][int(cmds[2])-1][1]):
                    board[int(cmds[1])-1][int(cmds[2])-1][0]=True
                    if board[int(cmds[1])-1][int(cmds[2])-1][2]==0:
                        board=terminal_minesweeper.richochet(board,(int(cmds[1])-1,int(cmds[2])-1))
                else:
                    print('already uncovered or flagged')
            elif cmds[0]=='fl':
                if not board[int(cmds[1])-1][int(cmds[2])-1][1] and not board[int(cmds[1])-1][int(cmds[2])-1][0]:
                    board[int(cmds[1])-1][int(cmds[2])-1][1]=True
                else:
                    print('already flagged or already uncovered')
            elif cmds[0]=='uf':
                if board[int(cmds[1])-1][int(cmds[2])-1][1]:
                    board[int(cmds[1])-1][int(cmds[2])-1][1]=False
                else:
                    print('already not flagged')
            else:
                throw()
                continue
            if terminal_minesweeper.check(board):
                terminal_minesweeper.print_ending(board)
                exit()
    except KeyboardInterrupt:
        print('Interrupted')
        terminal_minesweeper.print_ending(board)
    except:
        if terminal_minesweeper.check(board):
            exit()
        print('ERROR')
        terminal_minesweeper.print_ending(board)
def run():
    try:
        __version__ = importlib.metadata.version("your-package-name")
    except importlib.metadata.PackageNotFoundError:
        __version__ = "0.0.0-dev"
    p=argparse.ArgumentParser(description='Minesweeper CLI')
    p.add_argument(
        '-r','--rules',
        action='store_true',
        help='gives rules'
    )
    p.add_argument(
        '-s','--size',
        type=int,
        default=9,
        help='set size to x'
    )
    p.add_argument(
        '-m','--mine_num',
        type=int,
        default=5,
        help='set number of mines to x'
    )
    p.add_argument(
        "-v", "--version", 
        action="version", 
        version=f"%(prog)s {__version__}"
    )

    args=p.parse_args()
    if args.rules:
        print_rules()
    if args.size:
        terminal_minesweeper.size=args.size
    if args.mine_num:
        terminal_minesweeper.num=args.mine_num
    mines=terminal_minesweeper.get_mines()
    board=terminal_minesweeper.create_starting_board(mines)
    main_loop(board)

def print_rules():
    place='''
  y------>
x
|
|
|
V'''
    rules='''
Minesweeper is a game where you uncover squares in a minefield, and discover where the mines are
this version has a 9 x 9 board with 10 mines in it.
commands:
uc x y = uncovers square (x,y)
fl x y = flags square (x,y)
uf x y = unflags square (x,y)
#####
Aim:
uncover every square without a mine on it.

Symbols:
F = flagged
A space = covered (unknown)
A number = the number of mines around it
M = a mine (game over)
If you step on a mine you lose, the number on the square is how many mines are around it (3 x 3 radius)
'''
    for i in rules.split('\n'):
        if i=='#####':
            print(place)
        else:
            print(i.rstrip())
        input()
    input('press enter to start:')
run()
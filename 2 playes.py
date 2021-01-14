
class TicTacToe:

    def __init__(self):
        self.__value =[[" "," "," "],[" "," "," "],[" "," "," "]]
        

    def DrawBoard(self):
        o=0
        for i in self.__value:
            for j in range(3):
                o = o+1
                if j!=2:
                    print (" "+i[j]+" |",end="")
                else:
                    print (" "+i[j])
                    if o!=9:
                        print("------------")


    def clearBoard(self):
        for i in self.__value:
            for j in range(3):
                i[j]=" "

    def newGame(self):
        while True:
            i = input("Do want to play again (y: Yes, N: No):")
            if i=='y' or i=='Y':
                self.clearBoard()
                self.DrawBoard()
                return True
            if i=='N' or i=='n':
                print("Than you.")
                return False    
            print("Wrong insertion, try again")

    def Play(self,a):
        flag=True
        while flag:
            i = input("Player '"+a+"', enter your move (row[1 to 3] column[1 to 3]):")
            v = self.CheckEntery(i)
            if v[0]:
                self.__value[v[1]][v[2]] = a
                flag=False

    def CheckDraw(self):
        for i in self.__value:
            for j in range(2):
                if i[j]==" ":
                    return False
        print("it's a draw")
        return True

    def CheckWin(self,a):
        x=[]
        for i in self.__value:
            if self.CheckRow(i,a):
                return True
        for i in range(3):
            for j in range(3):
                x.append(self.__value[j][i])
            if self.CheckColumn(x,a):
                return True
            x=[]
        if self.CheckDiagonal(a):
            return True
        return False

    def CheckColumn(self,a,b):
        for i in a:
            if i!=b:
                return False
        print("Player '"+b+"' won!")
        return True
                
    
    def CheckRow(self,a,b):
        for i in a:
            if i!=b:
                return False
        print("Player '"+b+"' won!")
        return True
            
            
    def CheckDiagonal(self,a):
        if self.__value[1][1]==" ":
            return False
        if (self.__value[0][0]==self.__value[1][1]==self.__value[2][2] or self.__value[0][2]==self.__value[1][1]==self.__value[2][0]):
            print("Player '"+a+"' won!")
            return True
        return False

    def CheckEntery(self,b):
        v=[]
        for i in b:
            if i!=" ":
                v.append(i)
        if len(v)>2 or len(v)<2:
            print("Wrong insertion values must be 2 numbers, try again")
            return [False,]
        for i in range(2):
            if not v[i].isdigit():
                print("Wrong insertion only numbers are allowed, try again")
                return [False,]
            v[i]=int(v[i])-1
        
        if v[0]>2 or v[0]<0 or v[1]>2 or v[1]<0:
            print("Wrong insertion out of range[1-3], Try again…")
            return [False,]
        if self.__value[v[0]][v[1]]!=" ":
            print("This move at ("+str(v[0]+1)+","+str(v[1]+1)+") is not valid. Try again…")
            return [False,]
        return [True,v[0],v[1]]

p = TicTacToe()
p.DrawBoard()
flag= True
while flag:
    p.Play("X")
    p.DrawBoard()
    if p.CheckWin('X'):
        flag = p.newGame()
    else:
        if p.CheckDraw():
            flag = p.newGame()
        else:
            p.Play("O")
            p.DrawBoard()
            if p.CheckWin('O'):
               flag = p.newGame()

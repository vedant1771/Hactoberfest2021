def design(board):
     for y in range(0,9):
          if(y%3==0 and y!=0):
               print("_ "*11)
          for x in range(0,9):
               if(x%3==0 and x!=0):
                    print(end=' | ')
               if(True):
                    print(board[y][x],end=' ')
          print()

def indi_inp():
     print("Enter individual number after arrow and press enter")
     temp=[[],[],[],[],[],[],[],[],[]]
     for y in range(9):
          for x in range(9):
               while True:
                    try:
                         inp=int(input('-->'))
                         if(inp>9 or inp<1):
                              raise ValueError
                         else:
                              temp[y].append(inp)
                         break
                    except:
                         print("Wrong Input!")
     return temp

def check(y,x,n,sudoku):
     if (n in sudoku[y]):
          return False
     for column in range(0,9):
          if (n == sudoku[column][x]):
               return False
     ynew=(y//3)*3
     xnew=(x//3)*3
     for column in range(0,3):
          for row in range (0,3):
               if(sudoku[ynew+column][xnew+row]==n):
                     return False
     return True

def solve(sudoku_sol):
     count=0
     for j in sudoku_sol:
          count+=j.count(0)
     if count ==0:
          return True
     for y in range(0,9):
          for x in range(0,9):
               if(sudoku_sol[y][x]==0):
                    for num in range(1,10):
                         if(check(y,x,num,sudoku_sol)):
                              sudoku_sol[y][x]=num
                              if(solve(sudoku_sol)):
                                   return True
                              sudoku_sol[y][x]=0
                    return False          
     
                    
def main():
     print('Welcome to sudoku')
     while True:
          try:
               x = str(input("1.do you want to try demo board OR 2.give board(choose 1 or 2)"))
               if(x not in '12' or x==''):
                    raise NameError
               break
          except:
               print("Wrong Input! Try again")
     if x=='1':
          print('the question grid,')
          design(sudoku)
          print()
          solve(sudoku)
          print('the solution grid,')
          design(sudoku)
          ext=input("have a nice day(click any button to exit)")
     elif x=='2':
          print("A.give individual numbers")
          print("B.give complete list")
          while True:
               try:
                    inp=str(input('Choose A/B'))
                    if inp not in 'AaBb':
                         raise NameError
                    break
               except:
                    print('Wrong Input!')
          if(inp in 'aA'):
               while True:
                    try:
                         sudoku_inp=indi_inp()
                         design(sudoku_inp)
                         print()
                         print('solution grid\n')
                         solve(sudoku_inp)
                         design(sudoku_inp)
                         ext=input("have a nice day(click any button to exit)")
                         break
                    except:
                         print("the board is invalid or an error has occured")
          elif(inp in 'bB'):
               while True:
                    try:
                         print("enter sudoku board in 2d list like this:-")
                         sudoku_inp=eval(input("{}\n".format(sudoku)))
                         design(sudoku_inp)
                         print()
                         print('solution grid\n')
                         solve(sudoku_inp)
                         design(sudoku_inp)
                         ext=input("have a nice day(click any button to exit)")
                         break
                    except:
                         print("the board is invalid or an error has occured")
#demo board
sudoku=[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
               [5, 2, 0, 0, 0, 0, 0, 0, 0], 
               [0, 8, 7, 0, 0, 0, 0, 3, 1], 
               [0, 0, 3, 0, 1, 0, 0, 8, 0], 
               [9, 0, 0, 8, 6, 3, 0, 0, 5], 
               [0, 5, 0, 0, 9, 0, 6, 0, 0], 
               [1, 3, 0, 0, 0, 0, 2, 5, 0], 
               [0, 0, 0, 0, 0, 0, 0, 7, 4], 
               [0, 0, 5, 2, 0, 6, 3, 0, 0]]
main()

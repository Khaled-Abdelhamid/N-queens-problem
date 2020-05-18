import numpy as np

# the function that checks the validity of placing a Queen in a specific row and column
def is_valid(board,N,row,col):
    # checking if the current row has any other queen
    if max(board[row,:])==1:
        return False

    # checking upper left diagonal
    k = row-1
    l = col-1
    while (k>=0 and l>=0):
        if (board[k,l] == 1):
            return False
        k=k-1
        l=l-1

    # checking lower left diagonal
    k = row+1
    l = col-1
    while (k<N and l>=0):
        if (board[k,l] == 1):
            return False
        k=k+1
        l=l-1
    return True

# this function is called recursivly to explore the solutions and stops when we reach one of the solutions
def placeQueen(board,N,col):
    # if we placed all the queens correctly and we found a solution
    if (col==N): 
        print()
        print(10*"="+"Done !!!"+10*"=")
        print(7*"="+"Board size : "+str (N)+7*"=")
        print()
        print(board)
        return True
    #for each row in the board do the folwoing
    for row in range(0,N): 
        if(is_valid(board,N,row,col)):
            board[row,col]=1
            
            if(placeQueen(board,N,col+1)==True):
                return True
            board[row,col]=0
    return False    #this happens if no possible solution found (when 1< N < 4)    

# this is a simple runner function that creates the board and call the placeQueenfunction for the first time
def main(N):
    board=np.zeros((N,N),dtype=int)
    if placeQueen(board,N,0)==False:
        print("no possible solution found for size {}".format(N))
    else: 
        return True   
    
if __name__=="__main__":
    # get the solution for N = 0 to N =10
    for i in range(0,11):
        main(i)
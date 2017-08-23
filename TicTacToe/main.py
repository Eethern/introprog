__author__ = 'chrarvi'

grid = []
coords = [[" " for x in range(3)] for y in range(3)]
n = 3

def genGrid(gridCount):
     grid = [[x in range(gridCount)] for y in range(gridCount)]
     #TODO 
  
   

def draw(gridCount, moves):
     if moves = (gridCount**2) - 1:
     return True







def init():
     grid = (coords[0][0],
             coords[1][0],
             coords[2][0],
             coords[0][1],
             coords[1][1],
             coords[1][2],
             coords[2][0],
             coords[2][1],
             coords[2][2])

     board =  """
                  0 1 2 
              0  [{0}|{1}|{2}]
                 -------
              1  [{3}|{4}|{5}]
                 -------
              2  [{6}|{7}|{8}]
                 -------
               """.format(grid[0])
                      
                      
                      
                      
                      
     print board
def hasWon():
     winConditions = (
                         [[0,0],[1,0],[2,0]],
                         [[0,1],[1,1],[2,1]],
                         [[0,2],[1,2],[2,2]],

                         [[0,0],[0,1],[0,2]],
                         [[1,0],[1,1],[1,2]],
                         [[2,0],[2,1],[2,2]],

                         [[0,0],[1,1],[2,2]],
                         [[2,0],[1,1],[0,2]]
                     )
    # for cond in winConditions:
     #     if coords[cond[0][0]][conds[0,1]]

     victor = None
     return False
def interact(player = 1):
     nextPlayer = None
     if hasWon():
          return
     elif player == 1:
          nextPlayer = 2
     else:
          nextPlayer = 1

     interact(nextPlayer)

if __name__ == "__main__":
    genGrid()
    init()


    player1 = ()
    player2 = ()
    i = 0
    #for grid
     #   if grid == "0"
      #      player

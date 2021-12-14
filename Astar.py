def euclid(a,x,y):
    return math.sqrt(math.pow((3-x),2)+math.pow((3-y),2))

print("Welcome to the the maze using A* algortihm")
print("this is the maze")
maze=[[9,0,0,1],[0,0,0,0],[0,1,0,0],[0,0,0,99]]
visited=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def printmaze:
    for i in range(4):
        for j in range(4):
            if maze[i][j]==0:
                print("_",end="\t")
            elif maze[i][j]==9:
                print("S",end="\t")
            elif maze[i][j]==99:
                print("G",end="\t")
            elif maze[i][j]==1:
                print("X",end="\t")
            else:
                print("O",end="\t")
        print("\n")
printmaze()
g=0
currentx=0
currenty=0
win=0
while win==0:
    mindis=10000
    i=currentx
    j=currenty
    if i-1>=0 and maze[i-1][j]!=1 and maze[i-1]:
        fup=g+euclid(maze,i-1,j)
        if fup<mindis:
            mindis=fup
            movex=i-1
            movey=j
    else:
        fup=999
    if i+1<=3 and maze[i+1][j]!=1:
        fdown= g+euclid(maze,i+1,j)
        if fdown<mindis:
            mindis=fdown
            movex=i+1
            movey=j
    else:
        fdown=999
    if j+1<=3 and maze[i][j+1]!=1:
        fright=g+euclid(maze,i,j+1)
        if fright<mindis:
            mindis=fright
            movex=i
            movej=j+1
    else:
        fright=999
    if j-1>=0 and maze[i][j-1]!=1:
        fleft=g+euclid(maze,i,j-1)
        if fleft<mindis:
            mindis=fleft
            movex=i
            movej=j-1
    else:
        fleft=999
    if i-1>=0 and j+1<=3 and maze[i-1][j+1]!=1:
        fne=g+euclid(maze,i-1,j+1)
        if fne<mindis:
            mindis=fne
            movex=i-1
            movey=j+1
    else:
        fne=999
    if i+1<=3 and j+1<=3 and maze[i+1][j+1]!=1:
        fse=g+euclid(maze,i+1,j+1)
        if fse<mindis:
            mindis=fse
            movex=i+1
            movey=j+1
    else:
        fse=999
    if i-1>=0 and j-1>=0 and maze[i-1][j-1]!=1:
        fnw=g+euclid(maze,i-1,j-1)
        if fnw<mindis:
            mindis=fnw
            movex=i-1
            movey=j-1
    else:
        fnw=999
    if i+1<=3 and j-1<=3 and maze[i+1][j-1]!=1:
        fsw=g+euclid(maze,i+1,j-1)
        if fsw<mindis:
            mindis=fsw
            movex=i+1
            movey=j-1
    else:
        fsw=999
    currentx=movex
    currenty=movey
maze[movex][movey]=111;
    if currentx==3 and currenty==3:
        win=1
        print("path found!")
    else:
        maze[currentx][currenty]=2
        g++










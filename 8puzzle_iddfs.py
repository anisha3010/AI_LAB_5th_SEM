def dfs(src,target,limit):
    
    if src==target:
 return True
    
    if limit<=0:
        return False
    
    
    adj = possible_moves(src)
    
    for move in adj:
        
        if dfs(move,target,limit-1):
          solution.append(move)
          return True
    return False
    
def possible_moves(state): 
   
    b = state.index(-1)  #find empty
    d = []#'d' for down, 'u' for up, 'r' for right, 'l' for left - directions array
          
    if b+3 in range(9):
        d.append('d')
    if b-3 in range(9):
        d.append('u')
    if b not in [0,3,6]:
        d.append('l')
    if b not in [2,5,8]:
        d.append('r')
    
    pos_moves = []
    for move in d:
        pos_moves.append(gen(state,move,b))
        
    # return all possible moves only if the move not in visited_states
    return [move for move in pos_moves ]
    
def gen(state, m, b): # m direction to move, b is blank
    # create a copy of current state to test the move
    temp = state.copy()                            
    
    if m=='d':
        a = temp[b+3]
        temp[b+3]=temp[b]
        temp[b]=a
    elif m=='u':
        a = temp[b-3]
        temp[b-3]=temp[b]
        temp[b]=a
    elif m=='l':
        a = temp[b-1]
        temp[b-1]=temp[b]
        temp[b]=a
    elif m=='r':
        a = temp[b+1]
        temp[b+1]=temp[b]
        temp[b]=a
    
    return temp
    
def iddfs(src,target,depth):
    
for i in range(1, depth+1):
        
        if dfs(src, target, i):
            return True
    return False

def print_grid(src):
    state = src.copy()
    state[state.index(-1)] = ' '
    print(str(state[0])+" "+str(state[1])+" "+str(state[2]),end="\n")
    print(str(state[3])+" "+str(state[4])+" "+str(state[5]),end="\n")
    print(str(state[6])+" "+str(state[7])+" "+str(state[8]),end="\n")
    print("\n")

#start 
src = [1,-1,5,3,2,8,6,4,7]
print("source state")
print_grid(src)
target = [-1,1,2,3,4,5,6,7,8]
print("goal state")
print_grid(target)
solution=[]
for i in range(1,10):
    val = iddfs(src,target,i)
    if val == True:
        print("limit="+str(i))
        solution.reverse()
        for x in solution:
            print_grid(x)
        break
    elif val == False:
        print("no solution in limit="+str(i))

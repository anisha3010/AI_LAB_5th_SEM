goal=[[0,0,0],[0,0,0],[0,0,0]]
present=[[0,0,0],[0,0,0],[0,0,0]]
temp=[[0,0,0],[0,0,0],[0,0,0]]

#display function
def display(a):
    for i in range(3):
        for j in range(3):
            if (a[i][j]==0):
                print("_",end="\t")
            else :
                print(""+str(a[i][j]),end="\t")
        print("\n")
    print("------------------")
    

print("Enter Goal matrix,0 for blank",end="\n")
for i in range(3):
    for j in range(3):
        goal[i][j]=int(input("["+str(i)+"]"+"["+str(j)+"]\t"))

display(goal)       
    
print("Enter Present matrix,0 for blank",end="\n")
for i in range(3):
    for j in range(3):
        present[i][j]=int(input("["+str(i)+"]"+"["+str(j)+"]\t"))

display(present)

count=0

def manhattan(temp1):
    
    total=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if temp1[i][j]==goal[k][l]:
                        x1=i
                        y1=j
                        x2=k
                        y2=l
            total+=abs(x2-x1)+abs(y2-y1)
    return total


def up(m,n,presenty):
    for i in range(3):
        for j in range(3):
            temp[i][j]=presenty[i][j]
    temp[m-1][n]=presenty[m][n]
    temp[m][n]=presenty[m-1][n]
    return manhattan(temp)
            
def down(m,n,presenty):
    for i in range(3):
        for j in range(3):
            temp[i][j]=presenty[i][j]
    temp[m+1][n]=presenty[m][n]
    temp[m][n]=presenty[m+1][n]
    return manhattan(temp)

def left(m,n,presenty):
    for i in range(3):
        for j in range(3):
            temp[i][j]=presenty[i][j]
    temp[m][n-1]=presenty[m][n]
    temp[m][n]=presenty[m][n-1]
    return manhattan(temp)

def right(m,n,presenty):
    for i in range(3):
        for j in range(3):
            temp[i][j]=presenty[i][j]
    temp[m][n+1]=presenty[m][n]
    temp[m][n]=presenty[m][n+1]
    return manhattan(temp)
      

diff=manhattan(present)

while (diff!=0):
    mindis=9999
    option=0
    tempx=0
    dis=0
    flag=0
    for i in range(3):
        for j in range(3):
            if (present[i][j]==0):
                flag=1
                w=i
                v=j
                if ((i-1)>=0):
                    dis=up(i,j,present)
                    if (dis<mindis):
                        mindis=dis
                        option=10
                if ((i+1)<=2):
                    dis=down(i,j,present)
                    if (dis<mindis):
                        mindis=dis
                        option=20
                if ((j-1)>=0):
                    dis=left(i,j,present)
                    if (dis<mindis):
                        mindis=dis
                        option=30
                if ((j+1)<=2):
                    dis=right(i,j,present)
                    if (dis<mindis):
                        mindis=dis
                        option=40
                
            if(flag==1):
                break
        if(flag==1):
            break
     
    if (option==10):
        print("Move UP")
        count+=1
        tempx=present[w][v]
        present[w][v]=present[w-1][v]
        present[w-1][v]=tempx
        display(present)
    elif (option==20):
        print("Move DOWN")
        count+=1
        tempx=present[w][v]
        present[w][v]=present[w+1][v]
        present[w+1][v]=tempx
        display(present)
    elif (option==30):
        print("Move LEFT")
        count+=1
        tempx=present[w][v]
        present[w][v]=present[w][v-1]
        present[w][v-1]=tempx
        display(present)
    elif (option==40):
        print("Move RIGHT")
        count+=1
        tempx=present[w][v]
        present[w][v]=present[w][v+1]
        present[w][v+1]=tempx
        display(present)

    diff=manhattan(present)
    
    if(diff==0):
        print("DONE!")
        display(present)
    elif(count>=50):
        print("no solution")
        diff=0
        







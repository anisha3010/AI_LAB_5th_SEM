def board(a1,ch1):
  for i in range(3):
    for j in range(3):
      if(a1[i][j]==1 and ch1==1):
        print("O",end='\t')
      elif a1[i][j]==1 and ch1==2:
        print("X",end='\t')
      elif a1[i][j]==2 and ch1==1:
        print("X",end='\t')
      elif a1[i][j]==2 and ch1==2:
        print("O",end='\t')
      elif a1[i][j]==0:
        print("_",end='\t')
    print('\n')
    
print("Welcome to tictac toe game")
ch=int(input(("1-playing O, 2-playing X")))
choice=int(input("Enter 1. Computer starts the game 2. User starts the game\n"))

if choice==2:
    turn=1
    a=[[0,0,0],[0,0,0],[0,0,0]]
    win=0
   
   #winning
    while(win==0):
        b=int(input("make your move"))
        c=int((b-1)/3)
        d=int((b-1)%3)
        if(a[c][d]==0):
            a[c][d]=1
            placed=0
            board(a,ch)
        else :
            print("can't place")
            continue
       
        print("MY TURN")
        if(placed==0):
            for m in range(3):
                count=0;
                for n in range(3):
                    if(a[m][n]==2):
                        count+=1
                    if (count==2):
                        for p in range(3):
                            if(a[m][p]==0):
                                a[m][p]=2
                                #print("X placed in "+str((m*3)+1+p))
                                placed=1
                                turn+=1
                                win=1
                                print("The computer has beaten you!")
                                break

                if(placed==1):
                    break
       
        if(placed==0):
            for m in range(3):
                count=0;
                for n in range(3):
                    if(a[n][m]==2):
                        count+=1
                    if (count==2):
                        for p in range(3):
                            if(a[p][m]==0):
                                a[p][m]=2
                                #print("X placed in "+str((p*3)+1+m))
                                placed=1
                                turn+=1
                                win=1
                                print("The computer has beaten you!")
                                break

                if(placed==1):
                    break
       
        if(placed==0):
            if((a[0][0]+a[1][1]+a[2][2])==4):
                if(a[0][0]==0):
                    a[0][0]=2
                    #print("X placed in 1")
                    placed=1
                    turn+=1
                    win=1
                    print("The computer has beaten you!")
                elif(a[1][1]==0):
                    a[1][1]=2
                    #print("X placed in 5")
                    placed=1
                    turn+=1
                    win=1
                    print("The computer has beaten you!")
                elif(a[2][2]==0):
                    a[2][2]=2
                    #print("X placed in 9")
                    placed=1
                    turn+=1
                    win=1
                    print("The computer has beaten you!")
        if(placed==0):
            if((a[0][2]+a[1][1]+a[2][0])==4):
                if(a[0][2]==0):
                    a[0][2]=2
                    #print("X placed in 3")
                    placed=1
                    turn+=1
                    win=1
                    print("The computer has beaten you!")
                elif(a[1][1]==0):
                    a[1][1]=2
                   # print("X placed in 5")
                    placed=1
                    turn+=1
                    win=1
                    print("The computer has beaten you!")
                elif(a[2][0]==0):
                    a[2][0]=2
                    #print("X placed in 7")
                    placed=1
                    turn+=1
                    win=1
                    print("The computer has beaten you!")

        if(placed==0):
            for m in range(3):
                count=0;
                for n in range(3):
                    if(a[m][n]==1):
                        count+=1
                    if (count==2):
                        for p in range(3):
                            if(a[m][p]==0):
                                a[m][p]=2
                                #print("X placed in "+str((m*3)+1+p))
                                placed=1
                                turn+=1
                               
                                break

                if(placed==1):
                    break
       
        if(placed==0):
            for m in range(3):
                count=0;
                for n in range(3):
                    if(a[n][m]==1):
                        count+=1
                    if (count==2):
                        for p in range(3):
                            if(a[p][m]==0):
                                a[p][m]=2
                                #print("X placed in "+str((p*3)+1+m))
                                placed=1
                                turn+=1
                                break

                if(placed==1):
                    break
       
        if(placed==0):
            if(a[0][0]==1 and a[1][1]==1 and a[2][2]==0):
                a[2][2]=2
                #print("X placed in 1")
                placed=1
                turn+=1
            elif(a[0][0]==1 and a[1][1]==0 and a[2][2]==1):
                a[1][1]=2
                #print("X placed in 5")
                placed=1
                turn+=1
            elif(a[0][0]==0 and a[1][1]==1 and a[2][2]==1):
                a[0][0]=2
                #print("X placed in 9")
                placed=1
                turn+=1
        if(placed==0):
            if(a[0][2]==1 and a[1][1]==1 and a[2][0]==0):
                a[2][0]=2
                #print("X placed in 7")
                placed=1
                turn+=1
            elif(a[0][2]==1 and a[1][1]==0 and a[2][0]==1):
                a[1][1]=2
                #print("X placed in 5")
                placed=1
                turn+=1
            elif(a[0][2]==0 and a[1][1]==1 and a[2][0]==1):
                a[0][2]=2
                #print("X placed in 3")
                placed=1
                turn+=1

        if(placed==0):
            if (a[1][1]==0 and turn==1):
                a[1][1]=2
                placed=1
                turn+=1
            elif a[1][1]==1 and turn==1:
                a[0][0]=2
                placed=1
                turn+=1
            elif a[1][1]==2 and turn==2:
                if a[0][0]==1 or a[0][2]==1 or a[2][0]==1 or a[2][2]==1:
                    if a[0][1]==0:
                        a[0][1]=2
                        placed=1
                        turn+=1
                    elif a[1][0]==0:
                        a[1][0]=2
                        placed=1
                        turn+=1
                    elif a[1][2]==0:
                       a[1][2]=2
                       placed=1
                       turn+=1
                    elif a[2][1]==0:
                       a[2][1]=2
                       placed=1
                       turn+=1
            elif a[0][0]==2 and a[1][1]==1 and a[2][2]==1 and turn==2:
                a[0][2]=2
                placed=1
                turn+=1
        if placed==0:
          if a[0][0]==0:
            a[0][0]=2
            placed=1
            turn+=1
          elif a[2][0]==0:
            a[2][0]=2
            placed=1
            turn+=1
          elif a[0][2]==0:
            a[0][2]=2
            placed=1
            turn+=1
          elif a[2][2]==0:
            a[2][2]=2
            placed=1
            turn+=1
                
        if placed==0:
            print("draw")
            win=1
        if placed==1:
          board(a,ch)

if choice==1:
  a=[[0,0,0],[0,0,0],[0,0,0]]
  win=0
  a[0][0]=2
  turn=0
  board(a,ch)
  while(win==0):
    
    if(a[0][0]!=0 and a[0][1]!=0 and a[0][2]!=0 and a[1][0]!=0 and a[1][1]!=0 and a[1][2]!=0 and a[2][0]!=0 and a[2][1]!=0 and a[2][2]!=0):
      print("Its a draw")
      win=1
      break
    b=int(input("Make your move"))
    c=int((b-1)/3)
    d=int((b-1)%3)
    if(a[c][d]==0):
      a[c][d]=1
      placed=0
    else :
      print("can't place")
      continue
    if(placed==0):
      for m in range(3):
        count=0
        for n in range(3):
          if(a[m][n]==2):
            count+=1
        if (count==2):
          for p in range(3):
            if(a[m][p]==0):
              a[m][p]=2
              #print("X placed in "+str((m*3)+1+p))
              placed=1
              turn+=1
              win=1
              print("The computer has beaten you!")
              board(a,ch)
              break

      if(placed==1):
        break
    if(placed==0):
      for m in range(3):
        count=0
        for n in range(3):
          if(a[n][m]==2):
            count+=1
        if (count==2):
          for p in range(3):
            if(a[p][m]==0):
              a[p][m]=2
              #print("X placed in "+str((p*3)+1+m))
              placed=1
              turn+=1
              win=1
              print("The computer has beaten you!")
              board(a,ch)
              break
      if(placed==1):
        break
    if placed==0:
      if((a[0][0]+a[1][1]+a[2][2])==4):
        if(a[0][0]==0):
          a[0][0]=2
          #print("X placed in 1")
          placed=1
          turn+=1
          win=1
          print("The computer has beaten you!")
        elif(a[1][1]==0):
          a[1][1]=2
          print("X placed in 5")
          placed=1
          turn+=1
          win=1
          print("The computer has beaten you!")
        elif(a[2][2]==0):
          a[2][2]=2
          #print("X placed in 9")
          placed=1
          turn+=1
          win=1
          print("The computer has beaten you!")
                    
                
    if(placed==0):
      if((a[0][2]+a[1][1]+a[2][0])==4):
        if(a[0][2]==0):
          a[0][2]=2
          #print("X placed in 3")
          placed=1
          turn+=1
          win=1
          print("The computer has beaten you!")
        elif(a[1][1]==0):
          a[1][1]=2
          #print("X placed in 5")
          placed=1
          turn+=1
          win=1
          print("The computer has beaten you!")
        elif(a[2][0]==0):
          a[2][0]=2
          #print("X placed in 7")
          placed=1
          turn+=1
          win=1
          print("The computer has beaten you!")
    if(placed==0):
          for m in range(3):
              count=0;
              for n in range(3):
                  if(a[m][n]==1):
                      count+=1
                  if (count==2):
                      for p in range(3):
                          if(a[m][p]==0):
                              a[m][p]=2
                              #print("X placed in "+str((m*3)+1+p))
                              placed=1
                              turn+=1
                              
                              break

              if(placed==1):
                  break
        #column
    if(placed==0):
        for m in range(3):
            count=0;
            for n in range(3):
                if(a[n][m]==1):
                    count+=1
                if (count==2):
                    for p in range(3):
                        if(a[p][m]==0):
                            a[p][m]=2
                            #print("X placed in "+str((p*3)+1+m))
                            placed=1
                            turn+=1
                            break

            if(placed==1):
                break
        #diagonal
    if(placed==0):
        if(a[0][0]==1 and a[1][1]==1 and a[2][2]==0):
            a[2][2]=2
            #print("X placed in 1")
            placed=1
            turn+=1
        elif(a[0][0]==1 and a[1][1]==0 and a[2][2]==1):
            a[1][1]=2
            #print("X placed in 5")
            placed=1
            turn+=1
        elif(a[0][0]==0 and a[1][1]==1 and a[2][2]==1):
            a[0][0]=2
            #print("X placed in 9")
            placed=1
            turn+=1
    if(placed==0):
        if(a[0][2]==1 and a[1][1]==1 and a[2][0]==0):
            a[2][0]=2
            #print("X placed in 7")
            placed=1
            turn+=1
        elif(a[0][2]==1 and a[1][1]==0 and a[2][0]==1):
            a[1][1]=2
            #print("X placed in 5")
            placed=1
            turn+=1
        elif(a[0][2]==0 and a[1][1]==1 and a[2][0]==1):
            a[0][2]=2
            #print("X placed in 3")
            placed=1
            turn+=1
    if(placed==0):
          if (a[1][1]==1):
              if(a[2][2]==0 and turn==0):
                  a[2][2]=2
                  #print("X placed in 9")
                  placed=1
                  turn+=1
    if(placed==0):
      if(turn==0):
        
        
        if(a[0][1]==1 or a[0][2]==1 or a[2][1]==1 or a[2][2]==1):
          #print("this cond")
          a[2][0]=2
          placed+=1
          turn+=1
        elif(a[1][0]==1 or a[1][2]==1 or a[2][0]==1):
          
          a[0][2]=2
          placed+=1
          turn+=1
      elif(turn==1):
        
        if(a[0][2]==0 and a[0][1]==0 and a[1][2]==0):
          
          a[0][2]=2
          placed+=1
          turn+=1
        elif(a[2][0]==0 and a[1][0]==0 and a[2][1]==0):
          a[2][0]=2
          placed+=1
          turn+=1
        elif(a[2][2]==0 and a[2][1]==0 and a[1][2]==0):
          a[2][2]=2
          placed+=1
          turn+=1
    if(placed==0):
      print("draw")
      win=1
    if(placed==1):
      board(a,ch)
     
    
  
    



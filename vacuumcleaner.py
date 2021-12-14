print("VACUUM CLEANER DEMO")
choice=int(input("1-simple reflex,2-model based"))
if choice==1:
    print("welcome to simple reflex vacuum cleaner")
    print("2 rooms, A and B")

    room=input("enter current room")
    print("Switching on vacuum cleaner")
    ch=1
    while ch!=0:
        
        statcurrent=int(input("enter status of room "+room+"(1-dirty,0-clean)"))
        if statcurrent==1:
            action="Suck"
            
        else:
            if room=='A':
                action="clean!-moving right"
                room='B'
            else:
                action="clean!-moving left"
                room='A'
        print("action: ",action)
        
        print("current room",room)
        
        ch=int(input("would you like to switch off the vacuum cleaner?0-switch it off,1-not stop"))
if choice==2:
    print("welcome to model based reflex vacuum cleaner")
    print("2 rooms, A and B")
    statA=int(input(("enter status of room A(1-dirty,0-clean)")))
    statB=int(input(("enter status of room B(1-dirty,0-clean)")))
    percept={'A':statA,'B':statB}
    print("status of both rooms before cleaning")
    print(percept)
    room=input("enter current room")
    stat=1

    if percept[room]==1:
        percept[room]=0
        if room=='A':
            action="Suck\nMoving right"
            room='B'
        else:
            action="Suck\nMoving left"
            room='A'
    else:
        if room=='A':
            action="Moving right"
            room='B'
        else:
            action="Moving left"
            room='A'
    print(action)
    if percept[room]==1:
        action="Suck\nNo ops"
        percept[room]=0
    else:
        action="No ops"
    print(action)
    print("status of both rooms after cleaning")
    print(percept)

VACUUM CLEANER DEMO
1-simple reflex,2-model based1
welcome to simple reflex vacuum cleaner
2 rooms, A and B
enter current roomA
Switching on vacuum cleaner
enter status of room A(1-dirty,0-clean)1
action:  Suck
current room A
would you like to switch off the vacuum cleaner?0-switch it off,1-not stop1
enter status of room A(1-dirty,0-clean)0
action:  clean!-moving right
current room B
would you like to switch off the vacuum cleaner?0-switch it off,1-not stop1
enter status of room B(1-dirty,0-clean)1
action:  Suck
current room B
would you like to switch off the vacuum cleaner?0-switch it off,1-not stop0

VACUUM CLEANER DEMO
1-simple reflex,2-model based2
welcome to model based reflex vacuum cleaner
2 rooms, A and B
enter status of room A(1-dirty,0-clean)1
enter status of room B(1-dirty,0-clean)0
status of both rooms before cleaning
{'A': 1, 'B': 0}
enter current roomB
Moving left
Suck
No ops
status of both rooms after cleaning
{'A': 0, 'B': 0}




















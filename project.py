def game(c1,c2):
    if(count1>count2):
        print("\nfirst player won\n ")
    elif(count1<count2):
        print("\nSecond player win\n")
    else:
        print("\nThere is a tie in the match\n ")
               
count1=0
count2=0
i=0
while True: 
    print("R. ROCK")
    print("P. PAPER")
    print("S. SCISSOR")
    print("E. Exit")
    choice1 = input("\n input your first choice ")
    choice2 = input("\n input your second  choice ")
    i=i+1
    if (choice1 == "R" and choice2 == "S") :
        
        print("\nFirst player gains 1 point \n")
        count1=count1+1
    if(i==3):
        game(count1,count2)
    elif(choice1==choice2):
        print("\nDRAW\n")
        
    elif(choice1 == "S" and choice2 == "R"):
        print("\n second player gains 1 point\n ")
        count2=count2+1
        
    elif(choice1 == "P" and choice2 == "S"):
        print("\n second player gains 1 point\n ")
        count2=count2+1
    elif(choice1 == "S" and choice2 == "P"):
        print("\nfirst player gains 1 point \n")
        count1=count1+1
        
    elif(choice1 == "P" and choice2 == "R"):
        print("\nfirst player gains 1 point\n ")
        count1=count1+1
        
    elif(choice1 == "R" and choice2 == "P"):
        print("\nsecond player gains 1 point\n ")
        count2=count2+1
    
    if (choice1 == "E" and choice2=="E" ):
        print("\nprogram ended \n")
        quit()
game(count1,count2)        
 

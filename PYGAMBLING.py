import keyboard
import math
import numpy
import sys
tokens = 5


running = True
print ("Welcome to PYGAMBLING")
a = input ("You have 5 tokens, do you wish to play?(Yes|No): ")
if a == ("no"):
    sys.exit()
if a == ("yes"):
    print ("Rules: I costs 1 to roll, get as many tokens as you can")
while running:
    numb = math.ceil(numpy.random.rand()*5 )
    gamble = input (f"You have {tokens} tokens press g to roll")
    if gamble == ("g"):
        tokens - 1
        print(f"{numb}")
        if numb == 1:
            tokens -= 1
            print("You rolled Unlucky")
        if numb == 2:
            tokens += 0
            print("You rolled Common")
        if numb == 3:
            tokens += 1
            print ("You rolled Uncommon")
        if numb == 4:
            tokens += 2
            print ("You rolled Rare")
        if numb == 5:
            tokens += 3
            print("You rolled Epic")
        b = input (f"You now have {tokens} tokens, do you wish to play again?(Yes|No)")
        if b == ("no"):
            sys.exit()
        if b == ("yes"):
            pass
                
                
        
        


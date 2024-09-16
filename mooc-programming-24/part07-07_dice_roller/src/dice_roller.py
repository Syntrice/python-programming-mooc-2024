# Write your solution here

from random import choices

def roll(die: str):
    match die:
        case "A":
            return choices([3,6],weights=[5,1], k=1)[0]
        case "B":
            return choices([2,5],weights=[3,3], k=1)[0]
        case "C":
            return choices([1,4],weights=[1,5], k=1)[0]
        case _:
            raise ValueError

def play(die1: str, die2: str, times: int):
    die1_wins = 0
    die2_wins = 0
    draws = 0
    
    for i in range(times):
        die1_roll = roll(die1)
        die2_roll = roll(die2)
        
        if die1_roll == die2_roll:
            draws += 1
            continue
        elif die1_roll > die2_roll:
            die1_wins += 1
            continue
        else:
            die2_wins += 1
            continue
    
    return (die1_wins, die2_wins, draws)
        
if __name__ == "__main__":
    for i in range(20):
        print(roll("A"), " ", end="")
    print()
    for i in range(20):
        print(roll("B"), " ", end="")
    print()
    for i in range(20):
        print(roll("C"), " ", end="")
import random 

def thegame():
    yourhand = input("'r' for rock, 's' for scissors, 'p' for paper: \n")
    pchand = random.choice(['r', 'p', 's'])

    if yourhand == pchand:
        return 'Its a tie'
    if winnergame(yourhand, pchand):
       return 'You won!'
    
    return 'You lost!'
       
def winnergame(yourhand, pchand):
    if((yourhand == 'r' and pchand == 's')or(yourhand == 's' and pchand == 'p')or (yourhand == 'p' and pchand == '')):
        return 'true'
#r>s p>r s>p r>

print(thegame())
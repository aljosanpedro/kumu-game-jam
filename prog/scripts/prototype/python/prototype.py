from random     import seed
from time       import sleep

from bugtongs   import Bugtongs
from cards      import Cards

    
def main():
    # BATTLE START
    print("\n---BATTLE START!---\n")
    
    seed() # RNG set-up
    Bugtongs() # load real & fake bugtongs and their attributes


    # ROUND START
    print("\n---ROUND START!---\n")
    
    # Load Bugtongs & Cards
    bugtongs = Bugtongs.draw() # [player,enemy,fake]
    
    cards = Cards.load(bugtongs) # player & enemy bugtongs -> cards
    Cards.set_face_up(cards, False)

    
    # MEMORIZE PHASE
    print("\n---MEMORIZE PHASE---\n")
    
    Cards.set_face_up(cards, True)
    
    timer(15)
    
    Cards.set_face_up(cards, False)
    
    
    # PLAY PHASE
    print("\n---PLAY PHASE---\n")
    
    # Announcer reads 1st half of a drawn bugtong
    
    # replace timer w/ smth that can track time instead
    timer(5)


def timer(time):
    print("---Timer---")
    for t in range(time,0,-1):
        print(t)
        sleep(1)
    print()
    

if __name__ == "__main__":
    main()

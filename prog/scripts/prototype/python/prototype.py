from phases      import Phases
from bugtongs    import Bugtongs
from cards       import Cards

    
def main():
    # BATTLE START
    Phases.battle_start()
    
    # ROUND START
    Phases.round_start()
    
    bugtongs = Bugtongs.draw() # [player,enemy,fake]
    
    cards = Cards.load(bugtongs) # player & enemy bugtongs -> cards
    Cards.set_face_up(cards, False)
    
    # MEMORIZE PHASE
    Phases.memorization()
    
    Cards.set_face_up(cards, True)
    Phases.memorization_timer_input() # timer; [Enter] -> skip, [G] -> guide
    Cards.set_face_up(cards, False)
    
    # PLAY PHASE
    Phases.play()
    
    # Announcer reads 1st half of a drawn bugtong
    # use "bugtongs" list in this file
    
    # timer, input
    

if __name__ == "__main__":
    main()

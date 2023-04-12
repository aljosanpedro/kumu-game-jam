from random     import choice

from phase      import Phase
from bugtong    import Bugtong
from card       import Card

    
def main():
    # BATTLE START
    Phase.battle_start()
    
    # ROUND START
    Phase.round_start()
    
    bugtongs = Bugtong.draw_bugtongs() # [player,enemy,fake]
    
    cards = Card.load_cards(bugtongs) # player & enemy Bugtong -> cards
    Card.set_face_up(cards, False)
    
    # MEMORIZE PHASE
    Phase.memory_start()
    
    Card.set_face_up(cards, True)
    Phase.memory_timer_input() # timer; [Enter] -> skip, [G] -> guide
    Card.set_face_up(cards, False)
    
    Phase.done()
    
    # PLAY PHASE
    Phase.play_start()
    
    bugtong = choice(bugtongs)
    Phase.play_read(bugtong)

    action = Phase.play_timer_input()
    
    result = Phase.play_judge(bugtong, cards, action)
    
    #Characters.apply_result(result)
    
    Phase.done()
    


if __name__ == "__main__":
    main()

# Imports
from control        import Control
from phases.memory  import MemoryPhase
from phases.play    import PlayPhase
from bugtong        import Bugtong
from card           import Card


# Main
def main():
    battle_start()
    
    bugtongs, cards = round_start()
    
    memory_phase(cards)
    
    play_phase(bugtongs, cards)
    

# Flow Methods
def battle_start():
    Control.start("battle")
    
    Bugtong.load_raws() # load real & fake bugtongs and their attributes


def round_start():
    Control.start("round")
    
    bugtongs = Bugtong.draw_for_round() # [player,enemy,fake]
    
    cards = Card.load_from_bugtongs(bugtongs) # player & enemy Bugtong -> cards
    Card.set_face_up(cards, False)
    
    return [bugtongs, cards]


def memory_phase(cards):
    phase = "memory"
    Control.start(phase)
    memory_phase = MemoryPhase(15) # set time
    
    Card.set_face_up(cards, True)
    
    input = MemoryPhase.timer_input(memory_phase) # timer; [Enter] -> skip, [G] -> guide
    action = MemoryPhase.input_to_action(input)
    MemoryPhase.print_action(action, phase)
    
    Card.set_face_up(cards, False)
    
    Control.end()


def play_phase(bugtongs, cards):
    phase = "play"
    Control.start(phase)
    play_phase = PlayPhase(10)
    
    bugtong = Bugtong.draw_reading(bugtongs)
    PlayPhase.read(bugtong)

    input = PlayPhase.timer_input(play_phase)
    action = PlayPhase.input_to_action(input)
    PlayPhase.print_action(action, phase)
    
    result, owner = PlayPhase.judge(bugtong, cards, action)
    Card.set_face_up(cards, True)
    PlayPhase.print_results(bugtong, result, owner)
    
    #Characters.apply_result(result)
    
    Control.end()


# Run
if __name__ == "__main__":
    main()

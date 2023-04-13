# Imports
from control        import Control

from phases.memory  import MemoryPhase
from phases.play    import PlayPhase
from phases.result  import Result

from bugtong        import Bugtong
from card           import Card

from character      import Character


# Main
def main():
    # Battle Start
    characters = battle_start()
    
    while True:   
        # Is Battle Done? 
        winner = Control.is_battle_done(characters)
        
        if not winner == "":
            battle_end(winner)
            break
        
        # Round Proper
        bugtongs, cards = round_start(characters)
        
        characters = memory_phase(cards)
        
        bugtong, action = play_phase(bugtongs)
        
        round_results(bugtong, cards, action, characters)
        
    # Battle End
    return


# Flow Methods
def battle_start() -> list:
    Control.print_phase("battle start")
    
    # Characters
    player = Character("Rara", 100, "idle")
    enemy = Character("Pina", 100, "idle")
    
    # Bugtongs
    Bugtong.load_raws() # load real & fake bugtongs and their attributes

    return [player, enemy]


def round_start(characters) -> list:
    # Start
    Control.print_phase("round start")
    
    # Characters
    Character.set_anim_both(characters, "idle")

    # Bugtongs
    bugtongs = Bugtong.draw_for_round() # [player,enemy,fake]
    
    # Cards
    cards = Card.load_from_bugtongs(bugtongs) # player & enemy Bugtong -> cards
    Card.set_face_up(cards, False)
    
    # End
    memory_phase_vars = [cards, characters]
    return memory_phase_vars


def memory_phase(memory_phase_vars) -> list:
    # Start
    cards, characters = memory_phase_vars
    phase = "memory phase"
    Control.print_phase(phase)
    memory_phase = MemoryPhase(15) # set time
    
    # Cards Face: UP
    Character.set_anim_both(characters, "casting")
    
    Card.set_face_up(cards, True)
    input = MemoryPhase.timer_input(memory_phase) # timer; [Enter] -> skip, [G] -> guide
    action = MemoryPhase.input_to_action(input)
    MemoryPhase.print_action(action, phase)
    
    # Cards Face: DOWN
    Card.set_face_up(cards, False)
    
    # End
    Control.end()
    return characters


def play_phase(bugtongs) -> list:
    # Start
    phase = "play phase"
    Control.print_phase(phase)
    play_phase = PlayPhase(10)
    
    # 1st Half Reading
    bugtong = Bugtong.draw_reading(bugtongs)
    PlayPhase.read(bugtong)

    # Player Action
    input = PlayPhase.timer_input(play_phase)
    action = PlayPhase.input_to_action(input)
    PlayPhase.print_action(action, phase)
    
    # End
    Control.end()
    return [bugtong, action]


def round_results(bugtong, cards, action, characters):
    phase = "results phase"
    Control.print_phase(phase)
    
    result, owner = Result.judge(bugtong, cards, action)
    Card.set_face_up(cards, True)
    Result.print_results(bugtong, result, owner)
    
    #Character.apply_result(action, result, characters)
    
    Control.end()
    Control.enter_to_continue()
    

def battle_end(winner):
    Control.end("battle")
    
    print(f"Winner: {winner}\n")


# Run
if __name__ == "__main__":
    main()

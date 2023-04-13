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
    player, enemy = battle_start()
    
    while True:   
        # Is Battle Done? 
        winner = Control.is_battle_done(player, enemy)
        
        if not winner == "":
            battle_end(winner)
            break
        
        # Round Proper
        bugtongs, cards = round_start(player, enemy)
        
        memory_phase(cards)
        
        bugtong, action = play_phase(bugtongs)
        
        round_results(bugtong, cards, action)
        
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


def round_start(player, enemy) -> list:
    Control.print_phase("round start")
    
    # Characters
    player.status()
    enemy.status()
    
    # Bugtongs
    bugtongs = Bugtong.draw_for_round() # [player,enemy,fake]
    
    # Cards
    cards = Card.load_from_bugtongs(bugtongs) # player & enemy Bugtong -> cards
    Card.set_face_up(cards, False)
    
    return [bugtongs, cards]


def memory_phase(cards):
    phase = "memory phase"
    Control.print_phase(phase)
    memory_phase = MemoryPhase(15) # set time
    
    Card.set_face_up(cards, True)
    
    input = MemoryPhase.timer_input(memory_phase) # timer; [Enter] -> skip, [G] -> guide
    action = MemoryPhase.input_to_action(input)
    MemoryPhase.print_action(action, phase)
    
    Card.set_face_up(cards, False)
    
    Control.end()


def play_phase(bugtongs) -> list:
    phase = "play phase"
    Control.print_phase(phase)
    play_phase = PlayPhase(10)
    
    bugtong = Bugtong.draw_reading(bugtongs)
    PlayPhase.read(bugtong)

    input = PlayPhase.timer_input(play_phase)
    action = PlayPhase.input_to_action(input)
    PlayPhase.print_action(action, phase)
    
    Control.end()
    
    return [bugtong, action]


def round_results(bugtong, cards, action):
    phase = "results phase"
    Control.print_phase(phase)
    
    result, owner = Result.judge(bugtong, cards, action)
    Card.set_face_up(cards, True)
    Result.print_results(bugtong, result, owner)
    
    #Characters.apply_result(result)
    
    Control.end()
    Control.enter_to_continue()
    

def battle_end(winner):
    Control.end("battle")
    
    print(f"Winner: {winner}\n")


# Run
if __name__ == "__main__":
    main()
